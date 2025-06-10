# IntentPredictionConfiguration

**Framework**: App Intents  
**Kind**: protocol

An interface that provides the configuration for a single prediction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol IntentPredictionConfiguration
```

## Topics

### Associated Types
- [associatedtype Intent : AppIntent](intentpredictionconfiguration/intent.md)

## Relationships

### Conforming Types
- [IntentPrediction](intentprediction.md)
- [TupleIntentPrediction](tupleintentprediction.md)

## See Also

- [static var predictionConfiguration: Self.Prediction](predictableintent/predictionconfiguration.md)
  A collection of predictions the system can use when it suggests the app intent.
- [associatedtype Prediction : IntentPredictionConfiguration](predictableintent/prediction.md)
- [enum IntentPredictionsBuilder](intentpredictionsbuilder.md)
  A result builder that allows you to declaratively describe the predictions for an app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentpredictionconfiguration)*