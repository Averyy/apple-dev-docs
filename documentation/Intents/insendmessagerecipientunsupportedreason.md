# INSendMessageRecipientUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the reason why a recipient is not supported.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum INSendMessageRecipientUnsupportedReason
```

```c
enum INSendMessageRecipientUnsupportedReason : NSInteger;
```

## Topics

### Enumeration Cases
- [INSendMessageRecipientUnsupportedReason.noAccount](./insendmessagerecipientunsupportedreason/noaccount.md)
  A recipient without an account.
- [INSendMessageRecipientUnsupportedReason.offline](./insendmessagerecipientunsupportedreason/offline.md)
  An offline recipient.
- [INSendMessageRecipientUnsupportedReason.messagingServiceNotEnabledForRecipient](./insendmessagerecipientunsupportedreason/messagingservicenotenabledforrecipient.md)
  A recipient for whom messaging is not enabled.
- [INSendMessageRecipientUnsupportedReason.noHandleForLabel](./insendmessagerecipientunsupportedreason/nohandleforlabel.md)
  A recipient for whom there is no handle for the provided label.
- [INSendMessageRecipientUnsupportedReason.noValidHandle](./insendmessagerecipientunsupportedreason/novalidhandle.md)
  A recipient for whom there is no valid handle.
- [INSendMessageRecipientUnsupportedReason.requestedHandleInvalid](./insendmessagerecipientunsupportedreason/requestedhandleinvalid.md)
  A recipient for whom the requested handle is invalid.
- [INSendMessageRecipientUnsupportedReason.requiringInAppAuthentication](./insendmessagerecipientunsupportedreason/requiringinappauthentication.md)
### Initializers
- [init?(rawValue: Int)](./insendmessagerecipientunsupportedreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Resolution Result Object
- [class func unsupported(forReason: INSendMessageRecipientUnsupportedReason) -> Self](./insendmessagerecipientresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution indicates that your app can’t use the specified person as a message recipient.
- [init(personResolutionResult: INPersonResolutionResult)](./insendmessagerecipientresolutionresult/init%28personresolutionresult%29.md)
  Creates a resolution result object with the specified person resolution result object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessagerecipientunsupportedreason)*