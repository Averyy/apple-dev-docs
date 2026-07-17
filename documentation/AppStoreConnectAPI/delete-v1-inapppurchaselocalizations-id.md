# Delete an in-app purchase localization (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete the metadata for a single in-app purchase localization.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/inAppPurchaseLocalizations/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [List all localizations for an in-app purchase](get-v2-inapppurchases-_id_-inapppurchaselocalizations.md)
  Get a list of localized display names and descriptions for a specific in-app purchase.
- [Create an in-app purchase localization (v1)](post-v1-inapppurchaselocalizations.md)
  Create a localized display name and description for an in-app purchase.
- [Read in-app purchase localization information (v1)](get-v1-inapppurchaselocalizations-_id_.md)
  Get the display name and description for a specific locale for an in-app purchase.
- [Modify an in-app purchase localization (v1)](patch-v1-inapppurchaselocalizations-_id_.md)
  Update the display name and description for a specific locale of an in-app purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-inapppurchaselocalizations-_id_)*