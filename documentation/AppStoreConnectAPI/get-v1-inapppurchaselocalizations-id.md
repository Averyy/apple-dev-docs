# Read in-app purchase localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the display name and description for a specific locale for an in-app purchase.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseLocalizations/{id}`

## Parameters

- `fields[inAppPurchaseLocalizations]` ([string])
- `include` ([string])
- `fields[inAppPurchases]` ([string])

## See Also

- [List all localizations for an in-app purchase](get-v2-inapppurchases-_id_-inapppurchaselocalizations.md)
  Get a list of localized display names and descriptions for a specific in-app purchase.
- [Create an in-app purchase localization](post-v1-inapppurchaselocalizations.md)
  Create a localized display name and description for an in-app purchase.
- [Modify an in-app purchase localization](patch-v1-inapppurchaselocalizations-_id_.md)
  Update the display name and description for a specific locale of an in-app purchase.
- [Delete an in-app purchase localization](delete-v1-inapppurchaselocalizations-_id_.md)
  Delete the metadata for a single in-app purchase localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaselocalizations-_id_)*