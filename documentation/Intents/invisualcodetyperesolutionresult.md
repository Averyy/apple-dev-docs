# INVisualCodeTypeResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the type of visual code used to exchange information.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INVisualCodeTypeResolutionResult
```

```objc
@interface INVisualCodeTypeResolutionResult : INIntentResolutionResult
```

## Overview

An [`INVisualCodeTypeResolutionResult`](./invisualcodetyperesolutionresult.md) object is what you return when resolving parameters containing an [`INVisualCodeType`](./invisualcodetype.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INVisualCodeType) -> Self](./invisualcodetyperesolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified value.
- [class func confirmationRequired(with: INVisualCodeType) -> Self](./invisualcodetyperesolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user confirm the value before proceeding.

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
- [class INBillTypeResolutionResult](./inbilltyperesolutionresult.md)
  A resolution result for the types of bills a user might pay.
- [class INBillPayeeResolutionResult](./inbillpayeeresolutionresult.md)
  A resolution result for the recipient of a bill payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invisualcodetyperesolutionresult)*