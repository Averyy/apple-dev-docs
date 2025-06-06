# analysisPolicy

**Framework**: SensitiveContentAnalysis  
**Kind**: property

A property that determines if the app detects nudity and how the app responds.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.0+

## Declaration

```swift
var analysisPolicy: SCSensitivityAnalysisPolicy { get }
```

## Mentions

- [Detecting nudity in media and providing intervention options](detecting-nudity-in-media-and-providing-intervention-options.md)

#### Discussion

Before attempting to use the framework, first check the [`analysisPolicy`](scsensitivityanalyzer/analysispolicy.md):

```swift
let policy = analyzer.analysisPolicy
if policy == .disabled { return }
```

An app can utilize the SensitiveContentAnalysis framework when the system sets the value of this property to either:

- [`SCSensitivityAnalysisPolicy.simpleInterventions`](scsensitivityanalysispolicy/simpleinterventions.md), which indicates that a user activates the Communication Safety parental control in Screen Time.
- [`SCSensitivityAnalysisPolicy.descriptiveInterventions`](scsensitivityanalysispolicy/descriptiveinterventions.md), which indicates that the user activates the Sensitive Content Warning user preference.

The framework won’t detect nudity if the system disables this property. For more information on why the system disables sensitive content analysis, see [`SCSensitivityAnalysisPolicy.disabled`](scsensitivityanalysispolicy/disabled.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalyzer/analysispolicy)*