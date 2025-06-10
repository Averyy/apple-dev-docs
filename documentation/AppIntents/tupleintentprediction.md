# TupleIntentPrediction

**Framework**: App Intents  
**Kind**: struct

A type that represents a collection of predictions for a specific app intent.

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
struct TupleIntentPrediction<Intent, T> where Intent : AppIntent
```

## Relationships

### Conforms To
- [IntentPredictionConfiguration](intentpredictionconfiguration.md)

## See Also

- [static func buildBlock<A0>(A0) -> A0](intentpredictionsbuilder/buildblock(_:).md)
- [static func buildBlock<A0, A1>(A0, A1) -> TupleIntentPrediction<A0.Intent, (A0, A1)>](intentpredictionsbuilder/buildblock(_:_:).md)
- [static func buildBlock<A0, A1, A2>(A0, A1, A2) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2)>](intentpredictionsbuilder/buildblock(_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/tupleintentprediction)*