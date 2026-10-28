# INSendRideFeedbackIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You successfully recorded the feedback for the ride.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case success
```

```c
INSendRideFeedbackIntentResponseCodeSuccess
```

## Discussion

Use this code during the handling phase to indicate that your ride service recorded the feedback for the ride. You can also specify this code during the confirmation phase to indicate that you are ready to handle the intent.

## See Also

### Constants
- [INSendRideFeedbackIntentResponseCode.unspecified](./unspecified.md)
  There is no specified response code.
- [INSendRideFeedbackIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INSendRideFeedbackIntentResponseCode.failure](./failure.md)
  You were unable to record the feedback for the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendridefeedbackintentresponsecode/success)*