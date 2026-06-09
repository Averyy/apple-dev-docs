# Get the end user license agreement ID for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/relationships/endUserLicenseAgreement`

## Parameters

- `id` (string) *(required)*

## See Also

- [List all app infos for an app](get-v1-apps-_id_-appinfos.md)
  Get information about an app that is currently live on App Store, or that goes live with the next version.
- [List app info IDs for an app](get-v1-apps-_id_-relationships-appinfos.md)
- [List all app store versions for an app](get-v1-apps-_id_-appstoreversions.md)
  Get a list of all App Store versions of an app across all platforms.
- [List App Store version IDs for an app](get-v1-apps-_id_-relationships-appstoreversions.md)
- [Read the end user license agreement information of an app](get-v1-apps-_id_-enduserlicenseagreement.md)
  Get the custom end user license agreement (EULA) for a specific app and the territories where the agreement applies.
- [List All Custom Product Pages for an App](get-v1-apps-_id_-appcustomproductpages.md)
  Get a list of all custom product pages for a specific app.
- [Get all custom product page resource ids for an app](get-v1-apps-_id_-relationships-appcustomproductpages.md)
  Get a list of custom product page resource IDs associated with an app.
- [List all app store experiments for an app](get-v1-apps-_id_-appstoreversionexperimentsv2.md)
  Get a list of all App Store version experiments for a specific app.
- [List App Store version experiment IDs for an app](get-v1-apps-_id_-relationships-appstoreversionexperimentsv2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-relationships-enduserlicenseagreement)*