# invitationManagement

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The invitation model of the multiseat subscription, either Apple-hosted or developer-hosted invitations.

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
let invitationManagement: Transaction.MultiSeatInfo.InvitationManagement
```

## Mentions

- [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md)
- [Hosting group invitations in your app](../../hosting-group-invitations-in-your-app.md)

## Discussion

The value reflects the invitation model in effect when the subscription began. If you change how your app hosts invitations in App Store Connect, the change applies to new purchases and resubscriptions, and this value doesn’t change for existing subscriptions.

## See Also

### Getting the invitation model
- [Transaction.MultiSeatInfo.InvitationManagement](./invitationmanagement-swift.struct.md)
  Values that indicate whether Apple or you host the invitations for a multiseat subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/multiseatinfo-swift.struct/invitationmanagement-swift.property)*