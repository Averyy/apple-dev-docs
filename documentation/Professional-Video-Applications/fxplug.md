# FxPlug

**Framework**: Professional-Video-Applications  
**Role**: API Collection

Create custom effects plug-ins for Final Cut Pro and Motion.

## Overview

When the effect or look you want to achieve can’t be created with the filters or generators provided with Final Cut Pro or Motion, use the FxPlug software development kit (SDK) to write your own custom visual effects. FxPlug is a compact, powerful image-processing plug-in architecture that lets you create unique, hardware-accelerated or CPU-based effects plug-ins with customized UI and onscreen controls.

FxPlug consists primarily of Objective-C protocol definitions. You create a plug-in by writing code in Objective-C, Objective-C++, or Swift that conforms to these protocols, implementing the methods declared by the protocols. The host application provides the capabilities in all the protocols that have the API suffix. Your plug-in is responsible for implementing the other protocols.

![A screenshot of a frame in a Motion file depicting a filter called “Light Rays” applied to an image of a tower in an Italian town.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3385875@2x.png)

FxPlug 4 introduces fully “out-of-process” FxPlug plug-ins, which have no component that runs inside of the host application process. Out-of-process plug-ins provide improved security for end users and allow plug-in developers the freedom to choose from a variety of rendering technologies, such as Metal, Core Graphics or Core Image to develop unique plug-ins that include on-screen controls and custom user interface elements—all running seamlessly in the host application. Plug-in developers can choose to implement in either Swift or Objective-C.

> **Note**:  OpenGL and OpenCL are deprecated in macOS.

Additionally, the new [`FxTileableEffect`](../professional_video_applications/fxtileableeffect.md) API lets third-party plug-ins render only portions of the output (known as *tiles*) for more efficiency, in the same manner as Apple’s own plug-ins.

This documentation highlights new and updated concepts and APIs in FxPlug 4. You can find documentation for legacy plug-ins created with FxPlug 3 in the [archived FxPlug 3.1.1 documentation](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/FXPlug_overview/FXPlugSDKOverview/FXPlugSDKOverview.html#//apple_ref/doc/uid/TP40002180).

> **Note**:  FxPlug 3 isn’t supported in Final Cut Pro or Motion.

## Topics

### Essentials
- [Setting up for FxPlug development](./setting-up-for-fxplug-development.md)
  Download and install the required software to develop FxPlug plug-ins.
- [Using out-of-process FxPlug plug-ins](./using-out-of-process-fxplug-plug-ins.md)
  Register and render FxPlug plug-ins with Motion and Final Cut Pro.
### Plug-in fundamentals
- [Building an FxPlug plug-in from an Xcode template](./building-an-fxplug-plug-in-from-an-xcode-template.md)
  Create a plug-in in Xcode with the FxPlug template.
- [Building an FxPlug plug-in manually](./building-an-fxplug-plug-in-manually.md)
  Create your own plug-in in Xcode.
- [Using FxPlug APIs](./using-fxplug-apis.md)
  Use various FxPlug APIs to communicate with host apps like Motion or Final Cut Pro.
- [Editing property lists for FxPlug plug-ins](./editing-property-lists-for-fxplug-plug-ins.md)
  Modify the way hosts recognize and display your FxPlug plug-in.
- [Thread safety in plug-ins](./thread-safety-in-plug-ins.md)
  Learn about reentrancy for plug-ins and best practices to make them thread safe.
### Rendering
- [Rendering in FxPlug](./rendering-in-fxplug.md)
  Use Metal or other frameworks to render images with your FxPlug plug-in.
- [Communicating with the plug-in state](./communicating-with-the-plug-in-state.md)
  Prepare the necessary information, such as parameter values, for your FxPlug plug-in to render.
- [Working with tiled images](./working-with-tiled-images.md)
  Render only the necessary tiles of an image in your FxPlug plug-in to improve efficiency.
- [Optimizing FxPlug plug-ins](./optimizing-fxplug-plug-ins.md)
  Maintain consistent rendering at all resolutions and aspect ratios by using pixel transforms.
- [protocol FxTileableEffect](../professional_video_applications/fxtileableeffect.md)
  The designated initializer for your plug-in for rendering only certain portions of the plug-in’s output, referred to as tiles.
### User interface
- [Adding parameters to plug-ins](./adding-parameters-to-plug-ins.md)
  Create standard and custom user-facing parameters for your plug-in that will appear in the inspector.
- [Adding onscreen controls to plug-ins](./adding-onscreen-controls-to-plug-ins.md)
  Simplify user interaction by using onscreen controls for your FxPlug plug-in.
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
### 3D and lighting
- [protocol Fx3DAPI_v5](../professional_video_applications/fx3dapi_v5.md)
  An API that defines the methods the host application provides to get information about the 3D environment, including camera and object transforms.
- [protocol FxLightingAPI_v3](../professional_video_applications/fxlightingapi_v3.md)
  An API you use to get information about lights in a scene in a Motion project.
- [class FxMatrix44](../professional_video_applications/fxmatrix44.md)
  The `FxMatrix` class encapsulates a 4x4 matrix object and provides matrix inversion and transforming of 2D and 3D points.
### Color
- [Managing color space and gamut in plug-ins](./managing-color-space-and-gamut-in-plug-ins.md)
  Control the appearance of your rendering by using the color gamut API.
- [protocol FxColorGamutAPI_v2](../professional_video_applications/fxcolorgamutapi_v2.md)
  A protocol that handles plug-in queries to the host for the project’s color gamut.
### Time and analysis
- [Understanding time in FxPlug](./understanding-time-in-fxplug.md)
  Learn about time handling in host apps and plug-ins.
- [Scheduling media in plug-ins](./scheduling-media-in-plug-ins.md)
  Use the scheduling APIs in FxPlug to retrieve frames from different times.
- [protocol FxTimingAPI_v4](../professional_video_applications/fxtimingapi_v4.md)
  A protocol that defines the methods provided by the host, so that a plug-in can query the timing properties of its input.
- [protocol FxKeyframeAPI_v3](../professional_video_applications/fxkeyframeapi_v3.md)
  A collection of methods for manipulating the keyframes of your FxPlug 4 plug-in.
- [Analyzing media](./analyzing-media.md)
  Use the FxPlug analysis API to analyze frames of source media before rendering them.
- [protocol FxAnalysisAPI](../professional_video_applications/fxanalysisapi.md)
  A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.
- [protocol FxAnalysisAPI_v2](../professional_video_applications/fxanalysisapi_v2.md)
  A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.
- [protocol FxAnalyzer](../professional_video_applications/fxanalyzer.md)
  A protocol you implement in your plug-in to analyze frames that the plug-in is applied to.
### Accessing host data
- [protocol FxProjectAPI](../professional_video_applications/fxprojectapi.md)
  Methods you use to get information about the project in which your plug-in instance is running.
- [protocol FxProjectAPI_v2](../professional_video_applications/fxprojectapi_v2.md)
  The method you use to get aspect ratio information about the project in which your plug-in instance is running.
### Testing and deployment
- [Testing FxPlug plug-ins](./testing-fxplug-plug-ins.md)
  Test and debug FxPlug plug-ins using a variety of methods.
- [Preparing plug-ins for use in Final Cut Pro](./preparing-plug-ins-for-use-in-final-cut-pro.md)
  Add a plug-in to a Motion effect template to use in Final Cut Pro.
- [Notarizing your FxPlug plug-in](./notarizing-your-fxplug-plug-in.md)
  Give users confidence in your FxPlug plug-in by enabling notarization.
### Legacy plug-ins
- [Migrating FxPlug 3 plug-ins to FxPlug 4](./migrating-fxplug-3-plug-ins-to-fxplug-4.md)
  Update existing FxPlug 3 plug-ins to out-of-process FxPlug 4 plug-ins.
- [Versioning and obsoleting old plug-ins](./versioning-and-obsoleting-old-plug-ins.md)
  Version plug-ins to add new capabilities, or obsolete them to remove them from the Motion Library.
- [protocol FxVersioningAPI](../professional_video_applications/fxversioningapi.md)
  A collection of methods that a host application implements to identify the plug-in version used by a project when it was first created.
### Macros
- [FxPlug macros](./fxplug-macros.md)

## See Also

### Effects
- [Create an effect template for use in Final Cut Pro](./create-an-effect-template-for-use-in-final-cut-pro.md)
  Use Motion to create custom filters, generators, and transitions for Final Cut Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/fxplug)*