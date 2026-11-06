# apple

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

An invitation model in which Apple hosts the invitations.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
static let apple: Transaction.MultiSeatInfo.InvitationManagement
```

## Discussion

The group purchaser invites people by using the invitation sheet that the system presents, or in Manage Subscriptions. Each person who joins gets their own transaction, with an ownership type of [`assigned`](../../ownershiptype-swift.struct/assigned.md).

For more information, see [Supporting multiseat purchases in your app](../../../supporting-multiseat-purchases-in-your-app.md).

## See Also

### Identifying the invitation model
- [static let developer: Transaction.MultiSeatInfo.InvitationManagement](./developer.md)
  An invitation model in which you host the invitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/multiseatinfo-swift.struct/invitationmanagement-swift.struct/apple)*