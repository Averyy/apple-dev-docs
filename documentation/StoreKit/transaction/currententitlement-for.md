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

- [static func currentEntitlements(for: String) -> Transaction.Transactions](transaction/currententitlements(for:).md)
  Gets the transactions that entitle the user to items purchased under a product ID.
- [var offerPeriodStringRepresentation: String?](transaction/offerperiodstringrepresentation.md)
  The string representation of the offer period applied to the subscription offer for this transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/currententitlement(for:))*