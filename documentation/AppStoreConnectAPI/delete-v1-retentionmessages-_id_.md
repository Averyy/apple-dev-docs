# Delete a retention message

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a specific retention message.

**Availability**:
- App Store Connect API 4.6+

## Mentions

- [Setting up retention messaging for auto-renewable subscriptions](./setting-up-retention-messaging.md)

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/retentionMessages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the retention message resource ID from the [`List retention messages for an app`](./get-v1-apps-_id_-retentionmessages.md) response.

## Responses

- `204` No Content: The request completed successfully with no response body.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Managing retention messages
- [Create a retention message](./post-v1-retentionmessages.md)
  Create a retention message for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-retentionmessages-_id_)*