# AppInfosResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list an app’s App Store information entries.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppInfosResponse
```

## Properties

- `data` ([AppInfo]) *(required)*: The resource data.
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.

## See Also

- [object AppInfo](appinfo.md)
  The data structure that represent an App Infos resource.
- [object AppInfoResponse](appinforesponse.md)
  The response body for endpoints that read or modify an app’s App Store information.
- [object AppInfoUpdateRequest](appinfoupdaterequest.md)
  The request body you use to update an App Info.
- [object AppInfoAppInfoLocalizationsLinkagesResponse](appinfoappinfolocalizationslinkagesresponse.md)
- [object AppInfoPrimaryCategoryLinkageResponse](appinfoprimarycategorylinkageresponse.md)
- [object AppInfoPrimarySubcategoryOneLinkageResponse](appinfoprimarysubcategoryonelinkageresponse.md)
- [object AppInfoPrimarySubcategoryTwoLinkageResponse](appinfoprimarysubcategorytwolinkageresponse.md)
- [object AppInfoSecondaryCategoryLinkageResponse](appinfosecondarycategorylinkageresponse.md)
- [object AppInfoSecondarySubcategoryOneLinkageResponse](appinfosecondarysubcategoryonelinkageresponse.md)
- [object AppInfoSecondarySubcategoryTwoLinkageResponse](appinfosecondarysubcategorytwolinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appinfosresponse)*