# signedPayload

**Framework**: App Store Server API  
**Kind**: typealias

A cryptographically signed payload, in JSON Web Signature (JWS) format, containing the response body for a version 2 notification.

**Availability**:
- App Store Server API 1.5+

## Declaration

```swift
string signedPayload
```

#### Discussion

The `signedpayload` is a string of three Base64 URL-encoded components, separated by a period.

For more information, see [`signedPayload`](https://developer.apple.com/documentation/AppStoreServerNotifications/signedPayload) in [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications).

## See Also

- [object sendAttemptItem](sendattemptitem.md)
  The success or error information and the date the App Store server records when it attempts to send a server notification to your server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/signedpayload)*