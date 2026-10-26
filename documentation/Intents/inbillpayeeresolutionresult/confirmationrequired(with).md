# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class func confirmationRequired(with billPayeeToConfirm: INBillPayee?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithBillPayeeToConfirm:(INBillPayee *) billPayeeToConfirm;
```

#### Return Value

A new [`INBillPayeeResolutionResult`](../inbillpayeeresolutionresult.md) object.

#### Discussion

Use this method when you can resolve the parameter to a single value but want the user to confirm that value.

## Parameters

- `billPayeeToConfirm`: The value that resolves the request, for the user to confirm.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INBillPayee) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified value.
- [class func disambiguation(with: [INBillPayee]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbillpayeeresolutionresult/confirmationrequired(with:))*