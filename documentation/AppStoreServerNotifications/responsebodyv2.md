# responseBodyV2

**Framework**: App Store Server Notifications  
**Kind**: dictionary

The response body the App Store sends in a version 2 server notification.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
object responseBodyV2
```

## Mentions

- [Receiving App Store Server Notifications](receiving-app-store-server-notifications.md)
- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

#### Discussion

The `signedPayload` object is a JWS representation. To get the transaction and subscription renewal details from the notification payload, process the `signedPayload` as follows:

1. Parse `signedPayload` to identify the JWS header, payload, and signature representations.
2. Base64URL-decode the payload to get the [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md). The decoded payload contains details of the notification such as the notification type and  data.
3. The `data` object contains a `signedTransactionInfo` ([`JWSTransaction`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSTransaction)) and based on the notification type, a `signedRenewalInfo` ([`JWSRenewalInfo`](jwsrenewalinfo.md)). Parse and Base64URL-decode these signed JWS representations to get transaction and subscription renewal details.

Each of the signed JWS representations, `signedPayload`, `signedTransactionInfo`, and `signedRenewalInfo`, have a JWS signature that you can validate on your server. Use the algorithm specified in the header’s [`alg`](alg.md) parameter to validate the signature. For more information about validating signatures, see the JSON Web Signature (JWS) [`IETF RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515) specification.

## Topics

### Response body payload
- [type signedPayload](signedpayload.md)
  A cryptographically signed payload, in JSON Web Signature (JWS) format, that contains the response body for a version 2 notification.

## See Also

- [App Store Server Notifications V2](app-store-server-notifications-v2.md)
  Specify your secure server’s URL in App Store Connect to receive version 2 notifications.
- [object responseBodyV2DecodedPayload](responsebodyv2decodedpayload.md)
  A decoded payload that contains the version 2 notification data.
- [type notificationType](notificationtype.md)
  The type that describes the in-app purchase or external purchase event for which the App Store sends the version 2 notification.
- [type subtype](subtype.md)
  A string that provides details about select notification types in version 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/responsebodyv2)*