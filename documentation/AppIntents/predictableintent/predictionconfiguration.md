# predictionConfiguration

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

A collection of predictions the system can use when it suggests the app intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@IntentPredictionsBuilder
<Self> static var predictionConfiguration: Self.Prediction { get }
```

## See Also

- [protocol IntentPredictionConfiguration](intentpredictionconfiguration.md)
  An interface that provides the configuration for a single prediction.
- [enum IntentPredictionsBuilder](intentpredictionsbuilder.md)
  A result builder that allows you to declaratively describe the predictions for an app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/predictableintent/predictionconfiguration)*