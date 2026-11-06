# List subscriptions for a retention message

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of the auto-renewable subscriptions that use a specific retention message.

**Availability**:
- App Store Connect API 4.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/retentionMessages/{id}/subscriptions`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the retention message resource ID from the [`List retention messages for an app`](./get-v1-apps-_id_-retentionmessages.md) response.

### Query Parameters

- `filter[productId]` ([string]): Filter the returned subscriptions by product ID.
- `filter[name]` ([string]): Filter the returned subscriptions by name.
- `filter[state]` ([string]): Filter the returned subscriptions by state.

  **Allowed Values**: `MISSING_METADATA`, `READY_TO_SUBMIT`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `DEVELOPER_ACTION_NEEDED`, `PENDING_BINARY_APPROVAL`, `APPROVED`, `DEVELOPER_REMOVED_FROM_SALE`, `REMOVED_FROM_SALE`, `REJECTED`
- `sort` ([string]): Attributes by which to sort.

  **Allowed Values**: `name`, `-name`
- `fields[subscriptions]` ([string]): Additional fields to include for each subscription resource returned by the response.

  **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`, `retentionOffers`, `retentionMessage`, `retentionMessageOffers`
- `fields[subscriptionLocalizations]` ([string]): Additional fields to include for each subscription localization resource returned by the response.

  **Allowed Values**: `name`, `locale`, `description`, `state`, `subscription`
- `fields[subscriptionAppStoreReviewScreenshots]` ([string]): Additional fields to include for each subscription app store review screenshot resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `assetToken`, `assetType`, `uploadOperations`, `assetDeliveryState`, `subscription`
- `fields[subscriptionGroups]` ([string]): Additional fields to include for each subscription group resource returned by the response.

  **Allowed Values**: `referenceName`, `subscriptions`, `subscriptionGroupLocalizations`, `versions`
- `fields[subscriptionIntroductoryOffers]` ([string]): Additional fields to include for each subscription introductory offer resource returned by the response.

  **Allowed Values**: `startDate`, `endDate`, `duration`, `offerMode`, `numberOfPeriods`, `targetSubscriptionPlanType`, `subscription`, `territory`, `subscriptionPricePoint`
- `fields[subscriptionPromotionalOffers]` ([string]): Additional fields to include for each subscription promotional offer resource returned by the response.

  **Allowed Values**: `duration`, `name`, `numberOfPeriods`, `offerCode`, `offerMode`, `targetSubscriptionPlanType`, `subscription`, `prices`
- `fields[subscriptionOfferCodes]` ([string]): Additional fields to include for each subscription offer code resource returned by the response.

  **Allowed Values**: `name`, `customerEligibilities`, `offerEligibility`, `duration`, `offerMode`, `numberOfPeriods`, `totalNumberOfCodes`, `productionCodeCount`, `sandboxCodeCount`, `active`, `autoRenewEnabled`, `targetSubscriptionPlanType`, `subscription`, `oneTimeUseCodes`, `customCodes`, `prices`
- `fields[subscriptionPrices]` ([string]): Additional fields to include for each subscription price resource returned by the response.

  **Allowed Values**: `startDate`, `preserved`, `planType`, `territory`, `subscriptionPricePoint`
- `fields[promotedPurchases]` ([string]): Additional fields to include for each promoted purchase resource returned by the response.

  **Allowed Values**: `visibleForAllUsers`, `enabled`, `state`, `inAppPurchaseV2`, `subscription`
- `fields[subscriptionAvailabilities]` ([string]): Additional fields to include for each subscription availability resource returned by the response.

  **Allowed Values**: `availableInNewTerritories`, `availableTerritories`
- `fields[winBackOffers]` ([string]): Additional fields to include for each win back offer resource returned by the response.

  **Allowed Values**: `referenceName`, `offerId`, `duration`, `offerMode`, `periodCount`, `customerEligibilityPaidSubscriptionDurationInMonths`, `customerEligibilityTimeSinceLastSubscribedInMonths`, `customerEligibilityWaitBetweenOffersInMonths`, `startDate`, `endDate`, `priority`, `promotionIntent`, `targetSubscriptionPlanType`, `prices`
- `fields[subscriptionImages]` ([string]): Additional fields to include for each subscription image resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `assetToken`, `imageAsset`, `uploadOperations`, `state`, `subscription`
- `fields[subscriptionPlanAvailabilities]` ([string]): Additional fields to include for each subscription plan availability resource returned by the response.

  **Allowed Values**: `availableInNewTerritories`, `planType`, `availableTerritories`
- `fields[subscriptionVersions]` ([string]): Additional fields to include for each subscription version resource returned by the response.

  **Allowed Values**: `version`, `state`, `subscription`, `image`, `images`, `localizations`
- `fields[retentionOffers]` ([string]): Additional fields to include for each retention offer resource returned by the response.

  **Allowed Values**: `referenceName`, `offerId`, `duration`, `offerMode`, `periodCount`, `customerEligibilityPaidSubscriptionDurationInMonths`, `customerEligibilityWaitBetweenOffersInMonths`, `targetSubscriptionPlanType`, `subscription`, `prices`
- `fields[retentionMessages]` ([string]): Additional fields to include for each retention message resource returned by the response.

  **Allowed Values**: `referenceName`, `versions`, `subscriptions`
- `limit` (integer): The maximum number of subscription resources to return.

  **Maximum**: `200`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`, `retentionOffers`, `retentionMessage`, `retentionMessageOffers`
- `limit[subscriptionLocalizations]` (integer): The maximum number of related subscription localization resources to return.

  **Maximum**: `50`
- `limit[introductoryOffers]` (integer): The maximum number of related introductory offer resources to return.

  **Maximum**: `50`
- `limit[promotionalOffers]` (integer): The maximum number of related promotional offer resources to return.

  **Maximum**: `50`
- `limit[offerCodes]` (integer): The maximum number of related offer code resources to return.

  **Maximum**: `50`
- `limit[prices]` (integer): The maximum number of related price resources to return.

  **Maximum**: `50`
- `limit[winBackOffers]` (integer): The maximum number of related win back offer resources to return.

  **Maximum**: `50`
- `limit[images]` (integer): The maximum number of related image resources to return.

  **Maximum**: `50`
- `limit[planAvailabilities]` (integer): The maximum number of related plan availability resources to return.

  **Maximum**: `50`
- `limit[versions]` (integer): The maximum number of related version resources to return.

  **Maximum**: `50`
- `limit[retentionOffers]` (integer): The maximum number of related retention offer resources to return.

  **Maximum**: `50`
- `limit[retentionMessageOffers]` (integer): The maximum number of related retention message offer resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`SubscriptionsResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Getting retention messages
- [Read a retention message](./get-v1-retentionmessages-_id_.md)
  Read details about a specific retention message.
- [List versions for a retention message](./get-v1-retentionmessages-_id_-versions.md)
  Get a list of versions for a specific retention message.
- [List version IDs for a retention message](./get-v1-retentionmessages-_id_-relationships-versions.md)
  Get a list of version IDs for a specific retention message.
- [List subscription IDs for a retention message](./get-v1-retentionmessages-_id_-relationships-subscriptions.md)
  Get a list of the subscription IDs that use a specific retention message.
- [List retention messages for an app](./get-v1-apps-_id_-retentionmessages.md)
  Get a list of retention messages for a specific app.
- [List retention message IDs for an app](./get-v1-apps-_id_-relationships-retentionmessages.md)
  Get a list of retention message IDs for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-retentionmessages-_id_-subscriptions)*