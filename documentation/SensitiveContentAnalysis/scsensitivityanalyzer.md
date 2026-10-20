# SCSensitivityAnalyzer

**Framework**: Sensitive Content Analysis  
**Kind**: class  
**Role**: Class

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

```objc
@interface SCSensitivityAnalyzer : NSObject
```

## Mentions

- [Detecting sensitive content in media and providing intervention options](./detecting-nudity-in-media-and-providing-intervention-options.md)
- [Testing your app’s response to sensitive media](./testing-your-app-s-response-to-sensitive-media.md)

#### Overview

To check an image for sensitive content, call one of this class’s `analyzeImage` methods and pass in a user-provided image, or a URL to the image.

```swift
// Analyze an image file at a particular URL.
let response = try await analyzer.analyzeImage(at: url)
```

To analyze a video file, pass a URL to a video on disk into [`videoAnalysis(forFileAt:)`](./scsensitivityanalyzer/videoanalysis%28forfileat%29.md) and wait for the [`hasSensitiveContent()`](./scsensitivityanalyzer/videoanalysishandler/hassensitivecontent%28%29.md) method to complete.

```swift
let handler = analyzer.videoAnalysis(forFileAt: videoFileUrl)
let response = try await handler.hasSensitiveContent()
```

This class successfully detects sensitive content only when [`analysisPolicy`](./scsensitivityanalyzer/analysispolicy.md) is a value other than [`SCSensitivityAnalysisPolicy.disabled`](./scsensitivityanalysispolicy/disabled.md).

> **Note**:  To analyze a video stream rather than static files, see [`SCVideoStreamAnalyzer`](./scvideostreamanalyzer.md).

## Topics

### Creating a sensitivity analyzer
- [init()](./scsensitivityanalyzer/init%28%29.md)
  Creates a sensitivity analyzer.
### Determining a detection strategy
- [var analysisPolicy: SCSensitivityAnalysisPolicy](./scsensitivityanalyzer/analysispolicy.md)
  A property that determines if the app detects nudity and how the app responds.
### Analyzing images
- [func analyzeImage(CGImage, completionHandler: (SCSensitivityAnalysis?, (any Error)?) -> Void)](./scsensitivityanalyzer/analyzeimage%28_,completionhandler%29.md)
  Analyzes an image for sensitive content and runs code on completion.
- [func analyzeImage(at: URL, completionHandler: (SCSensitivityAnalysis?, (any Error)?) -> Void)](./scsensitivityanalyzer/analyzeimage%28at,completionhandler%29.md)
  Analyzes an image file on disk at a URL and runs code on completion.
### Analyzing video
- [func videoAnalysis(forFileAt: URL) -> SCSensitivityAnalyzer.VideoAnalysisHandler](./scsensitivityanalyzer/videoanalysis%28forfileat%29.md)
  Analyzes a video file on disk at a URL for sensitive content.
- [SCSensitivityAnalyzer.VideoAnalysisHandler](./scsensitivityanalyzer/videoanalysishandler.md)
  An object that checks if a video contains sensitive content and provides status updates.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Image and video file analysis
- [enum SCSensitivityAnalysisPolicy](./scsensitivityanalysispolicy.md)
  Configurations that represent the way the framework checks for sensitive content and how the app responds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalyzer)*