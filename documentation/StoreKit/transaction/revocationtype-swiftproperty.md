# revocationType

**Framework**: StoreKit  
**Kind**: property

The type of revocation that occurred, or `nil` if the transaction was not revoked.

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

This property indicates whether the revocation was a family sharing revocation, a full refund, or a prorated refund. It is `nil` for transactions that have not been revoked.

> **Note**: This property is not present for Advanced Commerce transactions, which use [`refunds`](transaction/advancedcommerceinfo-swift.struct/item/refunds.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.property)*