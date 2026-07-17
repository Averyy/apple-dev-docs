# Read subscription information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}`

## Parameters

- `fields[promotedPurchases]` ([string])
- `fields[subscriptionIntroductoryOffers]` ([string])
- `fields[subscriptionLocalizations]` ([string])
- `fields[subscriptionOfferCodes]` ([string])
- `fields[subscriptionPrices]` ([string])
- `fields[subscriptions]` ([string])
- `include` ([string])
- `limit[introductoryOffers]` (integer)
- `limit[offerCodes]` (integer)
- `limit[prices]` (integer)
- `limit[subscriptionLocalizations]` (integer)
- `fields[subscriptionPromotionalOffers]` ([string])
- `fields[subscriptionAppStoreReviewScreenshots]` ([string])
- `limit[promotionalOffers]` (integer)
- `fields[subscriptionAvailabilities]` ([string])
- `fields[subscriptionGroups]` ([string])
- `fields[subscriptionImages]` ([string])
- `fields[subscriptionPlanAvailabilities]` ([string])
- `fields[subscriptionVersions]` ([string])
- `fields[winBackOffers]` ([string])
- `limit[images]` (integer)
- `limit[planAvailabilities]` (integer)
- `limit[versions]` (integer)
- `limit[winBackOffers]` (integer)

## See Also

- [Create an auto-renewable subscription](post-v1-subscriptions.md)
  Create an auto-renewable subscription for your app.
- [Modify an auto-renewable subscription](patch-v1-subscriptions-_id_.md)
  Update a specific auto-renewable subscription.
- [Delete a subscription](delete-v1-subscriptions-_id_.md)
  Delete a specific auto-renewable subscription that you configured for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_)*