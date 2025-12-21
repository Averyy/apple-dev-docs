# SCVideoStreamAnalyzer

**Framework**: SensitiveContentAnalysis  
**Kind**: class

An object that monitors a stream of video by analyzing frames for sensitive content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class SCVideoStreamAnalyzer
```

## Mentions

- [Detecting nudity in media and providing intervention options](detecting-nudity-in-media-and-providing-intervention-options.md)

#### Overview

Use this class to detect senstive content in a video stream, such as on a conference call that your app implements. The class detects senstive content in the video stream from either the device’s camera or the remote devices signed into the call, depending on how you configure the analyzer.

Create an instance of this class for each video stream in the call.

To begin analyzing the stream, pass it to either [`beginAnalysis(of:)`](scvideostreamanalyzer/beginanalysis(of:)-78qm.md) ([`AVCaptureDeviceInput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDeviceInput)) or [`beginAnalysis(of:)`](scvideostreamanalyzer/beginanalysis(of:)-9ehkx.md) ([`VTDecompressionSession`](https://developer.apple.com/documentation/VideoToolbox/VTDecompressionSession)), depending on your video playback implementation.

> ❗ **Important**:  This class works only when the Communication Safety parental control in Screen Time is enabled, or when the Sensitive Content Warnings setting is turned on. The initializers of this class throw an error if both settings are off.

##### React to Sensitive Content

When the framework detects sensitive content in the stream, it calls [`analysisChangedHandler`](scvideostreamanalyzer/analysischangedhandler.md) immediately with an [`SCSensitivityAnalysis`](scsensitivityanalysis.md) object that includes information about the detection.

You implement the [`analysisChangedHandler`](scvideostreamanalyzer/analysischangedhandler.md) callback to inspect the detection results, which includes confirmation that content is sensitve as well as guidance on next steps your app can take. The framework offers your app suggestions in the handler, which include:

- Alerting the person to the presence of sensitive content ([`shouldIndicateSensitivity`](scsensitivityanalysis/shouldindicatesensitivity.md))
- Interrupting video playback ([`shouldInterruptVideo`](scsensitivityanalysis/shouldinterruptvideo.md))
- Muting audio ([`shouldMuteAudio`](scsensitivityanalysis/shouldmuteaudio.md))

To stop analyzing the stream, call [`endAnalysis()`](scvideostreamanalyzer/endanalysis().md). If your app implements a custom stream decoder, you can analyze individual frames by passing pixel buffers to [`analyze(_:)`](scvideostreamanalyzer/analyze(_:).md).

In the event of an error during analysis, the handler receives an error object that details what went wrong. For more information, see: [`SCVideoStreamAnalysisChangeHandler`](scvideostreamanalysischangehandler.md).

##### Add the App Entitlement

To use this class, the system requires the [`com.apple.developer.sensitivecontentanalysis.client`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.sensitivecontentanalysis.client) entitlement in your app’s code signature. Calls to the framework fail to return positive results without it. You can can add this entitlement to your app by enabling the Sensitive Content Analysis capability in Xcode; see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

For more information, see [`Detecting nudity in media and providing intervention options`](detecting-nudity-in-media-and-providing-intervention-options.md).

## Topics

### Creating a video stream analyzer
- [init(participantUUID: String, streamDirection: SCVideoStreamAnalyzer.StreamDirection) throws](scvideostreamanalyzer/init(participantuuid:streamdirection:).md)
  Creates a video stream analyzer for the given call participant and stream option.
- [SCVideoStreamAnalyzer.StreamDirection](scvideostreamanalyzer/streamdirection.md)
  Options for the different types of analyzed video streams.
### Analyzing a video stream
- [func analyze(CVPixelBuffer)](scvideostreamanalyzer/analyze(_:).md)
  Analyzes individual video-stream frames for sensitive content.
- [func beginAnalysis(of: AVCaptureDeviceInput) throws](scvideostreamanalyzer/beginanalysis(of:)-78qm.md)
  Analyzes video frames for the given capture device input.
- [func beginAnalysis(of: VTDecompressionSession) throws](scvideostreamanalyzer/beginanalysis(of:)-9ehkx.md)
  Analyzes video frames for the given decompression session.
- [var analysisChanges: some AsyncSequence<SCSensitivityAnalysis, any Error>](scvideostreamanalyzer/analysischanges.md)
  A stream your app uses to receive video-stream analysis results.
- [func endAnalysis()](scvideostreamanalyzer/endanalysis.md)
  Stops stream analysis.
### Responding to sensitive content
- [var analysis: SCSensitivityAnalysis?](scvideostreamanalyzer/analysis.md)
  The results of the first detected sensitive video frame.
- [func continueStream()](scvideostreamanalyzer/continuestream.md)
  Indicates that your app is ready to resume video stream analysis.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer)*