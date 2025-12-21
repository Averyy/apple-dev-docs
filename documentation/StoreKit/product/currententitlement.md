# currentEntitlement

**Framework**: StoreKit  
**Kind**: property

The transaction that entitles the user to the product.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var currentEntitlement: VerificationResult<Transaction>? { get async }
```

#### Discussion

This value is `nil` if the customer isn’t currently entitled to this product. Current entitlement information applies only to non-consumables, non-renewing subscriptions, and auto-renewable subscriptions. The following example checks the current entitlement for a product.

```swift
guard let verificationResult = await product.currentEntitlement else {
    // The user isn’t currently entitled to this product.
    return
}

switch verificationResult {
case .verified(let transaction):
    // Check the transaction and give the user access to purchased 
    // content as appropriate.
    ...
case .unverified(let transaction, let verificationError):
    // Handle unverified transactions based 
    // on your business model.
    ...
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/currententitlement)*