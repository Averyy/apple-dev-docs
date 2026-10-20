# buildBlock(_:_:_:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
static func buildBlock<A0, A1, A2>(_ a0: A0, _ a1: A1, _ a2: A2) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2)> where Intent == A0.Intent, A0 : IntentPredictionConfiguration, A1 : IntentPredictionConfiguration, A2 : IntentPredictionConfiguration, A0.Intent == A1.Intent, A1.Intent == A2.Intent
```

Available when `Intent` conforms to `AppIntent`.

## See Also

### Building predictions
- [static func buildBlock<A0>(A0) -> A0](./buildblock%28_%29.md)
- [static func buildBlock<A0, A1>(A0, A1) -> TupleIntentPrediction<A0.Intent, (A0, A1)>](./buildblock%28_,_%29.md)
- [struct TupleIntentPrediction](../tupleintentprediction.md)
  A type that represents a collection of predictions for a specific app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentpredictionsbuilder/buildblock(_:_:_:))*