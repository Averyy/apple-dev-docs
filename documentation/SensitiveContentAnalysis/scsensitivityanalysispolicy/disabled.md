# SCSensitivityAnalysisPolicy.disabled

**Framework**: SensitiveContentAnalysis  
**Kind**: case

An indicator that the app lacks access to use the framework.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.0+

## Declaration

```swift
case disabled
```

## Mentions

- [Detecting nudity in media and providing intervention options](detecting-nudity-in-media-and-providing-intervention-options.md)

#### Discussion

If [`analysisPolicy`](scsensitivityanalyzer/analysispolicy.md) is this value, the framework doesn’t detect nudity. The system disables sensitive content analysis under any of the following conditions:

- The app lacks the necessary [`com.apple.developer.sensitivecontentanalysis.client`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.sensitivecontentanalysis.client) entitlement.
- Neither the Sensitive Content Warning user preference nor the Communication Safety parental control in Screen Time are active.
- The user disables the Sensitive Content Warnings toggle in your app’s Settings.

## See Also

- [SCSensitivityAnalysisPolicy.simpleInterventions](scsensitivityanalysispolicy/simpleinterventions.md)
  An indicator that user preference requests discrete detection of sensitive content.
- [SCSensitivityAnalysisPolicy.descriptiveInterventions](scsensitivityanalysispolicy/descriptiveinterventions.md)
  An indicator that user preference requests overt detection of sensitive content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysispolicy/disabled)*