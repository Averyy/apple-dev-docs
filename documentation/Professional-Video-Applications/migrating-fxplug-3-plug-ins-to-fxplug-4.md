# Migrating FxPlug 3 plug-ins to FxPlug 4

**Framework**: Professional-Video-Applications  
**Role**: Article

Update existing FxPlug 3 plug-ins to out-of-process FxPlug 4 plug-ins.

#### Overview

FxPlug 4 plug-ins run *out-of-process*, which means they run in a dedicated process outside the host app. Communication between the host and the plug-in occurs through an interprocess communication service (XPC) using IOSurface objects, which are suitable for sharing textures across process boundaries. Out-of-process plug-ins developed with FxPlug 4 have a slightly different structure than plug-ins developed with earlier versions of FxPlug. (See [Using out-of-process FxPlug plug-ins](./using-out-of-process-fxplug-plug-ins.md)).

In FxPlug 3, a plug-in was embedded within an XPC service, which was then embedded in a plug-in’s application wrapper. FxPlug 4 plug-ins remove the innermost layer, moving the actual plug-in code into the XPC service. Thus, you now have just two targets: a wrapper application and an XPC service.

If you developed plug-ins with FxPlug 3, you need to upgrade them to FxPlug 4 for compatibility with current versions of Final Cut Pro and Motion. Use the following process to update each plug-in.

##### Add additional search paths to support a sparse SDK

FxPlug 4.1 adopts a sparse SDK, which reduces the bundle size of your built plug-in. After installing FxPlug 4.1 and opening an Xcode project of an older plug-in, you may see the `’FxPlug/FxPlugSDK.h’ file not found` error. This error shouldn’t occur after you complete these steps.

1. In Xcode’s Project Navigator (Shift-Command-1), select your project.
2. Select the Builds Settings tab.
3. Select the All tab.
4. Search for “Additional SDK” in the build settings search field.
5. Modify Additional SDKs (`ADDITIONAL_SDKS`) to include `/Library/Developer/SDKs/FxPlug.sdk` in the Build Settings of the Xcode project.
6. Search for “Framework Search” in the build settings search field.
7. Modify Framework Search Paths (`FRAMEWORK_SEARCH_PATHS`) to include `/Library/Frameworks $(inherited)` in the Build Settings of the Xcode project.
8. Clean (Shift-Command-K) the project and then build (Command-R) again.

##### Set up build targets

FxPlug 3 plug-in code was embedded within an XPC service, which was then embedded in the plug-in’s application wrapper. In version 4, FxPlug moves the plug-in code into the XPC service, thereby removing the innermost layer. As a result, you now have just two targets, a wrapper application and an XPC service, whereas previously there were three targets.

To migrate your plug-ins to the new structure, in the `main.m` file of the XPC service, include the `FxPlug/FxPlugSDK` header and include this line in `main.m`:

**Swift**:

```swift
FxPrincipal.startServicePrincipal()
```

**Objective-C**:

```objc
[FxPrincipal startServicePrincipal];
```

Change the filter code to include it in the XPC service build target. Then remove the XPC protocol and otherwise refactor your filter code to live within the XPC service as a stand-alone class. To see an example of this, look at how `FxGradientCheckerboard.mm` is structured in the FxGradientCheckerboard example plug-in.

##### Make your plug-in conform to the FxTileableEffect protocol

In earlier versions of FxPlug, effects had to conform to either the `FxFilter` or `FxGenerator` protocols. In FxPlug 4, your plug-in must conform to the [`FxTileableEffect`](../professional_video_applications/fxtileableeffect.md) protocol instead. Host applications now render effects in tiles, which is usually more efficient. Tileable rendering is the same technique that Apple’s own plug-ins use to render.

Your actual plug-in code exists in an `NSObject` that conforms to the `FxTileableEffect` protocol, and your plug-in must implement this new protocol as indicated in the `FxTileableEffect` header file.

The rendering process differs between the earlier and current versions of FxPlug. In earlier versions of FxPlug, rendering occurred when the `renderOutput:withInput:withInfo:` method was called by the host application:

```objc
// FxPlug 3
- (BOOL)renderOutput:(FxImage *)outputImage
           withInput:(FxImage *)inputImage
            withInfo:(FxRenderInfo)renderInfo
```

Now, rendering occurs when the [`renderDestinationImage(_:sourceImages:pluginState:at:)`](../professional_video_applications/fxtileableeffect/renderdestinationimage%28_,sourceimages,pluginstate,at%29.md) method is called by the host application:

**Swift**:

```swift
// FxPlug 4
func renderDestinationImage(_ destinationImage: FxImageTile, sourceImages: [FxImageTile], pluginState: Data?, at renderTime: CMTime)
```

**Objective-C**:

```objc
// FxPlug 4
- (BOOL)renderDestinationImage:(FxImageTile *)destinationImage
                  sourceImages:(NSArray<FxImageTile *> *)sourceImages
                   pluginState:(NSData *)pluginState
                        atTime:(CMTime)renderTime
                         error:(NSError * _Nullable *)outError
```

> ❗ **Important**:  All FxPlug APIs now represent time using `CMTime` rather than `FxTime`. See [`CMTime`](../CoreMedia/cmtime.md).

##### Make changes to the information property lists for your plug-ins

Revise plug-in information property lists (`Info.plist`) to reflect some notable changes:

1. Migrate the `.fxplug` target’s `Info.plist` values over to the XPC service’s `Info.plist` file. (See [Editing property lists for FxPlug plug-ins](./editing-property-lists-for-fxplug-plug-ins.md) for a complete list of what to add).
2. Add the new keys to the XPC’s `Info.plist`: `RunLoopType`, `JoinExistingSession`, and a Dictionary named `_AdditionalSubServices`. (See [Add XPCService entry](./editing-property-lists-for-fxplug-plug-ins.md#Add-XPCService-entry) for more information about these keys).
3. In the XPC’s `Info.plist` file, under the “`PluginKit`” section, revise the Protocol key to use a value of `PROXPCProtocol` instead of `FxXPCProtocol`.

If your plug-in used dynamic registration, then it previously had an in-process component. This is no longer the case in FxPlug 4.1, so you need to make the following changes:

1. Migrate the registrar code that was in your in-process bundle to the XPC bundle.
2. Remove the in-process bundle from your plug-in.
3. Delete the `EmbeddedCode` and `EmbeddedProtocol` keys from the XPC’s `Info.plist`.
4. Migrate the `ProPlugDictionaryVersion`, and `ProPlugDynamicRegistration` keys over to the XPC’s `Info.plist` file.
5. Add a new key, `ProPlugDynamicRegistrationPrincipalClass`, to the XPC’s `Info.plist` and make the value the name of your registrar class. See [Add ProPlugDynamicRegistration and ProPlugDynamicRegistrationPrincipalClass keys](./editing-property-lists-for-fxplug-plug-ins.md#Add-ProPlugDynamicRegistration-and-ProPlugDynamicRegistrationPrincipalClass-keys) for more information.

##### Remove deprecated methods from FxTemporalImageAPI

All versions of `FxTemporalImageAPI` are deprecated in FxPlug 4.1 and aren’t accessible in an FxPlug 4-based plug-in, so remove deprecated methods from the `FxTemporalImageAPI` such as `getInputTexture:withInfo:atFxTime:`.

When you implement the [`scheduleInputs(_:withPluginState:at:)`](../professional_video_applications/fxtileableeffect/scheduleinputs%28_,withpluginstate,at%29.md) scheduling method of  [`FxTileableEffect`](../professional_video_applications/fxtileableeffect.md), that information is used to determine which frames are required for your plug-in to render. Those frames are automatically added to the `sourceImages` array of your [`renderDestinationImage(_:sourceImages:pluginState:at:)`](../professional_video_applications/fxtileableeffect/renderdestinationimage%28_,sourceimages,pluginstate,at%29.md) method in the order in which you specify them in your scheduling methods. (See the `FxPictureInPicture` and `FxTemporalBlur` plug-ins for examples.)

##### Remove other deprecated APIs, or update to the latest versions

Remove methods from the deprecated APIs `FxHostCapabilities`, `FxWindowAPI`, `FxAppearanceAPI`, `FxHostResourcesAPI`, `FxRenderNotificationAPI`, and `FxProgressAPI`. Convert or update any implemented methods in `FxFilter`, `FxGenerator` and `FxTransition` to the appropriate FxPlug 4 methods available in [`FxTileableEffect`](../professional_video_applications/fxtileableeffect.md). Most other FxPlug APIs are updated with new versions specifically for use in FxPlug 4 style plug-ins.

## See Also

### Legacy plug-ins
- [Versioning and obsoleting old plug-ins](./versioning-and-obsoleting-old-plug-ins.md)
  Version plug-ins to add new capabilities, or obsolete them to remove them from the Motion Library.
- [protocol FxVersioningAPI](../professional_video_applications/fxversioningapi.md)
  A collection of methods that a host application implements to identify the plug-in version used by a project when it was first created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/migrating-fxplug-3-plug-ins-to-fxplug-4)*