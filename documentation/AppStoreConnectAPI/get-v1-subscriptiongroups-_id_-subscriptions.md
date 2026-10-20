# List all subscriptions for a subscription group

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of all auto-renewable subscriptions in a subscription group.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionGroups/{id}/subscriptions`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[promotedPurchases]` ([string]): **Allowed Values**: `visibleForAllUsers`, `enabled`, `state`, `inAppPurchaseV2`, `subscription`
- `fields[subscriptionGroups]` ([string]): **Allowed Values**: `referenceName`, `subscriptions`, `subscriptionGroupLocalizations`, `versions`
- `fields[subscriptionIntroductoryOffers]` ([string]): **Allowed Values**: `startDate`, `endDate`, `duration`, `offerMode`, `numberOfPeriods`, `targetSubscriptionPlanType`, `subscription`, `territory`, `subscriptionPricePoint`
- `fields[subscriptionLocalizations]` ([string]): **Allowed Values**: `name`, `locale`, `description`, `state`, `subscription`
- `fields[subscriptionOfferCodes]` ([string]): **Allowed Values**: `name`, `customerEligibilities`, `offerEligibility`, `duration`, `offerMode`, `numberOfPeriods`, `totalNumberOfCodes`, `productionCodeCount`, `sandboxCodeCount`, `active`, `autoRenewEnabled`, `targetSubscriptionPlanType`, `subscription`, `oneTimeUseCodes`, `customCodes`, `prices`
- `fields[subscriptionPrices]` ([string]): **Allowed Values**: `startDate`, `preserved`, `planType`, `territory`, `subscriptionPricePoint`
- `fields[subscriptions]` ([string]): **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`
- `filter[name]` ([string])
- `filter[productId]` ([string])
- `filter[state]` ([string]): **Allowed Values**: `MISSING_METADATA`, `READY_TO_SUBMIT`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `DEVELOPER_ACTION_NEEDED`, `PENDING_BINARY_APPROVAL`, `APPROVED`, `DEVELOPER_REMOVED_FROM_SALE`, `REMOVED_FROM_SALE`, `REJECTED`
- `include` ([string]): **Allowed Values**: `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`
- `limit` (integer): **Maximum**: `200`
- `limit[introductoryOffers]` (integer): **Maximum**: `50`
- `limit[offerCodes]` (integer): **Maximum**: `50`
- `limit[prices]` (integer): **Maximum**: `50`
- `limit[subscriptionLocalizations]` (integer): **Maximum**: `50`
- `sort` ([string]): **Allowed Values**: `name`, `-name`
- `fields[subscriptionPromotionalOffers]` ([string]): **Allowed Values**: `duration`, `name`, `numberOfPeriods`, `offerCode`, `offerMode`, `targetSubscriptionPlanType`, `subscription`, `prices`
- `fields[subscriptionAppStoreReviewScreenshots]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `assetToken`, `assetType`, `uploadOperations`, `assetDeliveryState`, `subscription`
- `limit[promotionalOffers]` (integer): **Maximum**: `50`
- `fields[subscriptionAvailabilities]` ([string]): **Allowed Values**: `availableInNewTerritories`, `availableTerritories`
- `fields[subscriptionImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `assetToken`, `imageAsset`, `uploadOperations`, `state`, `subscription`
- `fields[subscriptionPlanAvailabilities]` ([string]): **Allowed Values**: `availableInNewTerritories`, `planType`, `availableTerritories`
- `fields[subscriptionVersions]` ([string]): **Allowed Values**: `version`, `state`, `subscription`, `image`, `images`, `localizations`
- `fields[winBackOffers]` ([string]): **Allowed Values**: `referenceName`, `offerId`, `duration`, `offerMode`, `periodCount`, `customerEligibilityPaidSubscriptionDurationInMonths`, `customerEligibilityTimeSinceLastSubscribedInMonths`, `customerEligibilityWaitBetweenOffersInMonths`, `startDate`, `endDate`, `priority`, `promotionIntent`, `targetSubscriptionPlanType`, `prices`
- `limit[images]` (integer): **Maximum**: `50`
- `limit[planAvailabilities]` (integer): **Maximum**: `50`
- `limit[versions]` (integer): **Maximum**: `50`
- `limit[winBackOffers]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`SubscriptionsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create a subscription group](./post-v1-subscriptiongroups.md)
  Create a subscription group for an app.
- [List all subscription groups for an app](./get-v1-apps-_id_-subscriptiongroups.md)
  Get a list of subscription groups for a specific app.
- [List subscription group IDs for an app](./get-v1-apps-_id_-relationships-subscriptiongroups.md)
- [Read subscription group information](./get-v1-subscriptiongroups-_id_.md)
  Get the details of a specific subscription group.
- [Modify a subscription group](./patch-v1-subscriptiongroups-_id_.md)
  Update the reference name for a specific subscription group.
- [Delete a subscription group](./delete-v1-subscriptiongroups-_id_.md)
  Delete a specific empty subscription group.
- [List all subscription group localizations](./get-v1-subscriptiongroups-_id_-subscriptiongrouplocalizations.md)
  Get a list of all localized metadata for a specific subscription group.
- [List localization IDs for a subscription group](./get-v1-subscriptiongroups-_id_-relationships-subscriptiongrouplocalizations.md)
- [List subscription IDs for a subscription group](./get-v1-subscriptiongroups-_id_-relationships-subscriptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptiongroups-_id_-subscriptions)*