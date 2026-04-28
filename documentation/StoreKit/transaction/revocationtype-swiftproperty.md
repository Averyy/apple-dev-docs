# revocationType

**Framework**: StoreKit  
**Kind**: property

The type of refund or revocation that applies to the transaction.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
let revocationType: Transaction.RevocationType?
```

#### Discussion

This property indicates whether the transaction has a full refund, a prorated refund, or is revoked from Family Sharing. This property is `nil` for transactions that are not revoked.

> **Note**: This property is not present for Advanced Commerce transactions, which use [`refunds`](transaction/advancedcommerceinfo-swift.struct/item/refunds.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.property)*