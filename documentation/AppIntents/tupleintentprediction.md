# TupleIntentPrediction

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

A type that represents a collection of predictions for a specific app intent.

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
struct TupleIntentPrediction<Intent, T> where Intent : AppIntent
```

## Relationships

### Conforms To
- [IntentPredictionConfiguration](./intentpredictionconfiguration.md)

## See Also

### Building predictions
- [static func buildBlock<A0>(A0) -> A0](./intentpredictionsbuilder/buildblock%28_%29.md)
- [static func buildBlock<A0, A1>(A0, A1) -> TupleIntentPrediction<A0.Intent, (A0, A1)>](./intentpredictionsbuilder/buildblock%28_,_%29.md)
- [static func buildBlock<A0, A1, A2>(A0, A1, A2) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2)>](./intentpredictionsbuilder/buildblock%28_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/tupleintentprediction)*