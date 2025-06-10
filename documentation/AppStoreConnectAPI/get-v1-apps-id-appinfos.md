# List All App Infos for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about an app that is currently live on App Store, or that goes live with the next version.

**Availability**:
- App Store Connect API 1.2+

#### Discussion

Use this endpoint to retrieve the derived app-level information for an app. If the app has both a “Ready for Sale” version and a version you’re preparing for release, it will have two app infos. One represents information about the app currently in the App Store, and the other represents the information that takes effect when you release the next version. Use the `appStoreState` attribute to differentiate them.

##### Example Request and Response

## See Also

- [GET /v1/apps/{id}/relationships/appInfos](get-v1-apps-_id_-relationships-appinfos.md)
- [List All App Store Versions for an App](get-v1-apps-_id_-appstoreversions.md)
  Get a list of all App Store versions of an app across all platforms.
- [GET /v1/apps/{id}/relationships/appStoreVersions](get-v1-apps-_id_-relationships-appstoreversions.md)
- [Read the End User License Agreement Information of an App](get-v1-apps-_id_-enduserlicenseagreement.md)
  Get the custom end user license agreement (EULA) for a specific app and the territories where the agreement applies.
- [GET /v1/apps/{id}/relationships/endUserLicenseAgreement](get-v1-apps-_id_-relationships-enduserlicenseagreement.md)
- [List all custom product pages for an app](get-v1-apps-_id_-appcustomproductpages.md)
  Get a list of all custom product pages for a specific app.
- [GET /v1/apps/{id}/relationships/appCustomProductPages](get-v1-apps-_id_-relationships-appcustomproductpages.md)
- [GET /v1/apps/{id}/appStoreVersionExperimentsV2](get-v1-apps-_id_-appstoreversionexperimentsv2.md)
- [GET /v1/apps/{id}/relationships/appStoreVersionExperimentsV2](get-v1-apps-_id_-relationships-appstoreversionexperimentsv2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appinfos)*