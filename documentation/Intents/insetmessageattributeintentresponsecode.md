# INSetMessageAttributeIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the response state.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum INSetMessageAttributeIntentResponseCode
```

```c
enum INSetMessageAttributeIntentResponseCode : NSInteger;
```

## Topics

### Response State
- [INSetMessageAttributeIntentResponseCode.unspecified](./insetmessageattributeintentresponsecode/unspecified.md)
  An unknown response code.
- [INSetMessageAttributeIntentResponseCode.ready](./insetmessageattributeintentresponsecode/ready.md)
  The app is ready to handle the intent.
- [INSetMessageAttributeIntentResponseCode.inProgress](./insetmessageattributeintentresponsecode/inprogress.md)
  You are ready to handle the intent.
- [INSetMessageAttributeIntentResponseCode.success](./insetmessageattributeintentresponsecode/success.md)
  You successfully handled the intent.
- [INSetMessageAttributeIntentResponseCode.failure](./insetmessageattributeintentresponsecode/failure.md)
  You are unable to modify the messages.
- [INSetMessageAttributeIntentResponseCode.failureRequiringAppLaunch](./insetmessageattributeintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to modify the messages.
- [INSetMessageAttributeIntentResponseCode.failureMessageNotFound](./insetmessageattributeintentresponsecode/failuremessagenotfound.md)
  One or more of the specified messages were not found.
- [INSetMessageAttributeIntentResponseCode.failureMessageAttributeNotSet](./insetmessageattributeintentresponsecode/failuremessageattributenotset.md)
  The message attributes couldn’t be modified.
### Initializers
- [init?(rawValue: Int)](./insetmessageattributeintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INSetMessageAttributeIntentResponseCode](./insetmessageattributeintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintentresponsecode)*