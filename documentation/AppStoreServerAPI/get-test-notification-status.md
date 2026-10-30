# Get Test Notification Status

**Framework**: App Store Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Check the status of the test App Store server notification sent to your server.

**Availability**:
- App Store Server API 1.5+

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)
- [Identifying rate limits](./identifying-rate-limits.md)

## Discussion

Call this endpoint using the `testNotificationToken` you receive when you call [`Request a Test Notification`](./request-a-test-notification.md). You can check the status using the `testNotificationToken` for up to six months. Use the information in the [`CheckTestNotificationResponse`](./checktestnotificationresponse.md) to troubleshoot your server if it’s unable to receive App Store Server Notifications successfully.

## Endpoint

`GET https://api.storekit-sandbox.apple.com/inApps/v1/notifications/test/{testNotificationToken}`

## Parameters

### Path Parameters

- `testNotificationToken` (testNotificationToken) *(required)*: The token that uniquely identifies a test, that you receive when you call [`Request a Test Notification`](./request-a-test-notification.md).

## Responses

- `200` OK (`CheckTestNotificationResponse`, `application/json`): Success.
- `400` Bad Request (`InvalidTestNotificationTokenError`, `application/json`): The test notification token is invalid. Use a valid token that you receive in the [`SendTestNotificationResponse`](./sendtestnotificationresponse.md).
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](./generating-json-web-tokens-for-api-requests.md).
- `404` Not Found (`TestNotificationNotFoundError`, `application/json`): The status isn’t yet available or the test notification token wasn’t found.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit.
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`): Server error. Try again later.

## See Also

### App Store Server Notifications testing
- [Request a Test Notification](./request-a-test-notification.md)
  Ask App Store Server Notifications to send a test notification to your server.
- [object SendTestNotificationResponse](./sendtestnotificationresponse.md)
  A response that contains the test notification token.
- [object CheckTestNotificationResponse](./checktestnotificationresponse.md)
  A response that contains the contents of the App Store server’s test notification and the result from your server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-test-notification-status)*