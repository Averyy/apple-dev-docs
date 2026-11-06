# assigned

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

The transaction belongs to a customer who has access through an organization or group.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 27.0, macOS 27.0, tvOS 27.0, watchOS 27.0, visionOS 27.0)
static var assigned: Transaction.OwnershipType { get }
```

## Mentions

- [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md)
- [Testing multiseat subscriptions](../../testing-multiseat-subscriptions.md)

## Discussion

A customer has access through an organization when the organization assigns the subscription to them through Volume Purchasing, in Apple Business or Apple School Manager. A customer has access through a group when they join the group of a multiseat subscription that uses Apple-hosted invitations. Subscriptions that use developer-hosted invitations don’t create transactions for the people who join the group.

An assigned transaction mirrors the group purchaser’s transaction under its own transaction identifier, and doesn’t include an [`appAccountToken`](../appaccounttoken.md). If the customer loses access through the organization or group, the transaction’s [`revocationType`](../revocationtype-swift.property.md) is [`assignmentRevocation`](../revocationtype-swift.struct/assignmentrevocation.md).

For more information, see [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md).

## See Also

### Getting ownership types
- [static let familyShared: Transaction.OwnershipType](./familyshared.md)
  The transaction belongs to a family member who benefits from the service.
- [static let purchased: Transaction.OwnershipType](./purchased.md)
  The transaction belongs to the purchaser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/ownershiptype-swift.struct/assigned)*