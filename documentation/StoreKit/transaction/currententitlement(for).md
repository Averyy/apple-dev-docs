# currentEntitlement(for:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Gets the latest transactions that entitle the customer to a specified product.

**Availability**:
- iOS 15.0+ - Deprecated in 18.4
- iPadOS 15.0+ - Deprecated in 18.4
- Mac Catalyst 15.0+ - Deprecated in 18.4
- macOS 12.0+ - Deprecated in 15.4
- tvOS 15.0+ - Deprecated in 18.4
- visionOS 1.0+ - Deprecated in 2.4
- watchOS 8.0+ - Deprecated in 11.4

> **Deprecated**: Use [`currentEntitlements`](./currententitlements.md) instead.

## Declaration

```swift
static func currentEntitlement(for productID: String) async -> VerificationResult<Transaction>?
```

#### Return Value

A [`VerificationResult`](../verificationresult.md) or `nil` if the customer has no current Apple In-App Purchases.

## Parameters

- `productID`: Apple In-App Purchase product identifier.

## See Also

### Deprecated
- [static func currentEntitlements(for: String) -> Transaction.Transactions](./currententitlements%28for%29.md)
  Gets the transactions that entitle the user to items purchased under a product ID.
- [var offerPeriodStringRepresentation: String?](./offerperiodstringrepresentation.md)
  The string representation of the offer period applied to the subscription offer for this transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/currententitlement(for:))*