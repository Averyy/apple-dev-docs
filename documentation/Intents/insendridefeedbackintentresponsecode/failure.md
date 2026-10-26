# INSendRideFeedbackIntentResponseCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You were unable to record the feedback for the ride.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case failure
```

```c
INSendRideFeedbackIntentResponseCodeFailure
```

#### Discussion

Use this code for both transient and unrecoverable errors that prevented you from recording the feedback for the ride.

## See Also

### Constants
- [INSendRideFeedbackIntentResponseCode.unspecified](./unspecified.md)
  There is no specified response code.
- [INSendRideFeedbackIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INSendRideFeedbackIntentResponseCode.success](./success.md)
  You successfully recorded the feedback for the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendridefeedbackintentresponsecode/failure)*