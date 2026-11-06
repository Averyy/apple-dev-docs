# List retention message IDs for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of retention message IDs for a specific app.

**Availability**:
- App Store Connect API 4.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/relationships/retentionMessages`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `limit` (integer): The maximum number of retention message resource identifiers to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AppRetentionMessagesLinkagesResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Getting retention messages
- [List retention messages for an app](./get-v1-apps-_id_-retentionmessages.md)
  Get a list of retention messages for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-relationships-retentionmessages)*