# unsupported(forReason:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution indicates that your app can’t use the specified person as a message recipient.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func unsupported(forReason reason: INSendMessageRecipientUnsupportedReason) -> Self
```

```objc
+ (instancetype) unsupportedForReason:(INSendMessageRecipientUnsupportedReason) reason;
```

#### Return Value

A new resolution result object.

#### Discussion

Use this method when a problem with the recipient’s account would prevent you from sending the message. When you return a resolution of this type, Siri prompts the user to provide a new recipient, which you must then resolve. The cycle of prompting the user and asking you to resolve the parameter continues until you resolve the parameter successfully.

## Parameters

- `reason`: The reason why the recipient is not supported. For a list of possible values, see [`INSendMessageRecipientUnsupportedReason`](../insendmessagerecipientunsupportedreason.md).

## See Also

### Creating a Resolution Result Object
- [enum INSendMessageRecipientUnsupportedReason](../insendmessagerecipientunsupportedreason.md)
  Constants indicating the reason why a recipient is not supported.
- [init(personResolutionResult: INPersonResolutionResult)](./init%28personresolutionresult%29.md)
  Creates a resolution result object with the specified person resolution result object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessagerecipientresolutionresult/unsupported(forreason:))*