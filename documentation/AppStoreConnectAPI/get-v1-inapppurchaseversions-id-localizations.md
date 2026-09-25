# List localizations for an In-App Purchase version

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the localized display names and descriptions captured in a draft version of an In-App Purchase.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](app-store-connect-api-4-4-1-release-notes.md)
- [Managing In-App Purchases](managing-in-app-purchases.md)
- [Working with In-App Purchase versions](working-with-in-app-purchase-versions.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseVersions/{id}/localizations`

## Parameters

- `fields[inAppPurchaseLocalizations]` ([string])
- `fields[inAppPurchaseVersions]` ([string])
- `limit` (integer)
- `include` ([string])

## See Also

- [Create an In-App Purchase localization](post-v2-inapppurchaselocalizations.md)
  Create a localized display name and description for an In-App Purchase configured with the v2 API.
- [Read In-App Purchase localization information](get-v2-inapppurchaselocalizations-_id_.md)
  Get the display name and description for a specific locale of an In-App Purchase configured with the v2 API.
- [Modify an In-App Purchase localization](patch-v2-inapppurchaselocalizations-_id_.md)
  Update the display name and description for a specific locale of an In-App Purchase configured with the v2 API.
- [Delete an In-App Purchase localization](delete-v2-inapppurchaselocalizations-_id_.md)
  Delete a localized display name and description for an In-App Purchase configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseversions-_id_-localizations)*