# SCSensitivityAnalysisPolicy

**Framework**: SensitiveContentAnalysis  
**Kind**: enum

Configurations that represent the way the framework checks for sensitive content and how the app responds.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.0+

## Declaration

```swift
enum SCSensitivityAnalysisPolicy
```

#### Overview

This enumeration defines the possible values for the [`SCSensitivityAnalyzer`](scsensitivityanalyzer.md) property [`analysisPolicy`](scsensitivityanalyzer/analysispolicy.md). The values of the policy determine how your app manages sensitive content detection.

```swift
// Check the current analysis policy. 
let policy = analyzer.analysisPolicy
if policy == .disabled { return } 
else if policy == .simpleInterventions {
    // The Sensitive Content Warning setting is active.
} else if policy == .descriptiveInterventions {
    // The Communication Safety setting is active.
}
```

For guidance about observing the active analysis policy, see [`Detecting nudity in media and providing intervention options`](detecting-nudity-in-media-and-providing-intervention-options.md).

## Topics

### Checking and intervention strategies
- [SCSensitivityAnalysisPolicy.disabled](scsensitivityanalysispolicy/disabled.md)
  An indicator that the app lacks access to use the framework.
- [SCSensitivityAnalysisPolicy.simpleInterventions](scsensitivityanalysispolicy/simpleinterventions.md)
  An indicator that user preference requests discrete detection of sensitive content.
- [SCSensitivityAnalysisPolicy.descriptiveInterventions](scsensitivityanalysispolicy/descriptiveinterventions.md)
  An indicator that user preference requests overt detection of sensitive content.
### Creating an analysis policy value
- [init?(rawValue: Int)](scsensitivityanalysispolicy/init(rawvalue:).md)
  Creates an analysis policy value from the enumeration’s underlying type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class SCSensitivityAnalyzer](scsensitivityanalyzer.md)
  An object that analyzes media for sensitive content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysispolicy)*