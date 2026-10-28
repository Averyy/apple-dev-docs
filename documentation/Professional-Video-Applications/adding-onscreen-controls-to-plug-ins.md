# Adding onscreen controls to plug-ins

**Framework**: Professional-Video-Applications  
**Role**: Article

Simplify user interaction by using onscreen controls for your FxPlug plug-in.

## Overview

While the Motion or Final Cut Pro inspector is a powerful way to adjust and animate plug-in parameters in your host application, many users prefer using onscreen controls (OSCs) to adjust their effects. These controls draw directly on the canvas, on top of the project’s footage and elements. By creating onscreen controls, you give your users a richer set of tools that let them directly manipulate your plug-in’s parameters—something that many users find more intuitive. For example, consider the onscreen control of the ring lens in the following illustration. It allows you to adjust the inside radius, outside radius, and position, all by dragging the visible rings in the canvas:

![An example of a plug-in with an onscreen control showing a large ring over an image, a circular position control in the center with an attached angle handle control.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3655263@2x.png)

### Create onscreen controls

Onscreen controls are written as a type of plug-in, just like filters and generators, and can be bundled in the same application bundle as the plug-in. To implement an onscreen control plug-in, create an NSObject subclass that implements the `FxOnScreenControl` protocol. Then, add the OSC’s uuid to your plug-in’s `Info.plist` file to link them.

Your plug-in uses the `FxOnScreenControl` protocol to draw controls and other UI elements on the screen. Plug-ins also use this protocol to handle mouse and keyboard events. The `FxOnScreenControl` protocol consists of methods for drawing onscreen controls as well as methods for handling input events from the user.

FxPlug 4.0 introduced [`FxOnScreenControlAPI_v4`](../professional_video_applications/fxonscreencontrolapi_v4.md), which has additional (optional) methods for handling mouse-moved events.

### Initialize communication

Your onscreen control may also need access to the API Manager, to retrieve or set parameter values with [`FxParameterRetrievalAPI_v6`](../professional_video_applications/fxparameterretrievalapi_v6.md), for example. The host app sends your onscreen control plug-in an [`init(apiManager:)`](../professional_video_applications/fxtileableeffect/init%28apimanager%29-6vvaz.md) message, which includes a pointer to the API Manager object. Your plug-in can save this pointer for use later to communicate with the effect plug-in for which it provides an onscreen control UI.

### Identify drawing spaces

The first thing an onscreen control plug-in needs to do is tell the host application which drawing space it plans to use: *canvas space*, *object space*, or *document space*. Your plug-in should return the corresponding drawing space constant from its [`drawingCoordinates()`](../professional_video_applications/fxonscreencontrol_v4/drawingcoordinates%28%29.md) method. This tells the host application which space your plug-in is using. It also informs the host application as to what space it should use to transform mouse positions when it calls your plug-in to handle events.

> 💡 **Tip**:  To provide the best user experience, have your plug-in draw in the canvas space. For example, when drawing in the canvas space, your plug-in can draw handles and other UI elements that are a consistent size and always face the user.

**Swift**:

```swift
func drawingCoordinates() -> FxDrawingCoordinates
{
    return FxDrawingCoordinates(kFxDrawingCoordinates_CANVAS)
}
```

**Objective-C**:

```objc
- (FxDrawingCoordinates)drawingCoordinates
{
    return kFxDrawingCoordinates_CANVAS;
}
```

The drawing space types are:

- *Canvas space*. The area of the host application where the user places their footage, interacts with it, and watches it play back. It can be larger or smaller than just the area that gets rendered when the user exports their project as a movie, and its size varies based on how the user arranges the windows and panes of the application. The user can zoom in the canvas to see more detail in their project, or zoom out to get a higher-level overview. Its pixels are addressed starting at (0,0) from the leftmost and bottommost pixels to whatever the width and height happen to be. This may make it seem somewhat daunting to work with, but as you’ll see, you almost always want to use this space for your drawing because it gives users the best experience.
- *Object space*. The space that your plug-in’s point parameters are already in. It’s the normalized space of the object your plug-in is applied to (or of the object itself in the case of a generator). Point parameters have values in the range 0 to 1 in both directions to represent the area of the object—(0,0) represents the lower-left corner of the object, and (1,1) represents the upper-right corner. As such, working with absolute pixel values is very cumbersome in object space. But working with points is very convenient because you can easily handle proxy resolution and pixel aspect ratio by simply multiplying the point’s coordinates by the width and height of the image.
- *Document space*. Centered at the scene’s origin and always in project pixels. If you have a 1920 x 1080 pixel project, document space initially stretches from (–960,– 540) to (960,540) along the x and y axes and is in the same coordinates as the scene. As you move the camera, the coordinates stay anchored in the scene, rather than on the object or the canvas.

![An image showing the three drawing space types. From the left is a canvas space, in the middle is the object space, and on the right side is the document space. Each space shows the x and y axis and coordinates.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3915367@2x.png)

### Draw onscreen controls

This method is called when it is time for the plug-in to draw the onscreen controls.

**Swift**:

```swift
func drawOSC(withWidth width: Int, height: Int, activePart: Int, destinationImage: FxImageTile, at time: CMTime)
```

**Objective-C**:

```objc
- (void)drawOSCWithWidth:(NSInteger)width
                  height:(NSInteger)height
              activePart:(NSInteger)activePart
        destinationImage:(FxImageTile*)destinationImage
                  atTime:(CMTime)time;
```

Draw control parts in object space so that they align with your effect, but draw their handles in canvas space so that they always remain the same size and always face the user, regardless of the canvas zoom settings. You can convert between spaces by using methods such as [`convertPoint(fromSpace:fromX:fromY:toSpace:toX:toY:)`](../professional_video_applications/fxonscreencontrolapi/convertpoint%28fromspace,fromx,fromy,tospace,tox,toy%29.md) in [`FxOnScreenControlAPI`](../professional_video_applications/fxonscreencontrolapi.md). Look at `FxShapeOSC.m` in the `FxShape` project to see some examples of how to convert coordinates from object space to canvas space and vice versa.

### Perform a hit test with onscreen controls

Interacting with an OSC requires knowing if a user has clicked within a drawn control. Consider this method:

**Swift**:

```swift
func hitTestOSC(atMousePositionX mousePositionX: Double, mousePositionY: Double, activePart: UnsafeMutablePointer<Int>?, at time: CMTime)
```

**Objective-C**:

```objc
- (void)hitTestOSCAtMousePositionX:(double)mousePositionX
                    mousePositionY:(double)mousePositionY
                        activePart:(NSInteger*)activePart
                            atTime:(CMTime)time;
```

Here, your plug-in’s OSC is given the mouse’s position and the time. Your plug-in should return an `activePart` parameter consisting of a constant that represents the part number for the onscreen control that was returned as hit. Other event-driven messages use this `activePart` identifier to keep the plug-in informed of how the user is interacting with your OSC. If a mouse click did not land on a point that has an OSC control, return zero.

The following is an example of how your plug-in might handle updating a control handle’s position on screen when the mouse is moved:

**Swift**:

```swift
func mouseMoved(atPositionX mousePositionX: Double, positionY mousePositionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>?, at time: CMTime)
    {  
    // Convert the mouse position into object relative
    // coordinates for drawing later
    let oscAPI = apiManager!.api(for: FxOnScreenControlAPI_v4.self) as! FxOnScreenControlAPI_v4

    // The _mouseMovedPos variable is a class member
    // that we’ll reference again in our
    // mouseDown handler and drawing routines
 
    oscAPI.convertPoint(fromSpace: UInt(kFxDrawingCoordinates_CANVAS), fromX: mousePositionX, fromY: mousePositionY, toSpace: UInt(kFxDrawingCoordinates_OBJECT), toX: &_mouseMovedPos.x, toY: &_mouseMovedPos.y)

    // Redraw the OSC so we see the change in position on the circle's handle

    forceUpdate?.pointee = true
}
```

**Objective-C**:

```objc
- (void)mouseMovedAtPositionX:(double)mousePositionX 
                    positionY:(double)mousePositionY
                   activePart:(int)activePart
                    modifiers:(FxModifierKeys)modifiers
                  forceUpdate:(BOOL *)forceUpdate
                       atTime:(CMTime)time
{
    // Convert the mouse position into object relative
    // coordinates for drawing later
    id<FxOnScreenControlAPI_v4> oscAPI = [_apiManager apiForProtocol:@protocol(FxOnScreenControlAPI_v4)]; 

    // The _mouseMovedPos variable is a class member
    // that we’ll reference again in our
    // mouseDown handler and drawing routines
 
    [oscAPI convertPointFromSpace:kFxDrawingCoordinates_CANVAS
                            fromX:mousePositionX
                            fromY:mousePositionY
                          toSpace:kFxDrawingCoordinates_OBJECT
                              toX:&_mouseMovedPos.x
                              toY:&_mouseMovedPos.y];

    // Redraw the OSC so we see the change in position on the circle's handle

    *forceUpdate = YES;
}
```

### Implement mouse and keyboard event handling

Users need to interact with your controls, so you must implement mouse and keyboard event handling. The host app passes mouse coordinates to your plug-in, in its specified drawing space. For example, if your plug-in returns [`kFxDrawingCoordinates_CANVAS`](../professional_video_applications/kfxdrawingcoordinates_canvas.md) for its [`drawingCoordinates()`](../professional_video_applications/fxonscreencontrol_v4/drawingcoordinates%28%29.md) method, then your mouse event handlers will receive mouse coordinates in the canvas drawing space.

Your plug-in receives a call to these methods in response to actions that a user initiates with a mouse:

- **[`mouseDown(atPositionX:positionY:activePart:modifiers:forceUpdate:at:)`](../professional_video_applications/fxonscreencontrol_v4/mousedown%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)**: The user clicked on one of your controls.
- **[`mouseDragged(atPositionX:positionY:activePart:modifiers:forceUpdate:at:)`](../professional_video_applications/fxonscreencontrol_v4/mousedragged%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)**: The user dragged the mouse.
- **[`mouseUp(atPositionX:positionY:activePart:modifiers:forceUpdate:at:)`](../professional_video_applications/fxonscreencontrol_v4/mouseup%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)**: The user released the mouse.

In each of these methods, return `YES` for the `forceUpdate` parameter if you need the host app to redraw your controls (which you almost always will).

Generally, as the mouse is dragged, you’ll be updating your plug-in’s parameters, as follows:

1. Get the current value of the parameters.
2. Calculate the new value, based on where the mouse was dragged to.
3. Set the new value of the parameters based on the change in mouse position.

Here’s a longer example of how an OSC might update a point parameter as its lower-left corner handle is dragged:

**Swift**:

```swift
func mouseDragged(atPositionX mousePositionX: Double, positionY mousePositionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>?, at time: CMTime)
{
    let oscAPI = apiManager!.api(for: FxOnScreenControlAPI_v4.self) as! FxOnScreenControlAPI_v4
    let paramSetAPI = apiManager!.api(for: FxParameterSettingAPI_v5.self) as! FxParameterSettingAPI_v5
    let paramGetAPI = apiManager!.api(for: FxParameterRetrievalAPI_v6.self) as! FxParameterRetrievalAPI_v6

    var objectPos = (x:0.0, y:0.0)

    oscAPI.convertPoint(fromSpace: UInt(kFxDrawingCoordinates_CANVAS), fromX: mousePositionX, fromY: mousePositionY, toSpace: UInt(kFxDrawingCoordinates_OBJECT), toX: &objectPos.x, toY: &objectPos.y)

    let delta = (x: objectPos.x - lastObjectPosition.x, y: objectPos.y - lastObjectPosition.y)
    lastObjectPosition = objectPos


    if activePart == 1 /* kFSPart_Rectangle */
    {
        var ll = (x: 0.0, y: 0.0)
        var ur = (x: 0.0, y: 0.0)
        paramGetAPI.getXValue(&ll.x, yValue: &ll.y, fromParameter: UInt32(kLowerLeftID), at: time)
        paramGetAPI.getXValue(&ur.x, yValue: &ur.y, fromParameter: UInt32(kUpperRightID), at: time)

        ll.x += delta.x
        ll.y += delta.y
        ur.x += delta.x
        ur.y += delta.y

        paramSetAPI.setXValue(ll.x, yValue: ll.y, toParameter: UInt32(kLowerLeftID), at: time)
        paramSetAPI.setXValue(ur.x, yValue: ur.y, toParameter: UInt32(kUpperRightID), at: time)
    }
    else if activePart == 2 /* kFSPart_Circle */
    {
        var cc = (x: 0.0, y: 0.0)
        paramGetAPI.getXValue(&cc.x, yValue: &cc.y, fromParameter: UInt32(kCircleCenter), at: time)

        cc.x += delta.x
        cc.y += delta.y

        paramSetAPI.setXValue(cc.x, yValue: cc.y, toParameter: UInt32(kCircleCenter), at: time)
    }

    forceUpdate?.pointee = true
}
```

**Objective-C**:

```objc
- (void)mouseDraggedAtPositionX:(double)mousePositionX
                      positionY:(double)mousePositionY
                     activePart:(NSInteger)activePart
                      modifiers:(FxModifierKeys)modifiers
                    forceUpdate:(BOOL *)forceUpdate
                         atTime:(CMTime)time
{
    id<FxOnScreenControlAPI_v4> oscAPI = [_apiManager apiForProtocol:@protocol(FxOnScreenControlAPI_v4)]; 
    id<FxParameterSettingAPI_v5> paramSetAPI = [_apiManager apiForProtocol:@protocol(FxParameterSettingAPI_v5)]; 
    id<FxParameterRetrievalAPI_v6> paramGetAPI = [_apiManager apiForProtocol:@protocol(FxParameterRetrievalAPI_v6)];
    if ((oscAPI == nil) or (paramGetAPI == nil) or (paramSetAPI == nil))
    {
        NSLog (@"Unable to obtain the OSC or parameter APIs in %s:%d", __func__, __LINE__);
        return;
    }

    // Get some info about the object
    unsigned int    objWidth;
    unsigned int    objHeight;
    double          objPixelAspectRatio;

    [oscAPI objectWidth:&objWidth
                 height:&objHeight
       pixelAspectRatio:&objPixelAspectRatio];
 
    // Get the point parameter's values
    FxPoint2D   lowerLeft;
    FxPoint2D   upperRight;
    FxPoint2D   mousePosObjSpace;
    [paramGetAPI getXValue:&lowerLeft.x
                    YValue:&lowerLeft.y
             fromParameter:kShape_LowerLeft
                    atTime:time];

    [paramGetAPI getXValue:&upperRight.x
                    YValue:&upperRight.y
             fromParameter:kShape_UpperRight
                    atTime:time];
    // Get the mouse position in object relative space
    [oscAPI convertPointFromSpace:kFxDrawingCoordinates_CANVAS
                            fromX:mousePositionX
                            fromY:mousePositionY
                          toSpace:kFxDrawingCoordinates_OBJECT
                              toX:&mousePosObjSpace.x
                              toY:&mousePosObjSpace.y];

    // Find the change from the last time
    FxPoint2D   delta   = {
        mousePosObjSpace.x - _mouseDownPos.x,
        mousePosObjSpace.y - _mouseDownPos.y
    }; 

    // Save the current location for the next time around
    _mouseDownPos = mousePosObjSpace;
    _mouseMovedPos = mousePosObjSpace;

    // Tell the app to update
    *forceUpdate = YES;

    // Now respond to the part that the user clicked in
    FxPoint2D   newLowerLeft;
    switch (activePart)
    {
        ...
        case kShapeOSC_LowerLeft:
        newLowerLeft.x = mousePosObjSpace.x;
        newLowerLeft.y = mousePosObjSpace.y;
        newUpperRight = upperRight;
        break; 
        ... 
    }
    // Set the new values
    // ... 
    [paramSetAPI setXValue:newLowerLeft.x
                    YValue:newLowerLeft.y
               toParameter:kShape_LowerLeft
                    atTime:time];
    // ...
}
```

In addition to mouse events, you will also receive keyboard events:

- **[`keyDown(atPositionX:positionY:keyPressed:modifiers:forceUpdate:didHandle:at:)`](../professional_video_applications/fxonscreencontrol_v4/keydown%28atpositionx,positiony,keypressed,modifiers,forceupdate,didhandle,at%29.md)**: Provides information when a key is pressed.
- **[`keyUp(atPositionX:positionY:keyPressed:modifiers:forceUpdate:didHandle:at:)`](../professional_video_applications/fxonscreencontrol_v4/keyup%28atpositionx,positiony,keypressed,modifiers,forceupdate,didhandle,at%29.md)**: Provides information when a key is released.

The mouse and key methods mentioned so far are required to be implemented in your OSC. If you don’t need a particular method, leave the implementation empty and return `NO` for the `*didHandle` parameter.

There are also some mouse messages you can optionally receive; to do so, implement any of these:

- **[`mouseMoved(atPositionX:positionY:activePart:modifiers:forceUpdate:at:)`](../professional_video_applications/fxonscreencontrol_v4/mousemoved%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)**: Provides information when the mouse pointer changes location.
- **[`mouseEntered(atPositionX:positionY:modifiers:forceUpdate:at:)`](../professional_video_applications/fxonscreencontrol_v4/mouseentered%28atpositionx,positiony,modifiers,forceupdate,at%29.md)**: Provides information when the mouse pointer enters the view.
- **[`mouseExited(atPositionX:positionY:modifiers:forceUpdate:at:)`](../professional_video_applications/fxonscreencontrol_v4/mouseexited%28atpositionx,positiony,modifiers,forceupdate,at%29.md)**: Provides information when the mouse pointer leaves the view.

### Add onscreen controls to the Info.plist file

The `ProPlugPlugInList` array in the plug-in’s `Info.plist` file requires a separate entry for your onscreen control’s class, with its own UUID.

## Topics

### Onscreen Control APIs
- [protocol FxOnScreenControl_v4](../professional_video_applications/fxonscreencontrol_v4.md)
  Defines the methods a plug-in must implement to create parameter controls.
- [protocol FxOnScreenControlAPI](../professional_video_applications/fxonscreencontrolapi.md)
  The `FxOnScreenControlAPI` protocol defines the methods the host application uses to draw controls and other user interface elements directly on the canvas where the user has applied the plug-in.
- [protocol FxOnScreenControlAPI_v2](../professional_video_applications/fxonscreencontrolapi_v2.md)
  The `FxOnScreenControlAPI_v2` protocol specifies additions to the `FxOnScreenControlAPI` protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.
- [protocol FxOnScreenControlAPI_v3](../professional_video_applications/fxonscreencontrolapi_v3.md)
  The `FxOnScreenControlAPI_v3` protocol specifies additions to the [`FxOnScreenControlAPI`](../professional_video_applications/fxonscreencontrolapi.md) protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.
- [protocol FxOnScreenControlAPI_v4](../professional_video_applications/fxonscreencontrolapi_v4.md)
  The `FxOnScreenControlAPI_v4` protocol specifies additions to the [`FxOnScreenControlAPI`](../professional_video_applications/fxonscreencontrolapi.md) protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.
### Constants
- [typealias FxModifierKeys](../professional_video_applications/fxmodifierkeys.md)
  Specifies flags that identify modifier keys held down while an event is generated.
- [typealias FxDrawingCoordinates](../professional_video_applications/fxdrawingcoordinates.md)
  Constants used to identify coordinate spaces.

## See Also

### User interface
- [Adding parameters to plug-ins](./adding-parameters-to-plug-ins.md)
  Create standard and custom user-facing parameters for your plug-in that will appear in the inspector.
- [protocol FxPathAPI_v3](../professional_video_applications/fxpathapi_v3.md)
  An API that defines the methods to retrieve information about paths, shapes, and masks the user has drawn on an object.
- [protocol FxUndoAPI](../professional_video_applications/fxundoapi.md)
  An API that defines the methods that the host app implements to handle plug-in management of the host app’s undo queue.
- [protocol FxCommandAPI](../professional_video_applications/fxcommandapi.md)
  Commands that you can tell the host to perform.
- [protocol FxCommandAPI_v2](../professional_video_applications/fxcommandapi_v2.md)
  Adds functionality to move the playhead to a specific timeline time.
- [protocol FxRemoteWindowAPI](../professional_video_applications/fxremotewindowapi.md)
  A protocol that allows the plug-in to request that the host create a window.
- [protocol FxRemoteWindowAPI_v2](../professional_video_applications/fxremotewindowapi_v2.md)
  A protocol that allows the plug-in to request that the host create a window with a defined minimum and maximum size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/adding-onscreen-controls-to-plug-ins)*