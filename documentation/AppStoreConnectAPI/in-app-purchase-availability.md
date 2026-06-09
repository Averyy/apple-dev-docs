# In-app purchase availability

**Framework**: App Store Connect API

Read and modify territory availability for an in-app purchase.

## Topics

### Endpoints
- [Read information about the availablity of an in-app purchase](get-v1-inapppurchaseavailabilities-_id_.md)
  Get information about the territory availablity for an in-app purchase.
- [List the Territory Availablity of an In-App Purchase](get-v1-inapppurchaseavailabilities-_id_-availableterritories.md)
  List all the territories where an in-app purchase is available.
- [List available territory IDs for an in-app purchase availability](get-v1-inapppurchaseavailabilities-_id_-relationships-availableterritories.md)
- [Modify the Territory Availablity of an In-App Purchase](post-v1-inapppurchaseavailabilities.md)
  Update the territory availablity of a specific in-app purchase.
### Objects
- [object InAppPurchaseAvailability](inapppurchaseavailability.md)
  The territory availability configuration for an in-app purchase, specifying which App Store regions it’s offered in.
- [object InAppPurchaseAvailabilityCreateRequest](inapppurchaseavailabilitycreaterequest.md)
  The request body you use to create an in-app purchase availability.
- [object InAppPurchaseAvailabilityResponse](inapppurchaseavailabilityresponse.md)
  A response containing a single territory availability configuration for an in-app purchase.
- [object InAppPurchaseAvailabilityAvailableTerritoriesLinkagesResponse](inapppurchaseavailabilityavailableterritorieslinkagesresponse.md)

## See Also

- [Managing in-app purchases](managing-in-app-purchases.md)
  Learn how to create and manage in-app purchases with the App Store Connect API.
- [In-App Purchases](in-app-purchases.md)
  Create, modify, and delete in-app purchases for your app.
- [In-App Purchase Localizations](in-app-purchase-localizations.md)
  Create, modify, and delete localized metadata for in-app purchases.
- [In-App purchase price schedules](in-app-purchase-price-schedules.md)
  Create a scheduled price change for an in-app purchase, and get information about scheduled price changes.
- [In-app purchase images](in-app-purchase-images.md)
  Create, modify, and delete promotion images for your in-app purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/in-app-purchase-availability)*