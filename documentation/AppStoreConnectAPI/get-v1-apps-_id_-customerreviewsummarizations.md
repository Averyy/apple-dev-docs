# Read Customer Review Summarizations

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the customer review summarization for a specific app.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [App Store Connect API 4.0 release notes](./app-store-connect-api-4-0-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/customerReviewSummarizations`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the `apps` resource that represents your app. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `include` ([string]): Relationship data to include in the response.

  **Allowed Values**: `territory`
- `limit` (integer): Number of resources to return.

  **Maximum**: `200`
- `filter[territory]` ([string]): A filter of territories to include in the response.
- `fields[customerReviewSummarizations]` ([string]): **Allowed Values**: `createdDate`, `locale`, `platform`, `text`, `territory`
- `fields[territories]` ([string]): **Allowed Values**: `currency`
- `filter[platform]` ([string]) *(required)*: **Allowed Values**: `IOS`, `MAC_OS`, `TV_OS`, `VISION_OS`

## Responses

- `200` OK (`CustomerReviewSummarizationsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting customer reviews
- [List all customer reviews for an app](./get-v1-apps-_id_-customerreviews.md)
  Get a list of customer reviews for a specific app.
- [List customer review IDs for an app](./get-v1-apps-_id_-relationships-customerreviews.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-customerreviewsummarizations)*