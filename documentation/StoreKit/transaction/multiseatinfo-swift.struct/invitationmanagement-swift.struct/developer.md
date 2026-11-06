# developer

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

An invitation model in which you host the invitations.

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
static let developer: Transaction.MultiSeatInfo.InvitationManagement
```

## Discussion

You control the invitation experience and manage who has access to the service in your app. Group members don’t get their own transactions. To manage the subscription’s seats, use the seat endpoints of the [App Store Server API](../../../../AppStoreServerAPI/AppStoreServerAPI.md).

For more information, see [Hosting group invitations in your app](../../../hosting-group-invitations-in-your-app.md).

## See Also

### Identifying the invitation model
- [static let apple: Transaction.MultiSeatInfo.InvitationManagement](./apple.md)
  An invitation model in which Apple hosts the invitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/multiseatinfo-swift.struct/invitationmanagement-swift.struct/developer)*