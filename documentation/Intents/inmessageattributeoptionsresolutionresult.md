# INMessageAttributeOptionsResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for a search parameter that filters by message status.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INMessageAttributeOptionsResolutionResult
```

```objc
@interface INMessageAttributeOptionsResolutionResult : INIntentResolutionResult
```

## Overview

You create [`INMessageAttributeOptionsResolutionResult`](./inmessageattributeoptionsresolutionresult.md) objects when resolving intent parameters containing a value of type [`INMessageAttributeOptions`](./inmessageattributeoptions.md). Use the creation method that best reflects your ability to resolve the parameter. For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INMessageAttributeOptions) -> Self](./inmessageattributeoptionsresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified attribute.
- [class func confirmationRequired(with: INMessageAttributeOptions) -> Self](./inmessageattributeoptionsresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [+ successWithResolvedValue:](./inmessageattributeoptionsresolutionresult/successwithresolvedvalue_.md)
- [+ confirmationRequiredWithValueToConfirm:](./inmessageattributeoptionsresolutionresult/confirmationrequiredwithvaluetoconfirm_.md)

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
- [class INDateComponentsRangeResolutionResult](./indatecomponentsrangeresolutionresult.md)
  A resolution result for a range of dates in a parameter of an intent.
- [class INSendMessageRecipientResolutionResult](./insendmessagerecipientresolutionresult.md)
  A resolution result for the recipient of a message.
- [class INPersonResolutionResult](./inpersonresolutionresult.md)
  A resolution result for a user as a parameter of an intent.
- [class INOutgoingMessageTypeResolutionResult](./inoutgoingmessagetyperesolutionresult.md)
  A resolution result for the message’s format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessageattributeoptionsresolutionresult)*