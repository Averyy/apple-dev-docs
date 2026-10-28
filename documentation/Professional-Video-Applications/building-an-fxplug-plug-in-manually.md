# Building an FxPlug plug-in manually

**Framework**: Professional-Video-Applications  
**Role**: Article

Create your own plug-in in Xcode.

## Overview

Every FxPlug plug-in is contained within an application bundle, and uses an XPC service to communicate with the host applications, Final Cut Pro and Motion. In most cases, you can use the Xcode template that’s installed with the FxPlug SDK as a base your FxPlug plug-in (see [Building an FxPlug plug-in from an Xcode template](./building-an-fxplug-plug-in-from-an-xcode-template.md)). However, if you’re creating an especially complex plug-in (or if you’re the type who likes to know behind-the- scenes details), then this article is for you.

You can create your own FxPlug plug-in that’s discoverable by Motion and ready to be developed for your specific rendering goals. Begin by creating your plug-in’s structure, making the plug-in discoverable, and building and running your project to check for errors. Next, create your plug-in class, cache the host API manager, and define a properties dictionary. You then implement required methods to specify how the plug-in will render and to establish the plug-in state.

> **Note**:  This document describes how to create a plug-in with FxPlug 4. FxPlug 3 isn’t supported in Final Cut Pro and Motion. For more information, see [Migrating FxPlug 3 plug-ins to FxPlug 4](./migrating-fxplug-3-plug-ins-to-fxplug-4.md).

### Build the structure for your plug-in

To build the structure for your plug-in, follow these steps:

1. **Create an empty app.** Launch Xcode and create a new project. Select macOS to display the appropriate macOS templates. Then, select the App template, and click Next. Enter `FxPlugBrightness` as the Product Name for your app. For this example, choose Objective-C or Swift as the language, and select XIB for User Interface. Deselect Include Tests. Click Next. Specify a location for your project, and then click Create.

![A screenshot showing the create options for a new plug-in. The image shows the Product Name, Organization Identifier, Language, and User Interface fields.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3559538@2x.png)

> **Note**:  The plug-in application bundle can also present a UI made with Storyboards or SwiftUI.

1. **In the Xcode Editor toolbar, click the “Build and run” button.** Once the build successfully completes, a typical macOS application launches and displays an empty default window. (If you select the window, you see the name of your app, FxPlugBrightness, in the menu bar). Quit the app.
2. **Add an XPC service inside your new app.** In Xcode, click the “Show projects and targets list” button to toggle a list of your app’s project and build targets in the sidebar. In the Targets pane, select your app (if it’s not already selected). Click the plus sign (+) at the bottom of the pane, select XPC Service from the Framework & Library section, and click Next. Give your XPC service a name, such as “FxBrightnessXPC”. This is the name used to report any problems your host application has in the discovery process, so be sure to make note of it. Make sure the name of your app is displayed in the Embed in Application option, and then click Finish.
3. **Add the FxPlug and PluginManager frameworks.** In the Xcode Project and Targets sidebar pane, select the XPC service target you just added. Select General from the project menu bar, locate the Frameworks and Libraries section, and click the plus sign at the bottom of that section. Select `FxPlug.framework` from the list of frameworks and click add. Repeat for the `PluginManager.framework`. You may need to click “Add Other,” and locate the frameworks, which are installed in `/Library/Developer/Frameworks`.

![A screenshot of an FxPlug project in Xcode with the Show/Hide projects and Targets section, General tab, and linked Frameworks and Libraries sections labeled. The FxBrightnessXPC target is selected.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3559534@2x.png)

1. **Add a Copy Files phase.** Choose Build Phases from the Project menu bar and click the plus sign in the upper-left corner of that pane. Choose New Copy Files Phase from the menu and then expand the new section. Click the plus sign at the bottom of the new Copy Files section, select `FxPlug.framework`, and click Add. Repeat for the `PluginManager.framework`. See [Code sign embedded frameworks](./notarizing-your-fxplug-plug-in.md#Code-sign-embedded-frameworks) for information on scripting the copy and code sign phase for `PluginManager.framework`.

![A screenshot showing the Build Phases in the menu bar selected. The Copy Files phase with FxPlug.framework are selected and added to the project.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3559531@2x.png)

1. **Add a framework search path.** In the Targets pane, select your XPC service target and choose Build Settings from the project menu bar. Select All to make sure you’re seeing all available settings. In the Build Settings pane, search for Framework Search Paths. Expand the Framework Search Paths item, click the plus sign, and enter the path to where the FxPlug SDK is installed: `/Library/Frameworks $(inherited)`. Do this for both debug and release.

![A screenshot showing the Framework Search paths in the Build Setting pane. The screenshot shows the path to where the FxPlug SDK is installed.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3559530@2x.png)

1. **Add Additional SDKs path.** With your XPC service target still selected in the Targets pane, search for “Additional SDKs” and add the path `/Library/Developer/SDKs/FxPlug.sdk` as shown below. Do this for both debug and release.

![A screenshot showing the XPC Service target selected in the Targets pane. The Additional SDKs path shows the location of the FxPlug.sdk file.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3559532@2x.png)

### Make your plug-in discoverable

macOS uses a technology called PlugInKit to discover and register plug-ins on your system. When a host application launches, PluginKit reports a list of plug-ins that are available for that host. To make your plug-in discoverable by PluginKit, make `pluginkit` your Wrapper Extension. In the Targets list, select your XPC service, select Build Settings from the Project menu bar, and select All to make sure you’re seeing all available settings. It’s helpful to search for “packaging” to find the correct section.

Next, enter `pluginkit` in place of the default Wrapper Extension.

![A screenshot showing the XPC service selected in the Targets pane. The Build Settings pane on the right side shows the Wrapper Extension with the pluginkit selected.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3665056@2x.png)

Tell Xcode where to embed the plug-in bundle in your application bundle:

1. Select your wrapper app from the Targets list.
2. From the Project menu bar, select Build Phases. If you don’t already have a Copy Files phase item, first add one by clicking the Add A New Build Phase (+) button and then selecting New Copy Files Phase.
3. Find and expand the Copy Files phase item and then click the Add Items (+) button and at the Destination option, choose your XPC service. For example, the FxBrightnessXPC service would look like this, embedded.

![A screenshot showing the wrapper app selected in the Targets list. The Build Phase pane shows the Copy Files section with the Plugin destination location listed.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3665055@2x.png)

1. Configure your plug-in to be recognized as an FxPlug plug-in by modifying the `Info.plist` file for your XPC service. For a complete list of configuration requirements, see [Editing property lists for FxPlug plug-ins](./editing-property-lists-for-fxplug-plug-ins.md).

![Screenshot of DynamicRegXPC.pluginkit added to Embed PlugIns with Code Sign On Copy selected.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3375356@2x.png)

### Connect the host application to the plug-in

The host application must make an XPC connection to your plug-in. To do that, your plug-in’s XPC must call the `FxPrincipal` starting method in its `main.swift` file. Be sure to import the `FxPlug/FxPlugSDK.h` header file. In Objective-C, import it in your `main.m` file. In Swift, import it in your `XPC Service-Bridging-Header.h` file.

**Swift**:

```swift
#import <FxPlug/FxPlugSDK.h>
```

**Objective-C**:

```objc
#import <FxPlug/FxPlugSDK.h>
int main(int argc, const char *argv[])

{ 
    [FxPrincipal startServicePrincipal];
}
```

When using Swift, also add the following code to your `main.swift` file:

```swift
FxPrincipal.startServicePrincipal()
```

### Build and run your project

Once you finish editing your `Info.plist`, build and run your project. It should compile without errors and launch without complications. When you launch Motion, you see your plug-in either in the filter list or in the generator list (depending on whether your entry in `protocolNames` was `FxFilter` or `FxGenerator` as you indicated when [Editing property lists for FxPlug plug-ins](./editing-property-lists-for-fxplug-plug-ins.md)).

Confirm that your plug-in was discovered by querying `PlugInKit`. In Terminal, type the following:

```
pluginkit -m -p FxPlug
```

Terminal displays a list of every FxPlug plug-in on your system. If this list is very long, you can search the Terminal output for the specific name of your plug-in, like this:

```
pluginkit -m -p FxPlug | grep “FxPlugBrightness”
```

Terminal now displays `FxPlugBrightness(1.0)`. If you want more information about your discovered plug-in, add the verbose option like this:

```
pluginkit -mv -p FxPlug | grep “FxPlugBrightness”
```

Terminal now displays the following:

```
FxPlugBrightness(1.0)DE175335-4588-4C40-84D6-BCD4F0BCAC44 2019-07-09 15:41:18 +0000 /Users/your_username/Desktop/FxPlugBrightness/Build/Products/Debug/ FxPlugBrightness.app/Contents/PlugIns/FxPlugBrightness.pluginkit
```

> **Note**: Even though your plug-in has been discovered, it’s still not ready to use. If you use the plug-in in the library, you get unexpected results.

### Create your plug-in class

When a host application instantiates your plug-in, it looks for the `className` item in the `Info.plist` file for your XPC service. This class is where you write your plug-in code — making sure that it conforms to the [`FxTileableEffect`](../professional_video_applications/fxtileableeffect.md) protocol. (See [Rendering in FxPlug](./rendering-in-fxplug.md) for more information).

1. Select File > New > File and add a class to your project.
2. Set the name of the class to the `className` you entered in your `Info.plist` file. For example, call it `FxPlugBrightnessFilter`.
3. Set the Target Membership of the new class to the XPC service.
4. Open the source file that defines your class. In Objective-C, open the header file. In Swift, open the `.swift` source file.
5. In Objective-C, import `FxPlugSDK.h` at the top of your header file.
6. Make your class conform to the [`FxTileableEffect`](../professional_video_applications/fxtileableeffect.md) protocol, as shown in the following example.

**Swift**:

```swift
@objc(FxBrightnessFilter) class FxBrightnessFilter : NSObject, FxTileableEffect {
```

**Objective-C**:

```objc
#import <Foundation/Foundation.h>
#import <FxPlug/FxPlugSDK.h>

@interface FxPlugBrightnessFilter : NSObject <FxTileableEffect>
@end
```

### Cache the host API manager

Before you can add methods for the [`FxTileableEffect`](../professional_video_applications/fxtileableeffect.md) protocol, use the following code to cache the host API manager. For more on the role of the host API, see [Using FxPlug APIs](./using-fxplug-apis.md).

Declare the API Manager and initializer in your source file. For example, add this code to the `FxPlugBrightnessFilter.swift` file in Swift, or to the `FxPlugBrightnessFilter` header file in Objective-C.

**Swift**:

```swift
    let _apiManager : PROAPIAccessing!
    
    required init?(apiManager: PROAPIAccessing) {
        _apiManager = apiManager
    }
```

**Objective-C**:

```objc
@property (assign) id<PROAPIAccessing> apiManager; 
```

In Objective-C, add the code for the initializer to the `FxPlugBrightnessFilter` implementation `.m` file:

```objc
- (nullable instancetype)initWithAPIManager:
(id<PROAPIAccessing>)newApiManager;
{ 
    self=[super init];
    if (self !=nil)
    { 
        _apiManager = newApiManager;
    } 
    return self;
}
```

### Define a properties dictionary

Every plug-in defines a properties dictionary that holds configuration values unique to how that plug-in operates, including keys that specify if the plug-in can change its output size and if it supports tiled rendering. To define a properties dictionary for your plug-in, implement this method:

**Swift**:

```swift
func properties(_ properties: AutoreleasingUnsafeMutablePointer<NSDictionary>?) throws {
        let swiftProps = [
            kFxPropertyKey_MayRemapTime : NSNumber(booleanLiteral: false),
            kFxPropertyKey_PixelTransformSupport : NSNumber(value: kFxPixelTransform_Full),
            kFxPropertyKey_VariesWhenParamsAreStatic: NSNumber(booleanLiteral: false),
            kFxPropertyKey_ChangesOutputSize : NSNumber(booleanLiteral: false)
        ]
        let props = NSDictionary(dictionary: swiftProps)
        properties?.pointee = props
    }
```

**Objective-C**:

```objc
- (BOOL)properties:(NSDictionary * _Nonnull *)properties
             error:(NSError * _Nullable *)error
{
    *properties = @{
                    kFxPropertyKey_ChangesOutputSize : @NO,
                    kFxPropertyKey_NeedsFullBuffer : @NO,
                    kFxPropertyKey_VariesWhenParamsAreStatic : @NO
                    };
    return YES;
}
```

For information on other available key values, see `FxBaseEffect` `and` [`FxTileableEffect`](../professional_video_applications/fxtileableeffect.md). There are many options, such as:

- **[`kFxPropertyKey_NeedsFullBuffer`](../professional_video_applications/kfxpropertykey_needsfullbuffer.md)**: Indicates if this plug-in needs the entire image to do its processing, and can’t tile its rendering.
- **[`kFxPropertyKey_MayRemapTime`](../professional_video_applications/kfxpropertykey_mayremaptime.md)**: Indicates that your plug-in samples input from times other than the current time.
- **[`kFxPropertyKey_VariesWhenParamsAreStatic`](../professional_video_applications/kfxpropertykey_varieswhenparamsarestatic.md)**: Indicates whether this effect changes its rendering even when the parameters don’t change.

> **Note**: The property keys `kFxPropertyKey_IsThreadSafe` and `kFxPropertyKey_UsesRationalTime` are ignored for FxPlug 4 and newer plug-ins because all FxPlug 4 plug-ins are required to be thread-safe and use [`CMTime`](../CoreMedia/cmtime.md).

### Implement required and optional methods

Plug-ins generally require user interface elements such as parameter sliders, image wells, and color pickers. Add the [`addParameters()`](../professional_video_applications/fxtileableeffect/addparameters%28%29.md) method to your plug-in. For more information about parameter types, and examples of their usage, see [Using FxPlug APIs](./using-fxplug-apis.md) and [Adding parameters to plug-ins](./adding-parameters-to-plug-ins.md).

**Swift**:

```swift
func addParameters()
```

**Objective-C**:

```objc
- (BOOL)addParametersWithError:(NSError**)error;
```

You may choose to have your plug-in handle any changes in parameters made by your users (and relayed through the plug-in’s UI elements) with the [`parameterChanged(_:at:)`](../professional_video_applications/fxtileableeffect/parameterchanged%28_,at%29.md) method. Implement this optional method in your plug-in:

**Swift**:

```swift
func parameterChanged(_ paramID: UInt32, at time: CMTime)
```

**Objective-C**:

```objc
- (BOOL)parameterChanged:(UInt32)paramID
                  atTime:(CMTime)time
                   error:(NSError * _Nullable *)error;
```

The remaining methods required for your plug-in specify how your plug-in renders its effects:

**Swift**:

```swift
func renderDestinationImage(_ destinationImage: FxImageTile, sourceImages: [FxImageTile], pluginState: Data?, at renderTime: CMTime)
```

**Objective-C**:

```objc
- (BOOL)renderDestinationImage:(FxImageTile*)destinationImage
                  sourceImages:(NSArray<FxImageTile*>*)sourceImages
                   pluginState:(nullable NSData*)pluginState
                        atTime:(CMTime)renderTime
                         error:(NSError**)outError;
```

You will also need to implement two methods to set your source and destination rectangles:

**Swift**:

```swift
func sourceTileRect(_ sourceTileRect: UnsafeMutablePointer<FxRect>, sourceImageIndex: UInt, sourceImages: [FxImageTile], destinationTileRect: FxRect, destinationImage: FxImageTile, pluginState: Data?, at renderTime: CMTime)

func destinationImageRect(_ destinationImageRect: UnsafeMutablePointer<FxRect>, sourceImages: [FxImageTile], destinationImage: FxImageTile, pluginState: Data?, at renderTime: CMTime)
```

**Objective-C**:

```objc
- (BOOL)sourceTileRect:(nonnull FxRect*)sourceTileRect
      sourceImageIndex:(NSUInteger)sourceImageIndex
          sourceImages:(NSArray<FxImageTile*>*)sourceImages
   destinationTileRect:(FxRect)destinationTileRect
      destinationImage:(FxImageTile*)destinationImage
           pluginState:(nullable NSData*)pluginState
                atTime:(CMTime)renderTime
                 error:(NSError**)outError;


- (BOOL)destinationImageRect:(FxRect*)destinationImageRect
                sourceImages:(NSArray<FxImageTile*>*)sourceImages
            destinationImage:(FxImageTile*)destinationImage
                 pluginState:(nullable NSData*)pluginState
                      atTime:(CMTime)renderTime
                       error:(NSError**)outError;
```

Finally, your plug-in must prepare a “plug-in state” object when requested by the host app. To do this, implement the following method in your plug-in:

**Swift**:

```swift
func pluginState(_ pluginState: AutoreleasingUnsafeMutablePointer<NSData>?, at renderTime: CMTime, quality qualityLevel: UInt)
```

**Objective-C**:

```objc
- (BOOL)pluginState:(NSData* _Nonnull * _Nullable)pluginState
             atTime:(CMTime)renderTime
            quality:(FxQuality)qualityLevel
              error:(NSError**)error;
```

For more information on rendering, [`FxImageTile`](../professional_video_applications/fximagetile.md), or source and destination rectangles, see [Rendering in FxPlug](./rendering-in-fxplug.md) and [Working with tiled images](./working-with-tiled-images.md). For more information on plug-in state, see [Communicating with the plug-in state](./communicating-with-the-plug-in-state.md). For more information on timing in FxPlug, see [Scheduling media in plug-ins](./scheduling-media-in-plug-ins.md).

## See Also

### Plug-in fundamentals
- [Building an FxPlug plug-in from an Xcode template](./building-an-fxplug-plug-in-from-an-xcode-template.md)
  Create a plug-in in Xcode with the FxPlug template.
- [Using FxPlug APIs](./using-fxplug-apis.md)
  Use various FxPlug APIs to communicate with host apps like Motion or Final Cut Pro.
- [Editing property lists for FxPlug plug-ins](./editing-property-lists-for-fxplug-plug-ins.md)
  Modify the way hosts recognize and display your FxPlug plug-in.
- [Thread safety in plug-ins](./thread-safety-in-plug-ins.md)
  Learn about reentrancy for plug-ins and best practices to make them thread safe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/building-an-fxplug-plug-in-manually)*