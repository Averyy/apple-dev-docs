# INDateComponentsRangeResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for a range of dates in a parameter of an intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INDateComponentsRangeResolutionResult
```

```objc
@interface INDateComponentsRangeResolutionResult : INIntentResolutionResult
```

#### Overview

An [`INDateComponentsRangeResolutionResult`](./indatecomponentsrangeresolutionresult.md) object is what you return when resolving parameters containing an [`INDateComponentsRange`](./indatecomponentsrange.md) object. Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INDateComponentsRange) -> Self](./indatecomponentsrangeresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INDateComponentsRange?) -> Self](./indatecomponentsrangeresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [INDateComponentsRange]) -> Self](./indatecomponentsrangeresolutionresult/disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.

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
- [class INSendMessageRecipientResolutionResult](./insendmessagerecipientresolutionresult.md)
  A resolution result for the recipient of a message.
- [class INPersonResolutionResult](./inpersonresolutionresult.md)
  A resolution result for a user as a parameter of an intent.
- [class INOutgoingMessageTypeResolutionResult](./inoutgoingmessagetyperesolutionresult.md)
  A resolution result for the message’s format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatecomponentsrangeresolutionresult)*