# assignmentRevocation

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

The customer no longer has access through an organization or group.

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
@backDeployed(before: iOS 27.0, macOS 27.0, tvOS 27.0, watchOS 27.0, visionOS 27.0)
static var assignmentRevocation: Transaction.RevocationType { get }
```

## Mentions

- [Managing the life cycle of multiseat subscriptions](../../managing-the-life-cycle-of-multiseat-subscriptions.md)
- [Testing multiseat subscriptions](../../testing-multiseat-subscriptions.md)
- [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md)

## Discussion

The App Store sets this value when the organization or group purchaser removes the subscription from the customer, when the customer leaves the group, or when a refund removes their seat. It applies to transactions with an ownership type of [`assigned`](../ownershiptype-swift.struct/assigned.md). When a transaction has this revocation type, revoke the customer’s access to the content that the transaction provides.

For more information, see [Managing the life cycle of multiseat subscriptions](../../managing-the-life-cycle-of-multiseat-subscriptions.md).

## See Also

### Getting revocation types
- [static let fullRefund: Transaction.RevocationType](./fullrefund.md)
  The transaction was fully refunded.
- [static let proratedRefund: Transaction.RevocationType](./proratedrefund.md)
  The transaction was partially refunded based on consumption.
- [static let familyRevocation: Transaction.RevocationType](./familyrevocation.md)
  The transaction was revoked due to a family sharing revocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.struct/assignmentrevocation)*