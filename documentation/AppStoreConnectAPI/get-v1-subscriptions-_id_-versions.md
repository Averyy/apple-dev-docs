# List versions for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List the draft versions of an auto-renewable subscription.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](./app-store-connect-api-4-4-1-release-notes.md)
- [Working with subscription versions](./working-with-subscription-versions.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/versions`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `filter[state]` ([string]): **Allowed Values**: `PREPARE_FOR_SUBMISSION`, `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `ACCEPTED`, `APPROVED`, `REPLACED_WITH_NEW_VERSION`, `REJECTED`, `DEVELOPER_REJECTED`
- `fields[subscriptionVersions]` ([string]): **Allowed Values**: `version`, `state`, `subscription`, `image`, `images`, `localizations`
- `fields[subscriptions]` ([string]): **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`
- `fields[subscriptionImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `assetToken`, `imageAsset`, `uploadOperations`, `assetDeliveryState`
- `fields[subscriptionLocalizations]` ([string]): **Allowed Values**: `name`, `locale`, `description`, `version`
- `limit` (integer): **Maximum**: `200`
- `include` ([string]): **Allowed Values**: `subscription`, `image`, `images`, `localizations`
- `limit[images]` (integer): **Maximum**: `50`
- `limit[localizations]` (integer): **Maximum**: `50`

## Responses

- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `200` OK (`SubscriptionVersionsResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create a subscription version](./post-v1-subscriptionversions.md)
  Create a draft version of an auto-renewable subscription, capturing its current localized metadata and review images for App Review submission.
- [Read subscription version information](./get-v1-subscriptionversions-_id_.md)
  Get information about a specific draft version of an auto-renewable subscription.
- [Read the image for a subscription version](./get-v1-subscriptionversions-_id_-image.md)
  Get the review image attached to a draft version of an auto-renewable subscription.
- [List images for a subscription version](./get-v1-subscriptionversions-_id_-images.md)
  List the review images attached to a draft version of an auto-renewable subscription.
- [List localizations for a subscription version](./get-v1-subscriptionversions-_id_-localizations.md)
  List the localized display names and descriptions captured in a draft version of an auto-renewable subscription.
- [Read the image ID for a subscription version](./get-v1-subscriptionversions-_id_-relationships-image.md)
  Get the related resource ID for the review image attached to a draft version of an auto-renewable subscription.
- [List image IDs for a subscription version](./get-v1-subscriptionversions-_id_-relationships-images.md)
  Get the related resource IDs for the review images attached to a draft version of an auto-renewable subscription.
- [List localization IDs for a subscription version](./get-v1-subscriptionversions-_id_-relationships-localizations.md)
  Get the related resource IDs for the localizations captured in a draft version of an auto-renewable subscription.
- [List version IDs for a subscription](./get-v1-subscriptions-_id_-relationships-versions.md)
  Get the related resource IDs for the draft versions of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-versions)*