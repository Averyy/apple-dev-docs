# In-App Purchase availability

**Framework**: App Store Connect API

Read and modify territory availability for an In-App Purchase.

## Topics

### Endpoints
- [Read information about the availablity of an In-App Purchase](get-v1-inapppurchaseavailabilities-_id_.md)
  Get information about the territory availablity for an In-App Purchase.
- [List the Territory Availablity of an In-App Purchase](get-v1-inapppurchaseavailabilities-_id_-availableterritories.md)
  List all the territories where an In-App Purchase is available.
- [List available territory IDs for an In-App Purchase availability](get-v1-inapppurchaseavailabilities-_id_-relationships-availableterritories.md)
- [Modify the Territory Availablity of an In-App Purchase](post-v1-inapppurchaseavailabilities.md)
  Update the territory availablity of a specific In-App Purchase.
### Objects
- [object InAppPurchaseAvailability](inapppurchaseavailability.md)
  The territory availability configuration for an In-App Purchase, specifying which App Store regions it’s offered in.
- [object InAppPurchaseAvailabilityCreateRequest](inapppurchaseavailabilitycreaterequest.md)
  The request body you use to create an In-App Purchase availability.
- [object InAppPurchaseAvailabilityResponse](inapppurchaseavailabilityresponse.md)
  A response containing a single territory availability configuration for an In-App Purchase.
- [object InAppPurchaseAvailabilityAvailableTerritoriesLinkagesResponse](inapppurchaseavailabilityavailableterritorieslinkagesresponse.md)

## See Also

- [Managing In-App Purchases](managing-in-app-purchases.md)
  Create In-App Purchases, configure their metadata and pricing, submit them for review, and promote them with the App Store Connect API.
- [Working with In-App Purchase versions](working-with-in-app-purchase-versions.md)
  Manage draft versions of an In-App Purchase’s localized metadata and review images before submitting for App Review.
- [Migrating In-App Purchase metadata to v2](migrating-in-app-purchase-metadata-to-v2.md)
  Update an existing integration from the pre-4.4.1 metadata workflow to the version-based v2 workflow.
- [In-App Purchase Versions](in-app-purchase-versions.md)
  Create and read draft versions of an In-App Purchase, with their localized metadata and review images.
- [In-App Purchases](in-app-purchases.md)
  Create, modify, and delete In-App Purchases for your app.
- [In-App Purchase Localizations](in-app-purchase-localizations.md)
  Create, modify, and delete localized metadata for In-App Purchase versions.
- [In-App Purchase localizations (v1)](in-app-purchase-localizations-v1.md)
  Create, modify, and delete localized metadata for In-App Purchases.
- [In-App Purchase price schedules](in-app-purchase-price-schedules.md)
  Create a scheduled price change for an In-App Purchase, and get information about scheduled price changes.
- [In-App Purchase images](in-app-purchase-images.md)
  Create, modify, and delete promotion images for In-App Purchases.
- [In-App Purchase images (v1)](in-app-purchase-images-v1.md)
  Create, modify, and delete promotion images for your In-App Purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/in-app-purchase-availability)*