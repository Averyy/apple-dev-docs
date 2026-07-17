# List all localizations for an in-app purchase

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of localized display names and descriptions for a specific in-app purchase.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/inAppPurchases/{id}/inAppPurchaseLocalizations`

## Parameters

- `fields[inAppPurchaseLocalizations]` ([string])
- `fields[inAppPurchases]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [Create an in-app purchase localization (v1)](post-v1-inapppurchaselocalizations.md)
  Create a localized display name and description for an in-app purchase.
- [Read in-app purchase localization information (v1)](get-v1-inapppurchaselocalizations-_id_.md)
  Get the display name and description for a specific locale for an in-app purchase.
- [Modify an in-app purchase localization (v1)](patch-v1-inapppurchaselocalizations-_id_.md)
  Update the display name and description for a specific locale of an in-app purchase.
- [Delete an in-app purchase localization (v1)](delete-v1-inapppurchaselocalizations-_id_.md)
  Delete the metadata for a single in-app purchase localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-inapppurchases-_id_-inapppurchaselocalizations)*