# SCSensitivityAnalysis

**Framework**: Sensitive Content Analysis  
**Kind**: class

An object that indicates whether sensitive content is present and includes intervention guidance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.0+

## Declaration

```swift
class SCSensitivityAnalysis
```

## Mentions

- [Testing your app’s response to sensitive media](testing-your-app-s-response-to-sensitive-media.md)

#### Overview

The framework provides an instance of this class to convey the results of content sensitivity checks, for example:

- The [`SCSensitivityAnalyzer`](scsensitivityanalyzer.md) completion handler [`analyzeImage(_:completionHandler:)`](scsensitivityanalyzer/analyzeimage(_:completionhandler:).md)
- The [`SCVideoStreamAnalyzer`](scvideostreamanalyzer.md) callback [`SCVideoStreamAnalysisChangeHandler`](scvideostreamanalysischangehandler.md)

## Topics

### Confirming the presence of sensitive content
- [var isSensitive: Bool](scsensitivityanalysis/issensitive.md)
  A Boolean value that indicates whether the checked content contains sensitive material.
### Identifying content categories
- [var detectedTypes: Set<SCSensitivityAnalysis.ContentType>](scsensitivityanalysis/detectedtypes.md)
  A property that contains the categories of sensitive content that analysis detects.
- [SCSensitivityAnalysis.ContentType](scsensitivityanalysis/contenttype.md)
  A type that identifies a category of sensitive content.
### Receiving intervention guidance
- [var shouldIndicateSensitivity: Bool](scsensitivityanalysis/shouldindicatesensitivity.md)
  Intervention guidance that suggests the app indicate the presence of sensitive content.
- [var shouldInterruptVideo: Bool](scsensitivityanalysis/shouldinterruptvideo.md)
  Intervention guidance that suggests the app interrupt the video stream.
- [var shouldMuteAudio: Bool](scsensitivityanalysis/shouldmuteaudio.md)
  Intervention guidance that suggests the app mute the audio of the current video stream.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysis)*