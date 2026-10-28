# Thread safety in plug-ins

**Framework**: Professional-Video-Applications  
**Role**: Article

Learn about reentrancy for plug-ins and best practices to make them thread safe.

## Overview

In FxPlug 4, the framework handles requests from the host application on a serial queue on a background thread of the plug-in. Many requests move to a concurrent queue for processing by your plug-in. This avoids blocking incoming requests from other threads. It also allows processing of requests sent asynchronously from the same thread in the host application.

This background processing means you need to be careful to not read from and write to the same objects or memory on different threads at the same time. This includes your plug-in’s instance variables and properties, and those of any other objects you access during your plug-in’s lifetime.

### Understand reentrancy in Final Cut Pro and Motion

The rendering systems in Final Cut Pro and Motion generally work in two phases:

- Generating a graph of the objects you want to render and composite
- Performing the actual rendering and compositing of those objects

These two phases happen on different threads in the host application so they can pipeline together. Depending on the number of GPUs in the user’s machine, there may be one or more of these threads running concurrently.

For example, on a dual GPU system, the host may be building the graphs for frames `n` and `n+1` while rendering the graphs from frames `n-2` and `n-1`. This concurrent approach means the host does more work at once, fully utilizing the CPUs and GPUs when possible.

### Use best practices to make your plug-ins reentrant

FxPlug 3 and earlier also called your plug-ins on multiple threads at the same time. Using  a property, you turned this functionality off and required serial processing from the host. That property does nothing in FxPlug 4, so if you need to make non-reentrant code reentrant, the following strategies may help.

#### Use Immutable Data

Data structures that you canʼt modify are safe to use on multiple threads at the same time, if you don’t delete them on any thread while in use by another. Because you can’t update them, no thread receives old or partially changed data when you access it. Using the immutable forms of the standard Cocoa containers, such as [`NSArray`](../Foundation/nsarray.md) and [`NSDictionary`](../Foundation/nsdictionary.md), instead of the mutable forms, such as [`NSMutableArray`](../Foundation/nsmutablearray.md) and [`NSMutableDictionary`](../Foundation/nsmutabledictionary.md), is a good first step. You must also ensure that any classes you design have immutable variants that you use across threads.

#### Use a New Copy

If you need to mutate data in your plug-in, you can safely do so by having each thread create its own copy of the data it needs. Copy an existing immutable structure into a mutable one locally, or create all instances as you need them and then dispose of them when youʼre done. This approach ensures you never share them between threads. Making copies or creating objects as you need them may have performance implications if the objects are large or you need to perform a lot of computation to create them.

#### Use Synchronization Primitives

If it’s not possible to use immutable data or to always use a copy of the data you want to work with, you can synchronize access to your data between threads using synchronization primitives like locks, mutexes, semaphores, and condition variables. Each of these objects has its own behaviors, but in general they allow only one thread to access the data at a time, or they keep track of how many times the system accesses the data before allowing processing to continue. For example, you can use an [`NSLock`](../Foundation/nslock.md) object around your calls that access shared data. In the following code from the `FxShape` example, `lastPositionLock` is an `NSLock` used in `FxShapeOSC` that guards access to the `lastObjectPosition`:

**Swift**:

```swift
let lastPositionLock = NSLock()

@objc(FxShapeOSC) class FxShapeOSC: NSObject, FxOnScreenControl_v4
{
    let apiManager: PROAPIAccessing!
    var lastObjectPosition = (x:0.0, y:0.0)    

// ...

    func mouseDown(atPositionX mousePositionX: Double, positionY mousePositionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>?, at time: CMTime)
    {
        var lastObjectPos = lastObjectPosition
        let oscAPI = apiManager!.api(for: FxOnScreenControlAPI_v4.self) as! FxOnScreenControlAPI_v4
        lastPositionLock.lock()
        oscAPI.convertPoint(fromSpace: UInt(kFxDrawingCoordinates_CANVAS), fromX: mousePositionX, fromY: mousePositionY, toSpace: UInt(kFxDrawingCoordinates_OBJECT), toX: &lastObjectPos.x, toY: &lastObjectPos.y)
        lastObjectPosition = lastObjectPos
        lastPositionLock.unlock()
        forceUpdate?.pointee = false
    }

// ...

}
```

**Objective-C**:

```objc
@implementation FxShapeOSC
{
    NSLock* lastPositionLock;
}

- (instancetype)initWithAPIManager:(id<PROAPIAccessing>)newAPIManager
{
    self = [super init];
    
    if (self != nil)
    {
        apiManager = newAPIManager;
        lastPositionLock = [[NSLock alloc] init];
    }
    
    return self;
}

- (void)dealloc
{
    [lastPositionLock release];
    [super dealloc];
}

// ...

- (void)mouseDownAtPositionX:(double)mousePositionX
                   positionY:(double)mousePositionY
                  activePart:(NSInteger)activePart
                   modifiers:(FxModifierKeys)modifiers
                 forceUpdate:(BOOL *)forceUpdate
                      atTime:(CMTime)time
{
    id<FxOnScreenControlAPI_v4> oscAPI  = [apiManager apiForProtocol:@protocol(FxOnScreenControlAPI_v4)];
    [lastPositionLock lock];
    [oscAPI convertPointFromSpace:kFxDrawingCoordinates_CANVAS
                            fromX:mousePositionX
                            fromY:mousePositionY
                          toSpace:kFxDrawingCoordinates_OBJECT
                              toX:&lastObjectPosition.x
                              toY:&lastObjectPosition.y];
    [lastPositionLock unlock];
    *forceUpdate = NO;
}

// ...
```

In this example, the code retrieves the mouse position when a user clicks the mouse, and assigns the coordinates to the instance variable `lastObjectPosition`. Because you lock the `NSLock` before doing that, no other thread calling this function can access `lastObjectPosition` until you unlock it. If other functions access the `lastObjectPosition` (for example, [`mouseDragged(atPositionX:positionY:activePart:modifiers:forceUpdate:at:)`](../professional_video_applications/fxonscreencontrol_v4/mousedragged%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md) and [`mouseUp(atPositionX:positionY:activePart:modifiers:forceUpdate:at:)`](../professional_video_applications/fxonscreencontrol_v4/mouseup%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)), they must implement the same calls that lock the same `NSLock`.

These guidelines apply to any function that your plug-in implements. You can call the methods in [`FxTileableEffect`](../professional_video_applications/fxtileableeffect.md), and most of the other plug-in-implemented protocols, from background threads, and often on multiple threads at the same time. This includes [`pluginState(_:at:quality:)`](../professional_video_applications/fxtileableeffect/pluginstate%28_,at,quality%29.md), [`parameterChanged(_:at:)`](../professional_video_applications/fxtileableeffect/parameterchanged%28_,at%29.md), [`renderDestinationImage(_:sourceImages:pluginState:at:)`](../professional_video_applications/fxtileableeffect/renderdestinationimage%28_,sourceimages,pluginstate,at%29.md), and others.

## See Also

### Plug-in fundamentals
- [Building an FxPlug plug-in from an Xcode template](./building-an-fxplug-plug-in-from-an-xcode-template.md)
  Create a plug-in in Xcode with the FxPlug template.
- [Building an FxPlug plug-in manually](./building-an-fxplug-plug-in-manually.md)
  Create your own plug-in in Xcode.
- [Using FxPlug APIs](./using-fxplug-apis.md)
  Use various FxPlug APIs to communicate with host apps like Motion or Final Cut Pro.
- [Editing property lists for FxPlug plug-ins](./editing-property-lists-for-fxplug-plug-ins.md)
  Modify the way hosts recognize and display your FxPlug plug-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/thread-safety-in-plug-ins)*