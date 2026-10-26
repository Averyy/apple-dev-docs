# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func confirmationRequired(with balanceTypeToConfirm: INBalanceType) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithBalanceTypeToConfirm:(INBalanceType) balanceTypeToConfirm;
```

#### Return Value

A new [`INBalanceTypeResolutionResult`](../inbalancetyperesolutionresult.md) object.

#### Discussion

Use this method when you can resolve the balance type to a single value that is similar to the type specified by the user, but not exactly the same.

## Parameters

- `balanceTypeToConfirm`: The value that resolves the request but that must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INBalanceType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbalancetyperesolutionresult/confirmationrequired(with:))*