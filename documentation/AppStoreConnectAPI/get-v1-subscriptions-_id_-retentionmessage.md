# Read the retention message for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the retention message for a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 4.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/retentionMessage`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the subscription resource ID from the [`List all subscriptions for a subscription group`](./get-v1-subscriptiongroups-_id_-subscriptions.md) response.

### Query Parameters

- `fields[retentionMessages]` ([string]): Additional fields to include for each retention message resource returned by the response.

  **Allowed Values**: `referenceName`, `versions`, `subscriptions`
- `fields[retentionMessageVersions]` ([string]): Additional fields to include for each retention message version resource returned by the response.

  **Allowed Values**: `state`, `retentionMessage`, `localizations`, `placement`
- `fields[subscriptions]` ([string]): Additional fields to include for each subscription resource returned by the response.

  **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`, `retentionOffers`, `retentionMessage`, `retentionMessageOffers`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `versions`, `subscriptions`
- `limit[versions]` (integer): The maximum number of related version resources to return.

  **Maximum**: `50`
- `limit[subscriptions]` (integer): The maximum number of related subscription resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`RetentionMessageResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Assigning retention messages to subscriptions
- [Read the retention message ID for a subscription](./get-v1-subscriptions-_id_-relationships-retentionmessage.md)
  Get the retention message ID for a specific auto-renewable subscription.
- [Replace the retention message for a subscription](./patch-v1-subscriptions-_id_-relationships-retentionmessage.md)
  Assign a retention message to a specific auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-retentionmessage)*