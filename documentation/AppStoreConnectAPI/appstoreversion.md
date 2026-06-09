# AppStoreVersion

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represent an App Store Versions resource.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppStoreVersion
```

## Topics

### Objects
- [object AppStoreVersion.Attributes](appstoreversion/attributes-data.dictionary.md)
  Attributes that describe an App Store Versions resource.
- [object AppStoreVersion.Relationships](appstoreversion/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppStoreVersion.Attributes)
- `id` (string) *(required)*
- `relationships` (AppStoreVersion.Relationships)
- `type` (string) *(required)*
- `links` (ResourceLinks)

## See Also

- [object AppStoreVersionUpdateRequest](appstoreversionupdaterequest.md)
  The request body you use to update an App Store Version.
- [object AgeRatingDeclaration](ageratingdeclaration.md)
  A set of content descriptors for your app that App Store Connect uses to assign an age rating.
- [object AppStoreVersionResponse](appstoreversionresponse.md)
  The response body for endpoints that create, read, or modify an App Store version.
- [object AppStoreVersionsResponse](appstoreversionsresponse.md)
  The response body for endpoints that list App Store versions for an app.
- [object AppStoreVersionCreateRequest](appstoreversioncreaterequest.md)
  The request body you use to create an App Store Version.
- [object AppStoreVersionBuildLinkageRequest](appstoreversionbuildlinkagerequest.md)
  The request body you use to attach a build to an App Store version.
- [object AppStoreVersionBuildLinkageResponse](appstoreversionbuildlinkageresponse.md)
  A response body that contains the ID of a single related resource.
- [object AppStoreVersionAppClipDefaultExperienceLinkageRequest](appstoreversionappclipdefaultexperiencelinkagerequest.md)
  The request body you use to attach a default App Clip experience to an App Store version.
- [object AppStoreVersionAppClipDefaultExperienceLinkageResponse](appstoreversionappclipdefaultexperiencelinkageresponse.md)
  A response that contains the ID of a single related Default App Clip Experiences resource.
- [type AppStoreVersionState](appstoreversionstate.md)
  String that represents the state of an app version in the App Store.
- [type AppVersionState](appversionstate.md)
  String that represents the state of an app version.
- [object AppStoreVersionAlternativeDistributionPackageLinkageResponse](appstoreversionalternativedistributionpackagelinkageresponse.md)
- [object AppStoreVersionAppStoreReviewDetailLinkageResponse](appstoreversionappstorereviewdetaillinkageresponse.md)
- [object AppStoreVersionAppStoreVersionExperimentsLinkagesResponse](appstoreversionappstoreversionexperimentslinkagesresponse.md)
- [object AppStoreVersionAppStoreVersionExperimentsV2LinkagesResponse](appstoreversionappstoreversionexperimentsv2linkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstoreversion)*