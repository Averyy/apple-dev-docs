# AppInfoResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read or modify an app’s App Store information.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppInfoResponse
```

## Properties

- `data` (AppInfo) *(required)*: The resource data.
- `included` ([*])
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [object AppInfo](appinfo.md)
  The data structure that represent an App Infos resource.
- [object AppInfosResponse](appinfosresponse.md)
  The response body for endpoints that list an app’s App Store information entries.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appinforesponse)*