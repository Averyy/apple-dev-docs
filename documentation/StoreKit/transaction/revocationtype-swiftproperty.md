# revocationType

**Framework**: StoreKit  
**Kind**: property

The type of refund or revocation that applies to the transaction.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
let revocationType: Transaction.RevocationType?
```

#### Discussion

This property indicates whether the transaction has a full refund, a prorated refund, or is revoked from Family Sharing. This property is `nil` for transactions that are not revoked.

> **Note**: This property is not present for Advanced Commerce transactions, which use [`refunds`](transaction/advancedcommerceinfo-swift.struct/item/refunds.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.property)*