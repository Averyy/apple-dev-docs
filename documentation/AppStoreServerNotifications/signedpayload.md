# signedPayload

**Framework**: App Store Server Notifications  
**Kind**: typealias

A cryptographically signed payload, in JSON Web Signature (JWS) format, that contains the response body for a version 2 notification.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
string signedPayload
```

## Mentions

- [Receiving App Store Server Notifications](receiving-app-store-server-notifications.md)

#### Discussion

The `signedPayload` is a string of three Base64URL-encoded components, separated by a period. The string contains a JWS representation of the notification response body, signed by the App Store according to the JSON Web Signature (JWS) [`IETF RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515) specification.

The three components of the string are a header, a payload, and a signature, in that order.

To read the notification response body, Base64URL-decode the payload. Use a [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md) object to read the payload information.

To read the header, Base64URL-decode it and use a [`JWSDecodedHeader`](jwsdecodedheader.md) object to access the information. Use the information in the decoded header to verify the signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/signedpayload)*