# isSensitive

**Framework**: SensitiveContentAnalysis  
**Kind**: property

A Boolean value that indicates if checked content contains nudity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.0+

## Declaration

```swift
var isSensitive: Bool { get }
```

## Mentions

- [Testing your app’s response to sensitive media](testing-your-app-s-response-to-sensitive-media.md)

#### Discussion

The framework indicates that content is sensitive only when the active [`analysisPolicy`](scsensitivityanalyzer/analysispolicy.md) is a value other than [`SCSensitivityAnalysisPolicy.disabled`](scsensitivityanalysispolicy/disabled.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysis/issensitive)*