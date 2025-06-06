# externalPurchaseToken

**Framework**: App Store Server Notifications  
**Kind**: dictionary

The payload data that contains an external purchase token.

**Availability**:
- App Store Server Notifications 2.10+

## Declaration

```swift
object externalPurchaseToken
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)
- [Receiving App Store Server Notifications](receiving-app-store-server-notifications.md)

#### Discussion

The `externalPurchaseToken` object is part of the [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md). It’s present in the payload when the [`notificationType`](notificationtype.md) is `EXTERNAL_PURCHASE_TOKEN`. This notification type applies to apps that use the [`External Purchase`](https://developer.apple.com/documentation/StoreKit/external-purchase) API to offer alternative payment options.

This notification indicates that Apple didn’t receive a report for the token within the time period specified in the [`Commission, transaction reports, and payments`](https://developer.apple.comhttps://developer.apple.com/support/apps-using-alternative-payment-providers-in-the-eu/#commission-reports-and-payments) section of the article Using alternative payment options on the App Store in the European Union. To report tokens with or without associated transactions, call the [`Send External Purchase Report`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI/Send-External-Purchase-Report) endpoint of the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI) from your server.

The `externalPurchaseToken` object in the notification payload is the Base64URL-decoded JSON of the external purchase token your app or website receive when your customer initiates an external purchase. For more information on the external purchase token, see [`Receiving and decoding external purchase tokens`](https://developer.apple.com/documentation/StoreKit/receiving-and-decoding-external-purchase-tokens).

## Topics

### External purchase token fields
- [type externalPurchaseId](externalpurchaseid.md)
  The field of an external purchase token that uniquely identifies the token.
- [type tokenCreationDate](tokencreationdate.md)
  The field of an external purchase token that contains the UNIX date, in milliseconds, when the system created the token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/externalpurchasetoken)*