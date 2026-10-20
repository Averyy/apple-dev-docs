# AppInfoResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that read or modify an app’s App Store information.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```
object AppInfoResponse
```

## Properties

- `data` (AppInfo) *(required)*: The resource data.
- `included` ([*]): **Allowed Types**: `AgeRatingDeclaration`, `AppCategory`, `AppInfoLocalization`, `App`
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

### Objects
- [object AppInfo](./appinfo.md)
  The data structure that represent an App Infos resource.
- [object AppInfosResponse](./appinfosresponse.md)
  The response body for endpoints that list an app’s App Store information entries.
- [object AppInfoUpdateRequest](./appinfoupdaterequest.md)
  The request body you use to update an App Info.
- [object AppInfoAppInfoLocalizationsLinkagesResponse](./appinfoappinfolocalizationslinkagesresponse.md)
- [object AppInfoPrimaryCategoryLinkageResponse](./appinfoprimarycategorylinkageresponse.md)
- [object AppInfoPrimarySubcategoryOneLinkageResponse](./appinfoprimarysubcategoryonelinkageresponse.md)
- [object AppInfoPrimarySubcategoryTwoLinkageResponse](./appinfoprimarysubcategorytwolinkageresponse.md)
- [object AppInfoSecondaryCategoryLinkageResponse](./appinfosecondarycategorylinkageresponse.md)
- [object AppInfoSecondarySubcategoryOneLinkageResponse](./appinfosecondarysubcategoryonelinkageresponse.md)
- [object AppInfoSecondarySubcategoryTwoLinkageResponse](./appinfosecondarysubcategorytwolinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appinforesponse)*