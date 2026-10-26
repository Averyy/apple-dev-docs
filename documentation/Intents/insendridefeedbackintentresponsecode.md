# INSendRideFeedbackIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum INSendRideFeedbackIntentResponseCode
```

```c
enum INSendRideFeedbackIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INSendRideFeedbackIntentResponseCode.unspecified](./insendridefeedbackintentresponsecode/unspecified.md)
  There is no specified response code.
- [INSendRideFeedbackIntentResponseCode.ready](./insendridefeedbackintentresponsecode/ready.md)
  You are ready to handle the intent.
- [INSendRideFeedbackIntentResponseCode.success](./insendridefeedbackintentresponsecode/success.md)
  You successfully recorded the feedback for the ride.
- [INSendRideFeedbackIntentResponseCode.failure](./insendridefeedbackintentresponsecode/failure.md)
  You were unable to record the feedback for the ride.
### Initializers
- [init?(rawValue: Int)](./insendridefeedbackintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INSendRideFeedbackIntentResponseCode](./insendridefeedbackintentresponse/code.md)
  The code indicating whether your app successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendridefeedbackintentresponsecode)*