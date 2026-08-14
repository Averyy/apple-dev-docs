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

The `externalPurchaseToken` object is part of the [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md). It’s present in the payload when the [`notificationType`](notificationtype.md) is `EXTERNAL_PURCHASE_TOKEN`. This notification type applies to apps that use the [`External Purchase`](https://developer.apple.com/documentation/storekit/external-purchase) API to offer alternative payment options.

The `externalPurchaseToken` object is the Base64URL-decoded JSON of the external purchase token your app or website receives when your customer initiates an external purchase. For more information on external purchase tokens, see [`Receiving and decoding external purchase tokens`](https://developer.apple.com/documentation/storekit/receiving-and-decoding-external-purchase-tokens).

To report tokens with or without associated transactions, call the [`Send External Purchase Report`](https://developer.apple.com/documentation/externalpurchaseserverapi/send-external-purchase-report) endpoint of the [`External Purchase Server API`](https://developer.apple.com/documentation/externalpurchaseserverapi) from your server.

## Topics

### External purchase token fields
- [type externalPurchaseId](externalpurchaseid.md)
  The field of an external purchase token that uniquely identifies the token.
- [type tokenCreationDate](tokencreationdate.md)
  The field of an external purchase token that contains the UNIX date, in milliseconds, when the system created the token.
- [type tokenExpirationDate](tokenexpirationdate.md)
  The field of a custom link token that contains the UNIX date, in milliseconds, when the token expires.
- [type tokenType](tokentype.md)
  The type of an external purchase custom link token.

## Properties

- `externalPurchaseId` (externalPurchaseId) *(required)*: The unique identifier of the token. Use this value to report tokens and their associated transactions in the [`Send External Purchase Report`](https://developer.apple.com/documentation/externalpurchaseserverapi/send-external-purchase-report) endpoint.
- `tokenCreationDate` (tokenCreationDate) *(required)*: The UNIX time, in milliseconds, when the system created the token.
- `appAppleId` (appAppleId) *(required)*: The app Apple ID for which the system generated the token.
- `bundleId` (bundleId) *(required)*: The bundle ID of the app for which the system generated the token.
- `tokenExpirationDate` (tokenExpirationDate): The UNIX time, in milliseconds, when a token expires. This field is present only for custom link tokens.
- `tokenType` (tokenType): The custom link token type, either `SERVICES` or `ACQUISITION`. This field is present only for custom link tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/externalpurchasetoken)*