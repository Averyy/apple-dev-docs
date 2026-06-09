# AppInfo

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represent an App Infos resource.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppInfo
```

## Topics

### Objects
- [object AppInfo.Attributes](appinfo/attributes-data.dictionary.md)
  Attributes that describe an App Infos resource.
- [object AppInfo.Relationships](appinfo/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppInfo.Attributes): The resource’s attributes.
- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (AppInfo.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object AppInfoResponse](appinforesponse.md)
  The response body for endpoints that read or modify an app’s App Store information.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appinfo)*