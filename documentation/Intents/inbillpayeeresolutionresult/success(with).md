# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified value.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class func success(with resolvedBillPayee: INBillPayee) -> Self
```

```objc
+ (instancetype) successWithResolvedBillPayee:(INBillPayee *) resolvedBillPayee;
```

#### Return Value

A new [`INBillPayeeResolutionResult`](../inbillpayeeresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you’re able to resolve the parameter successfully to a recognizable value in your app.

## Parameters

- `resolvedBillPayee`: The value that resolves the requested value of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INBillPayee?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [INBillPayee]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbillpayeeresolutionresult/success(with:))*