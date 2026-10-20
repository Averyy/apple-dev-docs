# Read subscription information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Configuring multi-seat subscriptions for organizations](./configuring-multi-seat-subscriptions-for-organizations.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[promotedPurchases]` ([string]): **Allowed Values**: `visibleForAllUsers`, `enabled`, `state`, `inAppPurchaseV2`, `subscription`
- `fields[subscriptionIntroductoryOffers]` ([string]): **Allowed Values**: `startDate`, `endDate`, `duration`, `offerMode`, `numberOfPeriods`, `targetSubscriptionPlanType`, `subscription`, `territory`, `subscriptionPricePoint`
- `fields[subscriptionLocalizations]` ([string]): **Allowed Values**: `name`, `locale`, `description`, `state`, `subscription`
- `fields[subscriptionOfferCodes]` ([string]): **Allowed Values**: `name`, `customerEligibilities`, `offerEligibility`, `duration`, `offerMode`, `numberOfPeriods`, `totalNumberOfCodes`, `productionCodeCount`, `sandboxCodeCount`, `active`, `autoRenewEnabled`, `targetSubscriptionPlanType`, `subscription`, `oneTimeUseCodes`, `customCodes`, `prices`
- `fields[subscriptionPrices]` ([string]): **Allowed Values**: `startDate`, `preserved`, `planType`, `territory`, `subscriptionPricePoint`
- `fields[subscriptions]` ([string]): **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`
- `include` ([string]): **Allowed Values**: `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`
- `limit[introductoryOffers]` (integer): **Maximum**: `50`
- `limit[offerCodes]` (integer): **Maximum**: `50`
- `limit[prices]` (integer): **Maximum**: `50`
- `limit[subscriptionLocalizations]` (integer): **Maximum**: `50`
- `fields[subscriptionPromotionalOffers]` ([string]): **Allowed Values**: `duration`, `name`, `numberOfPeriods`, `offerCode`, `offerMode`, `targetSubscriptionPlanType`, `subscription`, `prices`
- `fields[subscriptionAppStoreReviewScreenshots]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `assetToken`, `assetType`, `uploadOperations`, `assetDeliveryState`, `subscription`
- `limit[promotionalOffers]` (integer): **Maximum**: `50`
- `fields[subscriptionAvailabilities]` ([string]) *(deprecated)*: **Allowed Values**: `availableInNewTerritories`, `availableTerritories`
- `fields[subscriptionGroups]` ([string]): **Allowed Values**: `referenceName`, `subscriptions`, `subscriptionGroupLocalizations`, `versions`
- `fields[subscriptionImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `assetToken`, `imageAsset`, `uploadOperations`, `state`, `subscription`
- `fields[subscriptionPlanAvailabilities]` ([string]): **Allowed Values**: `availableInNewTerritories`, `planType`, `availableTerritories`
- `fields[subscriptionVersions]` ([string]): **Allowed Values**: `version`, `state`, `subscription`, `image`, `images`, `localizations`
- `fields[winBackOffers]` ([string]): **Allowed Values**: `referenceName`, `offerId`, `duration`, `offerMode`, `periodCount`, `customerEligibilityPaidSubscriptionDurationInMonths`, `customerEligibilityTimeSinceLastSubscribedInMonths`, `customerEligibilityWaitBetweenOffersInMonths`, `startDate`, `endDate`, `priority`, `promotionIntent`, `targetSubscriptionPlanType`, `prices`
- `limit[images]` (integer): **Maximum**: `50`
- `limit[planAvailabilities]` (integer): **Maximum**: `50`
- `limit[versions]` (integer): **Maximum**: `50`
- `limit[winBackOffers]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`SubscriptionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and managing subscriptions
- [Create an auto-renewable subscription](./post-v1-subscriptions.md)
  Create an auto-renewable subscription for your app.
- [Modify an auto-renewable subscription](./patch-v1-subscriptions-_id_.md)
  Update a specific auto-renewable subscription.
- [Delete a subscription](./delete-v1-subscriptions-_id_.md)
  Delete a specific auto-renewable subscription that you configured for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_)*