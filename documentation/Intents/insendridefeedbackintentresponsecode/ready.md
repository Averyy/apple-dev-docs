# INSendRideFeedbackIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You are ready to handle the intent.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case ready
```

```c
INSendRideFeedbackIntentResponseCodeReady
```

#### Discussion

During the confirmation phase of an intent, use this code to signal that your Intents extension is ready and able to act on the intent.

## See Also

### Constants
- [INSendRideFeedbackIntentResponseCode.unspecified](./unspecified.md)
  There is no specified response code.
- [INSendRideFeedbackIntentResponseCode.success](./success.md)
  You successfully recorded the feedback for the ride.
- [INSendRideFeedbackIntentResponseCode.failure](./failure.md)
  You were unable to record the feedback for the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendridefeedbackintentresponsecode/ready)*