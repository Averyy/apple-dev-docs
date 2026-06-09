# SCSensitivityAnalysisPolicy.simpleInterventions

**Framework**: Sensitive Content Analysis  
**Kind**: case

An indicator that user preference requests discrete detection of sensitive content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.0+

## Declaration

```swift
case simpleInterventions
```

## Mentions

- [Detecting sensitive content in media and providing intervention options](detecting-nudity-in-media-and-providing-intervention-options.md)

#### Discussion

If this value is [`analysisPolicy`](scsensitivityanalyzer/analysispolicy.md), it indicates that the person turned on both of the following:

- Sensitive Content Warnings user preference
- Sensitive Content Warnings in your app’s settings

When your app detects sensitive content under this policy, your app needs to:

- Intervene on the receipt of sensitive content over the network but allow the app to transmit content over the network unchecked.
- Keep the intervention minimal by describing the issue briefly and updating your app’s UI unobstructively. For example, consider blurring and annotating the area that otherwise presents the sensitive content versus raising a new fullscreen alert.

## See Also

- [SCSensitivityAnalysisPolicy.disabled](scsensitivityanalysispolicy/disabled.md)
  An indicator that the app lacks access to use the framework.
- [SCSensitivityAnalysisPolicy.descriptiveInterventions](scsensitivityanalysispolicy/descriptiveinterventions.md)
  An indicator that the person requests overt detection of sensitive content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysispolicy/simpleinterventions)*