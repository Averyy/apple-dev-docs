# buildBlock(_:_:_:_:_:_:_:_:_:_:_:_:)

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
static func buildBlock<A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11>(_ a0: A0, _ a1: A1, _ a2: A2, _ a3: A3, _ a4: A4, _ a5: A5, _ a6: A6, _ a7: A7, _ a8: A8, _ a9: A9, _ a10: A10, _ a11: A11) -> TupleIntentPrediction<A0.Intent, (A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11)> where Intent == A0.Intent, A0 : IntentPredictionConfiguration, A1 : IntentPredictionConfiguration, A2 : IntentPredictionConfiguration, A3 : IntentPredictionConfiguration, A4 : IntentPredictionConfiguration, A5 : IntentPredictionConfiguration, A6 : IntentPredictionConfiguration, A7 : IntentPredictionConfiguration, A8 : IntentPredictionConfiguration, A9 : IntentPredictionConfiguration, A10 : IntentPredictionConfiguration, A11 : IntentPredictionConfiguration, A0.Intent == A1.Intent, A1.Intent == A2.Intent, A2.Intent == A3.Intent, A3.Intent == A4.Intent, A4.Intent == A5.Intent, A5.Intent == A6.Intent, A6.Intent == A7.Intent, A7.Intent == A8.Intent, A8.Intent == A9.Intent, A9.Intent == A10.Intent, A10.Intent == A11.Intent
```

Available when `Intent` conforms to `AppIntent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentpredictionsbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:))*