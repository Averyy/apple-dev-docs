# Product.PurchaseResult

**Framework**: StoreKit  
**Kind**: enum

The result of a purchase.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum PurchaseResult
```

#### Overview

The value of the purchase result represents the state of the purchase. When successful, the associated value contains a [`VerificationResult`](verificationresult.md) of the transaction. The following example illustrates calling [`purchase(options:)`](product/purchase(options:).md) on a [`Product`](product.md) value, checking the purchase status, and inspecting information about a successful transaction.

```swift
let result = try await product.purchase()
switch result {
case .success(let verificationResult):
    switch verificationResult {
    case .verified(let transaction):
        // Give the user access to purchased content.
        ...
        // Complete the transaction after providing
        // the user access to the content.
        await transaction.finish()
    case .unverified(let transaction, let verificationError):
        // Handle unverified transactions based 
        // on your business model.
        ...
    }
case .pending:
    // The purchase requires action from the customer. 
    // If the transaction completes, 
    // it's available through Transaction.updates.
    break
case .userCancelled:
    // The user canceled the purchase.
    break
@unknown default:
    break
}

```

## Topics

### Getting the Purchase Results
- [case success(VerificationResult<Transaction>)](product/purchaseresult/success(_:).md)
  The purchase succeeded and results in a transaction.
- [Product.PurchaseResult.userCancelled](product/purchaseresult/usercancelled.md)
  The user canceled the purchase.
- [Product.PurchaseResult.pending](product/purchaseresult/pending.md)
  The purchase is pending, and requires action from the customer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PurchaseAction](purchaseaction.md)
  An action that starts an In-App Purchase.
- [func purchase(options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(options:).md)
  Initiates a purchase for the product with the App Store and displays the confirmation sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseresult)*