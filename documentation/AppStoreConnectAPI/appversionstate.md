# AppVersionState

**Framework**: App Store Connect API  
**Kind**: typealias  
**Role**: Type

String that represents the state of an app version.

**Availability**:
- App Store Connect API 3.3+

## Declaration

```
string AppVersionState
```

## Possible Values

- `ACCEPTED`
- `DEVELOPER_REJECTED`
- `IN_REVIEW`
- `INVALID_BINARY`
- `METADATA_REJECTED`
- `PENDING_APPLE_RELEASE`
- `PENDING_DEVELOPER_RELEASE`
- `PREPARE_FOR_SUBMISSION`
- `PROCESSING_FOR_DISTRIBUTION`
- `READY_FOR_DISTRIBUTION`
- `READY_FOR_REVIEW`
- `REJECTED`
- `REPLACED_WITH_NEW_VERSION`
- `WAITING_FOR_EXPORT_COMPLIANCE`
- `WAITING_FOR_REVIEW`

## Mentions

- [App Store Connect API 3.7 release notes](./app-store-connect-api-3-7-release-notes.md)

## See Also

### Objects and Data Types
- [object AppStoreVersionUpdateRequest](./appstoreversionupdaterequest.md)
  The request body you use to update an App Store Version.
- [object AgeRatingDeclaration](./ageratingdeclaration.md)
  A set of content descriptors for your app that App Store Connect uses to assign an age rating.
- [object AppStoreVersion](./appstoreversion.md)
  The data structure that represent an App Store Versions resource.
- [object AppStoreVersionResponse](./appstoreversionresponse.md)
  The response body for endpoints that create, read, or modify an App Store version.
- [object AppStoreVersionsResponse](./appstoreversionsresponse.md)
  The response body for endpoints that list App Store versions for an app.
- [object AppStoreVersionCreateRequest](./appstoreversioncreaterequest.md)
  The request body you use to create an App Store Version.
- [object AppStoreVersionBuildLinkageRequest](./appstoreversionbuildlinkagerequest.md)
  The request body you use to attach a build to an App Store version.
- [object AppStoreVersionBuildLinkageResponse](./appstoreversionbuildlinkageresponse.md)
  A response body that contains the ID of a single related resource.
- [object AppStoreVersionAppClipDefaultExperienceLinkageRequest](./appstoreversionappclipdefaultexperiencelinkagerequest.md)
  The request body you use to attach a default App Clip experience to an App Store version.
- [object AppStoreVersionAppClipDefaultExperienceLinkageResponse](./appstoreversionappclipdefaultexperiencelinkageresponse.md)
  A response that contains the ID of a single related Default App Clip Experiences resource.
- [type AppStoreVersionState](./appstoreversionstate.md)
  String that represents the state of an app version in the App Store.
- [object AppStoreVersionAlternativeDistributionPackageLinkageResponse](./appstoreversionalternativedistributionpackagelinkageresponse.md)
- [object AppStoreVersionAppStoreReviewDetailLinkageResponse](./appstoreversionappstorereviewdetaillinkageresponse.md)
- [object AppStoreVersionAppStoreVersionExperimentsLinkagesResponse](./appstoreversionappstoreversionexperimentslinkagesresponse.md)
- [object AppStoreVersionAppStoreVersionExperimentsV2LinkagesResponse](./appstoreversionappstoreversionexperimentsv2linkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appversionstate)*