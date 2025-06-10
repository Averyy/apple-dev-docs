# IntentPredictionsBuilder

**Framework**: App Intents  
**Kind**: enum

A result builder that allows you to declaratively describe the predictions for an app intent.

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
@resultBuilder
enum IntentPredictionsBuilder<Intent> where Intent : AppIntent
```

## Topics

### Building predictions
- [static func buildBlock<A0>(A0) -> A0](intentpredictionsbuilder/buildblock(_:).md)
- [static func buildBlock<A0, A1>(A0, A1) -> TupleIntentPrediction<A0.Intent, (A0, A1)>](intentpredictionsbuilder/buildblock(_:_:).md)
- [static func buildBlock<A0, A1, A2>(A0, A1, A2) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2)>](intentpredictionsbuilder/buildblock(_:_:_:).md)
- [struct TupleIntentPrediction](tupleintentprediction.md)
  A type that represents a collection of predictions for a specific app intent.
### Type Methods
- [static func buildBlock<A0, A1, A2, A3>(A0, A1, A2, A3) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2, A3)>](intentpredictionsbuilder/buildblock(_:_:_:_:).md)
- [static func buildBlock<A0, A1, A2, A3, A4>(A0, A1, A2, A3, A4) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2, A3, A4)>](intentpredictionsbuilder/buildblock(_:_:_:_:_:).md)
- [static func buildBlock<A0, A1, A2, A3, A4, A5>(A0, A1, A2, A3, A4, A5) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2, A3, A4, A5)>](intentpredictionsbuilder/buildblock(_:_:_:_:_:_:).md)
- [static func buildBlock<A0, A1, A2, A3, A4, A5, A6>(A0, A1, A2, A3, A4, A5, A6) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2, A3, A4, A5, A6)>](intentpredictionsbuilder/buildblock(_:_:_:_:_:_:_:).md)
- [static func buildBlock<A0, A1, A2, A3, A4, A5, A6, A7>(A0, A1, A2, A3, A4, A5, A6, A7) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2, A3, A4, A5, A6, A7)>](intentpredictionsbuilder/buildblock(_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<A0, A1, A2, A3, A4, A5, A6, A7, A8>(A0, A1, A2, A3, A4, A5, A6, A7, A8) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2, A3, A4, A5, A6, A7, A8)>](intentpredictionsbuilder/buildblock(_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<A0, A1, A2, A3, A4, A5, A6, A7, A8, A9>(A0, A1, A2, A3, A4, A5, A6, A7, A8, A9) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2, A3, A4, A5, A6, A7, A8, A9)>](intentpredictionsbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10>(A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10)>](intentpredictionsbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11>(A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11)>](intentpredictionsbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12>(A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12)>](intentpredictionsbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13>(A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13)>](intentpredictionsbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14>(A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14)>](intentpredictionsbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildExpression<A0>(A0) -> A0](intentpredictionsbuilder/buildexpression(_:).md)

## See Also

- [static var predictionConfiguration: Self.Prediction](predictableintent/predictionconfiguration.md)
  A collection of predictions the system can use when it suggests the app intent.
- [associatedtype Prediction : IntentPredictionConfiguration](predictableintent/prediction.md)
- [protocol IntentPredictionConfiguration](intentpredictionconfiguration.md)
  An interface that provides the configuration for a single prediction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentpredictionsbuilder)*