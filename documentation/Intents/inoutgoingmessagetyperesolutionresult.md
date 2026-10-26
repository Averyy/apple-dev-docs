# INOutgoingMessageTypeResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the message’s format.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class INOutgoingMessageTypeResolutionResult
```

```objc
@interface INOutgoingMessageTypeResolutionResult : INIntentResolutionResult
```

#### Overview

Return an [`INOutgoingMessageTypeResolutionResult`](./inoutgoingmessagetyperesolutionresult.md) when you resolve an [`INOutgoingMessageType`](./inoutgoingmessagetype.md) parameter. Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result
- [class func success(with: INOutgoingMessageType) -> Self](./inoutgoingmessagetyperesolutionresult/success%28with%29.md)
  Creates an object with a resolution that involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INOutgoingMessageType) -> Self](./inoutgoingmessagetyperesolutionresult/confirmationrequired%28with%29.md)
  Creates an object with a resolution that requires the user to confirm the value before proceeding.

## Relationships

### Inherits From
- [INIntentResolutionResult](./inintentresolutionresult.md)
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
- [class INSendMessageRecipientResolutionResult](./insendmessagerecipientresolutionresult.md)
  A resolution result for the recipient of a message.
- [class INPersonResolutionResult](./inpersonresolutionresult.md)
  A resolution result for a user as a parameter of an intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inoutgoingmessagetyperesolutionresult)*