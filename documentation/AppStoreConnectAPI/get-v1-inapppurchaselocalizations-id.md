# Read In-App Purchase localization information (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the display name and description for a specific locale for an In-App Purchase.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseLocalizations/{id}`

## Parameters

- `fields[inAppPurchaseLocalizations]` ([string])
- `include` ([string])
- `fields[inAppPurchases]` ([string])

## See Also

- [List all localizations for an In-App Purchase](get-v2-inapppurchases-_id_-inapppurchaselocalizations.md)
  Get a list of localized display names and descriptions for a specific In-App Purchase.
- [Create an In-App Purchase localization (v1)](post-v1-inapppurchaselocalizations.md)
  Create a localized display name and description for an In-App Purchase.
- [Modify an In-App Purchase localization (v1)](patch-v1-inapppurchaselocalizations-_id_.md)
  Update the display name and description for a specific locale of an In-App Purchase.
- [Delete an In-App Purchase localization (v1)](delete-v1-inapppurchaselocalizations-_id_.md)
  Delete the metadata for a single In-App Purchase localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaselocalizations-_id_)*