# Read a retention message

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Read details about a specific retention message.

**Availability**:
- App Store Connect API 4.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/retentionMessages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the retention message resource ID from the [`List retention messages for an app`](./get-v1-apps-_id_-retentionmessages.md) response.

### Query Parameters

- `fields[retentionMessages]` ([string]): Additional fields to include for each retention message resource returned by the response.

  **Allowed Values**: `referenceName`, `versions`, `subscriptions`
- `fields[retentionMessageVersions]` ([string]): Additional fields to include for each retention message version resource returned by the response.

  **Allowed Values**: `state`, `retentionMessage`, `localizations`, `placement`
- `fields[subscriptions]` ([string]): Additional fields to include for each subscription resource returned by the response.

  **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`, `retentionOffers`, `retentionMessage`, `retentionMessageOffers`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `versions`, `subscriptions`
- `limit[subscriptions]` (integer): The maximum number of related subscription resources to return.

  **Maximum**: `50`
- `limit[versions]` (integer): The maximum number of related version resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`RetentionMessageResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Getting retention messages
- [List versions for a retention message](./get-v1-retentionmessages-_id_-versions.md)
  Get a list of versions for a specific retention message.
- [List version IDs for a retention message](./get-v1-retentionmessages-_id_-relationships-versions.md)
  Get a list of version IDs for a specific retention message.
- [List subscriptions for a retention message](./get-v1-retentionmessages-_id_-subscriptions.md)
  Get a list of the auto-renewable subscriptions that use a specific retention message.
- [List subscription IDs for a retention message](./get-v1-retentionmessages-_id_-relationships-subscriptions.md)
  Get a list of the subscription IDs that use a specific retention message.
- [List retention messages for an app](./get-v1-apps-_id_-retentionmessages.md)
  Get a list of retention messages for a specific app.
- [List retention message IDs for an app](./get-v1-apps-_id_-relationships-retentionmessages.md)
  Get a list of retention message IDs for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-retentionmessages-_id_)*