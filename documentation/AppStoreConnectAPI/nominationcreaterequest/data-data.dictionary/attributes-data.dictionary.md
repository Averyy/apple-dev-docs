# NominationCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- App Store Connect API 3.6+

## Declaration

```
object NominationCreateRequest.Data.Attributes
```

## Properties

- `description` (string) *(required)*
- `deviceFamilies` ([DeviceFamily])
- `hasInAppEvents` (boolean)
- `launchInSelectMarketsFirst` (boolean)
- `locales` ([string])
- `name` (string) *(required)*
- `notes` (string)
- `preOrderEnabled` (boolean)
- `publishEndDate` (date-time)
- `publishStartDate` (date-time) *(required)*
- `submitted` (boolean) *(required)*
- `supplementalMaterialsUris` ([uri])
- `type` (string) *(required)*: **Allowed Values**: `APP_LAUNCH`, `APP_ENHANCEMENTS`, `NEW_CONTENT`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/nominationcreaterequest/data-data.dictionary/attributes-data.dictionary)*