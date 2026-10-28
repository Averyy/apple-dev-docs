# INBillTypeResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the types of bills a user might pay.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INBillTypeResolutionResult
```

```objc
@interface INBillTypeResolutionResult : INIntentResolutionResult
```

## Overview

You create [`INBillTypeResolutionResult`](./inbilltyperesolutionresult.md) objects when resolving intent parameters containing a value of type [`INBillType`](./inbilltype.md). Use the creation method that best reflects your ability to resolve the parameter. For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INBillType) -> Self](./inbilltyperesolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified attribute.
- [class func confirmationRequired(with: INBillType) -> Self](./inbilltyperesolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [+ successWithResolvedValue:](./inbilltyperesolutionresult/successwithresolvedvalue_.md)
  Creates an object whose resolution involves the successful matching of the specified attribute.
- [+ confirmationRequiredWithValueToConfirm:](./inbilltyperesolutionresult/confirmationrequiredwithvaluetoconfirm_.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.

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

### Bill Data Objects
- [class INBillDetails](./inbilldetails.md)
  The detailed information associated with a bill.
- [class INBillPayee](./inbillpayee.md)
  The entity that receives the proceeds from a bill payment.
- [class INBillPayeeResolutionResult](./inbillpayeeresolutionresult.md)
  A resolution result for the recipient of a bill payment.
- [class INVisualCodeTypeResolutionResult](./invisualcodetyperesolutionresult.md)
  A resolution result for the type of visual code used to exchange information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbilltyperesolutionresult)*