# SCSensitivityAnalyzer

**Framework**: SensitiveContentAnalysis  
**Kind**: class

An object that analyzes media for sensitive content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.0+

## Declaration

```swift
class SCSensitivityAnalyzer
```

## Mentions

- [Detecting nudity in media and providing intervention options](detecting-nudity-in-media-and-providing-intervention-options.md)
- [Testing your app’s response to sensitive media](testing-your-app-s-response-to-sensitive-media.md)

#### Overview

To check an image for nudity, call one of this class’s `analyzeImage` methods and pass in a user-provided image, or a URL to the image.

```swift
// Analyze an image file at a particular URL.
let response = try await analyzer.analyzeImage(at: url)
```

To analyze a video file, pass a URL to a video on disk into [`videoAnalysis(forFileAt:)`](scsensitivityanalyzer/videoanalysis(forfileat:).md) and wait for the [`hasSensitiveContent()`](scsensitivityanalyzer/videoanalysishandler/hassensitivecontent().md) method to complete.

```swift
let handler = analyzer.videoAnalysis(forFileAt: videoFileUrl)
let response = try await handler.hasSensitiveContent()
```

This class successfully detects nudity only when [`analysisPolicy`](scsensitivityanalyzer/analysispolicy.md) is a value other than [`SCSensitivityAnalysisPolicy.disabled`](scsensitivityanalysispolicy/disabled.md).

> **Note**:  To analyze a video stream rather than static files, see [`SCVideoStreamAnalyzer`](scvideostreamanalyzer.md).

## Topics

### Creating a sensitivity analyzer
- [init()](scsensitivityanalyzer/init.md)
  Creates a sensitivity analyzer.
### Determining a nudity detection strategy
- [var analysisPolicy: SCSensitivityAnalysisPolicy](scsensitivityanalyzer/analysispolicy.md)
  A property that determines if the app detects nudity and how the app responds.
### Analyzing images
- [func analyzeImage(CGImage, completionHandler: (SCSensitivityAnalysis?, (any Error)?) -> Void)](scsensitivityanalyzer/analyzeimage(_:completionhandler:).md)
  Analyzes an image for sensitive content and runs code on completion.
- [func analyzeImage(at: URL, completionHandler: (SCSensitivityAnalysis?, (any Error)?) -> Void)](scsensitivityanalyzer/analyzeimage(at:completionhandler:).md)
  Analyzes an image file on disk at a URL and runs code on completion.
### Analyzing video
- [func videoAnalysis(forFileAt: URL) -> SCSensitivityAnalyzer.VideoAnalysisHandler](scsensitivityanalyzer/videoanalysis(forfileat:).md)
  Analyzes a video file on disk at a URL for sensitive content.
- [SCSensitivityAnalyzer.VideoAnalysisHandler](scsensitivityanalyzer/videoanalysishandler.md)
  An object that checks if a video contains sensitive content and provides status updates.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum SCSensitivityAnalysisPolicy](scsensitivityanalysispolicy.md)
  Configurations that represent the way the framework checks for sensitive content and how the app responds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalyzer)*