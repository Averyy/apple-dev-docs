# SCSensitivityAnalysisPolicy.descriptiveInterventions

**Framework**: SensitiveContentAnalysis  
**Kind**: case

An indicator that user preference requests overt detection of sensitive content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.0+

## Declaration

```swift
case descriptiveInterventions
```

## Mentions

- [Detecting nudity in media and providing intervention options](detecting-nudity-in-media-and-providing-intervention-options.md)

#### Discussion

If [`analysisPolicy`](scsensitivityanalyzer/analysispolicy.md) is this value, it indicates that the user enables both of the following:

- Communication Safety parental control in Screen Time
- Sensitive Content Warnings in your app’s settings

When your app detects nudity under this policy, your app needs to:

- Use child-appropriate language, such as broadly understood vocabulary
- Present an alert that fills the full screen.
- Intervene on the receipt of sensitve content over a network and before transmitting sensitive content over a network.

## See Also

- [SCSensitivityAnalysisPolicy.disabled](scsensitivityanalysispolicy/disabled.md)
  An indicator that the app lacks access to use the framework.
- [SCSensitivityAnalysisPolicy.simpleInterventions](scsensitivityanalysispolicy/simpleinterventions.md)
  An indicator that user preference requests discrete detection of sensitive content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysispolicy/descriptiveinterventions)*