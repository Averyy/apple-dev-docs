# Transaction.MultiSeatInfo.InvitationManagement

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Values that indicate whether Apple or you host the invitations for a multiseat subscription.

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
struct InvitationManagement
```

## Overview

With Apple-hosted invitations, the group purchaser invites people by using a sheet that the system presents, and each person who joins gets their own transaction. With developer-hosted invitations, you invite people and manage their access in your app, and you manage the subscription’s seats with the [App Store Server API](../../../AppStoreServerAPI/AppStoreServerAPI.md).

The raw values are `APPLE` and `DEVELOPER`, the same values that the App Store Server API uses.

To choose an invitation model, see [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md). For developer-hosted invitations, see [Hosting group invitations in your app](../../hosting-group-invitations-in-your-app.md).

## Topics

### Identifying the invitation model
- [static let apple: Transaction.MultiSeatInfo.InvitationManagement](./invitationmanagement-swift.struct/apple.md)
  An invitation model in which Apple hosts the invitations.
- [static let developer: Transaction.MultiSeatInfo.InvitationManagement](./invitationmanagement-swift.struct/developer.md)
  An invitation model in which you host the invitations.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the invitation model
- [let invitationManagement: Transaction.MultiSeatInfo.InvitationManagement](./invitationmanagement-swift.property.md)
  The invitation model of the multiseat subscription, either Apple-hosted or developer-hosted invitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/multiseatinfo-swift.struct/invitationmanagement-swift.struct)*