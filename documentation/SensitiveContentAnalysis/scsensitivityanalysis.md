# SCSensitivityAnalysis

**Framework**: SensitiveContentAnalysis  
**Kind**: class

An object that determines if checked content contains nudity.

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

The completion handler for [`SCSensitivityAnalyzer`](scsensitivityanalyzer.md) methods, such as [`analyzeImage(_:completionHandler:)`](scsensitivityanalyzer/analyzeimage(_:completionhandler:).md), receive an instance of this type as a `results` parameter.

```swift
// Check a loaded image for nudity.
let response = try await analyzer.analyzeImage(image.cgImage)

if response.isSensitive {
    // Check the active `analysisPolicy` on how to proceed.
}
```

For more information about checking the active [`analysisPolicy`](scsensitivityanalyzer/analysispolicy.md), see [`SCSensitivityAnalysisPolicy`](scsensitivityanalysispolicy.md).

## Topics

### Content-sensitivity check results
- [var isSensitive: Bool](scsensitivityanalysis/issensitive.md)
  A Boolean value that indicates if checked content contains nudity.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysis)*