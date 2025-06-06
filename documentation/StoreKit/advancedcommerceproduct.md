# AdvancedCommerceProduct

**Framework**: StoreKit  
**Kind**: struct

A product configured as a generic SKU in App Store Connect for use with the Advanced Commerce API.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
struct AdvancedCommerceProduct
```

## Topics

### Getting the product ID and type
- [let id: AdvancedCommerceProduct.ID](advancedcommerceproduct/id.md)
  The generic product ID.
- [AdvancedCommerceProduct.ProductType](advancedcommerceproduct/producttype.md)
- [let type: AdvancedCommerceProduct.ProductType](advancedcommerceproduct/type.md)
  The type of the product.
### Initiating purchases
- [AdvancedCommerceProduct.PurchaseOption](advancedcommerceproduct/purchaseoption.md)
- [func purchase(compactJWS: String, confirmIn: NSWindow, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](advancedcommerceproduct/purchase(compactjws:confirmin:options:)-7x4bh.md)
  Processes a purchase for the product.
- [func purchase(compactJWS: String, confirmIn: UIViewController, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](advancedcommerceproduct/purchase(compactjws:confirmin:options:)-54lkw.md)
  Processes a purchase for the product.
- [func purchase(compactJWS: String, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](advancedcommerceproduct/purchase(compactjws:options:).md)
  Processes a purchase for the product.
- [AdvancedCommerceProduct.PurchaseResult](advancedcommerceproduct/purchaseresult.md)
### Getting transactions and entitlements
- [var allTransactions: Transaction.Transactions](advancedcommerceproduct/alltransactions.md)
  All transactions associated with the generic product ID.
- [var currentEntitlements: Transaction.Transactions](advancedcommerceproduct/currententitlements.md)
  The transactions that entitle the customer to Advanced Commerce Items purchased using the generic product ID.
- [var latestTransaction: VerificationResult<Transaction>?](advancedcommerceproduct/latesttransaction.md)
  The most recent transaction associated with the generic product ID, if it exists.
### Initializing an instance
- [init(id: AdvancedCommerceProduct.ID) async throws](advancedcommerceproduct/init(id:).md)
  Creates an Advanced Commerce product.
### Handling errors
- [struct InvalidRequestError](invalidrequesterror.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Sending Advanced Commerce API requests from your app](sending-advanced-commerce-api-requests-from-your-app.md)
  Send Advanced Commerce API requests from your app that you authorize with a JSON Web Signature (JWS) you generate on your server.
- [Generating JWS to sign App Store requests](generating-jws-to-sign-app-store-requests.md)
  Create signed JSON Web Signature (JWS) strings on your server to authorize your API requests in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/advancedcommerceproduct)*