# ScreenCaptureKit

**Framework**: ScreenCaptureKit  
**Kind**: module

Stream screen content and audio to your app with fine-grained control over what you capture.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

#### Overview

Use ScreenCaptureKit to capture high-performance video and audio across iOS, iPadOS, macOS, tvOS, and visionOS. The framework gives you fine-grained control to select and stream only the content you want to capture, delivering media to your app as [`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer) objects with the associated metadata.

> ❗ **Important**: ScreenCaptureKit replaces ReplayKit for screen streaming and mirroring. A broadcast extension is no longer necessary.

Use [`SCContentSharingPicker`](sccontentsharingpicker.md), the system screen-sharing control, as the recommended approach for letting people select content sources and manage active streams, rather than building your own selection UI. To capture content while your app is in the background, configure the appropriate [`Configuring background execution modes`](https://developer.apple.com/documentation/Xcode/configuring-background-execution-modes) in the Signing & Capabilities pane in Xcode.

Request screen recording permission from the person before capturing content. In the Info pane of the Xcode target editor, add a `NSScreenCaptureUsageDescription` key with a description of why your app requires screen recording access.

> **Note**: For related WWDC sessions, see [`Meet ScreenCaptureKit`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10156) (WWDC22 Session 10156), [`Take ScreenCaptureKit to the next level`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10155) (WWDC22 Session 10155), and [`What’s new in ScreenCaptureKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10136/) (WWDC23 Session 10136).

## Topics

### Essentials
- [ScreenCaptureKit updates](../Updates/ScreenCaptureKit.md)
  Learn about important changes to ScreenCaptureKit.
- [Persistent Content Capture](../BundleResources/Entitlements/com.apple.developer.persistent-content-capture.md)
  A Boolean value that indicates whether a Virtual Network Computing (VNC) app needs persistent access to screen capture.
- [Capturing screen content on iOS](capturing-screen-content-on-ios.md)
  Record and share screen captures on iOS by presenting the system content-sharing picker.
- [Capturing screen content in macOS](capturing-screen-content-in-macos.md)
  Stream desktop content like displays, apps, and windows by adopting screen capture in your app.
### Shareable content
- [class SCShareableContent](scshareablecontent.md)
  An instance that represents a set of displays, apps, and windows that your app can capture.
- [class SCShareableContentInfo](scshareablecontentinfo.md)
  An instance that provides information for the content in a given stream.
- [enum SCShareableContentStyle](scshareablecontentstyle.md)
  The style of content presented in a stream.
- [class SCDisplay](scdisplay.md)
  An instance that represents a display device.
- [class SCRunningApplication](scrunningapplication.md)
  An instance that represents an app running on a device.
- [class SCWindow](scwindow.md)
  An instance that represents an onscreen window.
### Content capture
- [class SCStream](scstream.md)
  An instance that represents a stream of shareable content.
- [class SCStreamConfiguration](scstreamconfiguration.md)
  An instance that provides the output configuration for a stream.
- [class SCContentFilter](sccontentfilter.md)
  An instance that filters the content a stream captures.
- [protocol SCStreamDelegate](scstreamdelegate.md)
  A delegate protocol your app implements to respond to stream events.
- [class SCScreenshotManager](scscreenshotmanager.md)
  An instance for the capture of single frames from a stream.
- [class SCScreenshotConfiguration](scscreenshotconfiguration.md)
  An object that contains screenshot properties such as output width, height, and image quality specifications.
- [class SCScreenshotOutput](scscreenshotoutput.md)
  An object that contains all images requested by the client.
- [class SCVideoEffectOutput](scvideoeffectoutput.md)
### Output processing
- [protocol SCStreamOutput](scstreamoutput.md)
  A delegate protocol your app implements to receive capture stream output events.
- [enum SCStreamOutputType](scstreamoutputtype.md)
  Constants that represent output types for a stream frame.
- [struct SCStreamFrameInfo](scstreamframeinfo.md)
  An instance that defines metadata keys for a stream frame.
- [enum SCFrameStatus](scframestatus.md)
  Status values for a frame from a stream.
- [class SCClipBufferingOutput](scclipbufferingoutput.md)
### System content-sharing picker
- [class SCContentSharingPicker](sccontentsharingpicker.md)
  An instance of a picker presented by the operating system for managing frame-capture streams.
- [struct SCContentSharingPickerConfiguration](sccontentsharingpickerconfiguration-swift.struct.md)
  An instance for configuring the system content-sharing picker.
- [struct SCContentSharingPickerMode](sccontentsharingpickermode.md)
  Available modes for selecting streaming content from a picker presented by the operating system.
- [protocol SCContentSharingPickerObserver](sccontentsharingpickerobserver.md)
  An observer protocol your app implements to receive messages from the operating system’s content picker.
### Stream errors (Swift)
- [let SCStreamErrorDomain: String](scstreamerrordomain.md)
  A string representation of the error domain.
- [struct SCStreamError](scstreamerror.md)
  An instance representing a ScreenCaptureKit framework error.
### Classes
- [class SCRecordingEditor](screcordingeditor.md)
### Protocols
- [protocol SCClipBufferingOutputDelegate](scclipbufferingoutputdelegate.md)
- [protocol SCRecordingEditorDelegate](screcordingeditordelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/ScreenCaptureKit)*