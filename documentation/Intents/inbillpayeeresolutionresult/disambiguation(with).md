# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class func disambiguation(with billPayeesToDisambiguate: [INBillPayee]) -> Self
```

```objc
+ (instancetype) disambiguationWithBillPayeesToDisambiguate:(NSArray<INBillPayee *> *) billPayeesToDisambiguate;
```

#### Return Value

A new [`INBillPayeeResolutionResult`](../inbillpayeeresolutionresult.md) object.

#### Discussion

Use this method when you can’t resolve the payee uniquely and need the user to select from a limited set of possible options.

## Parameters

- `billPayeesToDisambiguate`: An array of payee objects from which to select. Specify as few items as possible, and preferably no more than five.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INBillPayee) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified value.
- [class func confirmationRequired(with: INBillPayee?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbillpayeeresolutionresult/disambiguation(with:))*