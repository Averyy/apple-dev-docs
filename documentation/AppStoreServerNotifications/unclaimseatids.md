# unclaimSeatIds

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

The identifiers of the seat claims that the App Store unclaimed in a group subscription that uses developer-hosted invitations.

**Availability**:
- App Store Server Notifications 2.23+

## Declaration

```
[uuid] unclaimSeatIds
```

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)

## Discussion

Each value in this array is a UUID that identifies a seat claim you made. The [`Claim Seat`](../AppStoreServerAPI/claim-seat.md) endpoint returns this identifier when you claim a seat.

The [`unclaimInfo`](./unclaiminfo.md) object contains this array when the [`notificationType`](./notificationtype.md) is `UNCLAIM_SEATS`. Revoke access for the customers you assigned to these seats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/unclaimseatids)*