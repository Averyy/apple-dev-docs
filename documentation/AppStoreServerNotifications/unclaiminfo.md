# unclaimInfo

**Framework**: App Store Server Notifications  
**Kind**: dictionary  
**Role**: Object

The payload data that identifies the seat claims the App Store unclaimed in a group subscription that uses developer-hosted invitations.

**Availability**:
- App Store Server Notifications 2.23+

## Declaration

```
object unclaimInfo
```

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)

## Discussion

The [`responseBodyV2DecodedPayload`](./responsebodyv2decodedpayload.md) contains an `unclaimInfo` object when the [`notificationType`](./notificationtype.md) is `UNCLAIM_SEATS`. This notification applies only to subscriptions with an [`invitationManagement`](./invitationmanagement.md) value of `DEVELOPER`.

The App Store already unclaimed the seats that the `unclaimSeatIds` array identifies. Each identifier is a seat claim identifier that the [`Claim Seat`](../AppStoreServerAPI/claim-seat.md) endpoint returned to you. When you receive this notification, revoke access for the customers you assigned to those seats.

The following example shows the decoded payload of an `UNCLAIM_SEATS` notification:

```json
{
  "notificationType": "UNCLAIM_SEATS",
  "notificationUUID": "3e7d9a4c-0b6f-4c9b-9a4e-6d2f1c8b5a70",
  "unclaimInfo": {
    "appAppleId": 1234567890,
    "bundleId": "com.example",
    "environment": "Production",
    "originalTransactionId": "12345",
    "unclaimSeatIds": [
      "8a1f3c2e-5b7d-4e9a-b6c4-2d8f0e1a3b5c",
      "c4e6a8b0-2d4f-4a6c-8e0b-1a3c5e7f9b2d"
    ]
  },
  "version": "2.0",
  "signedDate": 1735718400000
}
```

## Topics

### Seat identifiers
- unclaimSeatIds

## Properties

- `appAppleId` (appAppleId): The unique identifier of the app that the notification applies to.
- `bundleId` (bundleId): The bundle identifier of the app.
- `environment` (environment): The server environment that the notification applies to, either sandbox or production.
- `originalTransactionId` (originalTransactionId): The original transaction identifier of the group purchaser’s subscription.
- `unclaimSeatIds` (unclaimSeatIds): An array of the identifiers of the seat claims that the App Store unclaimed.

## See Also

### Response objects for in-app purchases
- [object summary](./summary.md)
  The payload data for a subscription-renewal-date extension notification.
- [object data](./data.md)
  The payload data that contains app metadata and the signed renewal and transaction information.
- [object appData](./appdata.md)
  The object that contains the app metadata and signed app transaction information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/unclaiminfo)*