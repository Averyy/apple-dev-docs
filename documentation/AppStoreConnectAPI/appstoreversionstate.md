# AppStoreVersionState

**Framework**: App Store Connect API  
**Kind**: typealias

String that represents the state of an app version in the App Store.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
string AppStoreVersionState
```

#### Discussion

- PossibleValues - DEVELOPER_REMOVED_FROM_SALE
- DEVELOPER_REJECTED
- IN_REVIEW
- INVALID_BINARY
- METADATA_REJECTED
- PENDING_APPLE_RELEASE
- PENDING_CONTRACT
- PENDING_DEVELOPER_RELEASE
- PREPARE_FOR_SUBMISSION
- PREORDER_READY_FOR_SALE
- PROCESSING_FOR_APP_STORE
- READY_FOR_SALE
- REJECTED
- REMOVED_FROM_SALE
- WAITING_FOR_EXPORT_COMPLIANCE
- WAITING_FOR_REVIEW
- REPLACED_WITH_NEW_VERSION
- ACCEPTED
- READY_FOR_REVIEW
- NOT_APPLICABLE

## See Also

- [object AppStoreVersionUpdateRequest](appstoreversionupdaterequest.md)
  The request body you use to update an App Store Version.
- [object AgeRatingDeclaration](ageratingdeclaration.md)
  The data structure that represents an Age Rating Declarations resource.
- [object AgeRatingDeclarationWithoutIncludesResponse](ageratingdeclarationwithoutincludesresponse.md)
- [object AppStoreVersion](appstoreversion.md)
  The data structure that represent an App Store Versions resource.
- [object AppStoreVersionResponse](appstoreversionresponse.md)
  A response that contains a single App Store Versions resource.
- [object AppStoreVersionsResponse](appstoreversionsresponse.md)
  A response that contains a list of App Store Version resources.
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
- [type AppVersionState](appversionstate.md)
  String that represents the state of an app version.
- [object AppStoreVersionAgeRatingDeclarationLinkageResponse](appstoreversionageratingdeclarationlinkageresponse.md)
- [object AppStoreVersionAlternativeDistributionPackageLinkageResponse](appstoreversionalternativedistributionpackagelinkageresponse.md)
- [object AppStoreVersionAppStoreReviewDetailLinkageResponse](appstoreversionappstorereviewdetaillinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstoreversionstate)*