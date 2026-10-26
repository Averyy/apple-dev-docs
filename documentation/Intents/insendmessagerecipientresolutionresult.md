# INSendMessageRecipientResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the recipient of a message.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class INSendMessageRecipientResolutionResult
```

```objc
@interface INSendMessageRecipientResolutionResult : INPersonResolutionResult
```

#### Overview

An [`INSendMessageRecipientResolutionResult`](./insendmessagerecipientresolutionresult.md) object is what you return when resolving parameters containing an [`INPerson`](./inperson.md) object. Use the [`unsupported(forReason:)`](./insendmessagerecipientresolutionresult/unsupported%28forreason%29.md) method to provide additional context about why a recipient was invalid. Otherwise, use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution options, see [`INPersonResolutionResult`](./inpersonresolutionresult.md) and [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func unsupported(forReason: INSendMessageRecipientUnsupportedReason) -> Self](./insendmessagerecipientresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution indicates that your app can’t use the specified person as a message recipient.
- [enum INSendMessageRecipientUnsupportedReason](./insendmessagerecipientunsupportedreason.md)
  Constants indicating the reason why a recipient is not supported.
- [init(personResolutionResult: INPersonResolutionResult)](./insendmessagerecipientresolutionresult/init%28personresolutionresult%29.md)
  Creates a resolution result object with the specified person resolution result object.

## Relationships

### Inherits From
- [INPersonResolutionResult](./inpersonresolutionresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Providing Resolution Results
- [class INMessageAttributeResolutionResult](./inmessageattributeresolutionresult.md)
  A resolution result for assorted attributes of a message.
- [class INMessageAttributeOptionsResolutionResult](./inmessageattributeoptionsresolutionresult.md)
  A resolution result for a search parameter that filters by message status.
- [class INDateComponentsRangeResolutionResult](./indatecomponentsrangeresolutionresult.md)
  A resolution result for a range of dates in a parameter of an intent.
- [class INPersonResolutionResult](./inpersonresolutionresult.md)
  A resolution result for a user as a parameter of an intent.
- [class INOutgoingMessageTypeResolutionResult](./inoutgoingmessagetyperesolutionresult.md)
  A resolution result for the message’s format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessagerecipientresolutionresult)*