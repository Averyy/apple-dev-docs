# PredictableIntent

**Framework**: App Intents  
**Kind**: protocol

An interface that allows the system to suggest the app intent to someone in the future using predictions you provide.

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
protocol PredictableIntent : AppIntent
```

## Topics

### Providing predictions
- [static var predictionConfiguration: Self.Prediction](predictableintent/predictionconfiguration.md)
  A collection of predictions the system can use when it suggests the app intent.
- [associatedtype Prediction : IntentPredictionConfiguration](predictableintent/prediction.md)
- [protocol IntentPredictionConfiguration](intentpredictionconfiguration.md)
  An interface that provides the configuration for a single prediction.
- [enum IntentPredictionsBuilder](intentpredictionsbuilder.md)
  A result builder that allows you to declaratively describe the predictions for an app intent.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct IntentPrediction](intentprediction.md)
  A prediction for a specific app intent that the system might display to someone when it’s relevant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/predictableintent)*