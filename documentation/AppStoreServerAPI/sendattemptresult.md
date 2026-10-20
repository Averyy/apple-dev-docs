# sendAttemptResult

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The success or error information the App Store server records when it attempts to send an App Store server notification to your server.

**Availability**:
- App Store Server API 1.8+

## Declaration

```
string sendAttemptResult
```

## Possible Values

- `SUCCESS`: The App Store server received a success response when it sent the notification to your server.
- `CIRCULAR_REDIRECT`: The App Store server detected a continual redirect. Check your server’s redirects for a circular redirect loop.
- `INVALID_RESPONSE`: The App Store server received an invalid response from your server.
- `NO_RESPONSE`: The App Store server didn’t receive a valid HTTP response from your server.
- `OTHER`: Another error occurred that prevented your server from receiving the notification.
- `PREMATURE_CLOSE`: The App Store server’s connection to your server was closed while the send was in progress.
- `SOCKET_ISSUE`: A network error caused the notification attempt to fail.
- `TIMED_OUT`: The App Store server didn’t get a response from your server and timed out. Check that your server isn’t processing messages in line.
- `TLS_ISSUE`: The App Store server couldn’t establish a TLS session or validate your certificate. Check that your server has a valid certificate and supports Transport Layer Security (TLS) protocol 1.2 or later.
- `UNSUCCESSFUL_HTTP_RESPONSE_CODE`: The App Store server didn’t receive an `HTTP 200` response from your server.
- `UNSUPPORTED_CHARSET`: The App Store server doesn’t support the supplied charset.

#### Discussion

The [`Get Notification History`](./get-notification-history.md) and [`Get Test Notification Status`](./get-test-notification-status.md) endpoints return a [`sendAttemptResult`](./sendattemptresult.md) for each notification attempt in their responses. This value describes the success or error the server encountered on its attempt to send the notification to your server.

In the production environment, the App Store server retries sending the notfications if it doesn’t receive a `200` response from your server. Your server may have successfully received the notification on the App Store server’s subsequent attempt if the [`sendAttemptResult`](./sendattemptresult.md) value shows an error.

In the sandbox environment, the App Store server attempts to send the notification one time.

For more information about the timing of retry attempts, see [Responding to App Store Server Notifications](../AppStoreServerNotifications/responding-to-app-store-server-notifications.md).

## See Also

### Data types
- [object sendAttemptItem](./sendattemptitem.md)
  The success or error information and the date the App Store server records when it attempts to send a server notification to your server.
- [type signedPayload](./signedpayload.md)
  A cryptographically signed payload, in JSON Web Signature (JWS) format, containing the response body for a version 2 notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/sendattemptresult)*