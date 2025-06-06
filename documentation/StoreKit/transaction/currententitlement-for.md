# currentEntitlement(for:)

**Framework**: StoreKit  
**Kind**: method

Gets the latest transactions that entitle the customer to a specified product.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func currentEntitlement(for productID: String) async -> VerificationResult<Transaction>?
```

#### Return Value

A [`VerificationResult`](verificationresult.md) or `nil` if the customer has no current In-App Purchases.

## Parameters

- `productID`: In-App Purchase product identifier.

## See Also

- [static var currentEntitlements: Transaction.Transactions](transaction/currententitlements.md)
  A sequence of the latest transactions that entitle a customer to In-App Purchases and subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/currententitlement(for:))*