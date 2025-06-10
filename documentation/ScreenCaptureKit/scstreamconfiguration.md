# SCStreamConfiguration

**Framework**: ScreenCaptureKit  
**Kind**: class

An instance that provides the output configuration for a stream.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
class SCStreamConfiguration
```

#### Overview

Creating an instance of this class provides a default configuration for a stream. Only configure its properties if you need to customize the output.

## Topics

### Specifying dimensions
- [var width: Int](scstreamconfiguration/width.md)
  The width of the output.
- [var height: Int](scstreamconfiguration/height.md)
  The height of the output.
- [var scalesToFit: Bool](scstreamconfiguration/scalestofit.md)
  A Boolean value that indicates whether to scale the output to fit the configured width and height.
- [var sourceRect: CGRect](scstreamconfiguration/sourcerect.md)
  A rectangle that specifies the source area to capture.
- [var destinationRect: CGRect](scstreamconfiguration/destinationrect.md)
  A rectangle that specifies a destination into which to write the output.
- [var preservesAspectRatio: Bool](scstreamconfiguration/preservesaspectratio.md)
  A Boolean value that determines if the stream preserves aspect ratio.
### Configuring colors
- [var pixelFormat: OSType](scstreamconfiguration/pixelformat.md)
  A pixel format for sample buffers that a stream outputs.
- [var colorMatrix: CFString](scstreamconfiguration/colormatrix.md)
  A color matrix to apply to the output surface.
- [var colorSpaceName: CFString](scstreamconfiguration/colorspacename.md)
  A color space to use for the output buffer.
- [var backgroundColor: CGColor](scstreamconfiguration/backgroundcolor.md)
  A background color for the output.
### Configuring captured elements
- [var showsCursor: Bool](scstreamconfiguration/showscursor.md)
  A Boolean value that determines whether the cursor is visible in the stream.
- [var shouldBeOpaque: Bool](scstreamconfiguration/shouldbeopaque.md)
  A Boolean value that indicates if semitransparent content presents as opaque.
- [var capturesShadowsOnly: Bool](scstreamconfiguration/capturesshadowsonly.md)
  A Boolean value that indicates if the stream only captures shadows.
- [var ignoreShadowsDisplay: Bool](scstreamconfiguration/ignoreshadowsdisplay.md)
  A Boolean value that indicates if the stream ignores the capturing of window shadows when streaming in display style.
- [var ignoreShadowsSingleWindow: Bool](scstreamconfiguration/ignoreshadowssinglewindow.md)
  A Boolean value that indicates if the stream ignores the capturing of window shadows when streaming in window style.
- [var ignoreGlobalClipDisplay: Bool](scstreamconfiguration/ignoreglobalclipdisplay.md)
  A Boolean value that indicates if the stream ignores content clipped past the edge of a display, when streaming in display style.
- [var ignoreGlobalClipSingleWindow: Bool](scstreamconfiguration/ignoreglobalclipsinglewindow.md)
  A Boolean value that indicates if the stream ignores content clipped past the edge of a display, when streaming in window style.
### Configuring captured frames
- [var queueDepth: Int](scstreamconfiguration/queuedepth.md)
  The maximum number of frames for the queue to store.
- [var minimumFrameInterval: CMTime](scstreamconfiguration/minimumframeinterval.md)
  The desired minimum time between frame updates, in seconds.
- [var captureResolution: SCCaptureResolutionType](scstreamconfiguration/captureresolution.md)
  The resolution at which to capture source content.
- [enum SCCaptureResolutionType](sccaptureresolutiontype.md)
  Available resolutions for content capture.
### Configuring audio
- [var capturesAudio: Bool](scstreamconfiguration/capturesaudio.md)
  A Boolean value that indicates whether to capture audio.
- [var sampleRate: Int](scstreamconfiguration/samplerate.md)
  The sample rate for audio capture.
- [var channelCount: Int](scstreamconfiguration/channelcount.md)
  The number of audio channels to capture.
- [var excludesCurrentProcessAudio: Bool](scstreamconfiguration/excludescurrentprocessaudio.md)
  A Boolean value that indicates whether to exclude audio from your app during capture.
### Identifying a stream
- [var streamName: String?](scstreamconfiguration/streamname.md)
  A name that you provide for identifying the stream.
### Notifying presenters
- [var presenterOverlayPrivacyAlertSetting: SCPresenterOverlayAlertSetting](scstreamconfiguration/presenteroverlayprivacyalertsetting.md)
  A value indicating if alerts appear to presenters while using Presenter Overlay.
- [enum SCPresenterOverlayAlertSetting](scpresenteroverlayalertsetting.md)
  Configures how to present streaming notifications to a streamer of Presenter Overlay.
### Enumerations
- [enum SCCaptureDynamicRange](sccapturedynamicrange.md)
- [SCStreamConfiguration.Preset](scstreamconfiguration/preset.md)
### Initializers
- [convenience init(preset: SCStreamConfiguration.Preset)](scstreamconfiguration/init(preset:).md)
### Instance Properties
- [var captureDynamicRange: SCCaptureDynamicRange](scstreamconfiguration/capturedynamicrange.md)
- [var captureMicrophone: Bool](scstreamconfiguration/capturemicrophone.md)
- [var includeChildWindows: Bool](scstreamconfiguration/includechildwindows.md)
- [var microphoneCaptureDeviceID: String?](scstreamconfiguration/microphonecapturedeviceid.md)
- [var showMouseClicks: Bool](scstreamconfiguration/showmouseclicks.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SCStream](scstream.md)
  An instance that represents a stream of shareable content.
- [class SCContentFilter](sccontentfilter.md)
  An instance that filters the content a stream captures.
- [protocol SCStreamDelegate](scstreamdelegate.md)
  A delegate protocol your app implements to respond to stream events.
- [class SCScreenshotManager](scscreenshotmanager.md)
  An instance for the capture of single frames from a stream.
- [class SCScreenshotConfiguration](scscreenshotconfiguration.md)
- [class SCScreenshotOutput](scscreenshotoutput.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration)*