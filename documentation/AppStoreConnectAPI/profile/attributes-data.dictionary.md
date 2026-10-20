# Profile.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a Profiles resource.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```
object Profile.Attributes
```

## Properties

- `name` (string)
- `platform` (BundleIdPlatform)
- `profileContent` (string)
- `uuid` (string)
- `createdDate` (date-time)
- `profileState` (string): **Allowed Values**: `ACTIVE`, `INVALID`
- `profileType` (string): **Allowed Values**: `IOS_APP_DEVELOPMENT`, `IOS_APP_STORE`, `IOS_APP_ADHOC`, `IOS_APP_INHOUSE`, `MAC_APP_DEVELOPMENT`, `MAC_APP_STORE`, `MAC_APP_DIRECT`, `TVOS_APP_DEVELOPMENT`, `TVOS_APP_STORE`, `TVOS_APP_ADHOC`, `TVOS_APP_INHOUSE`, `MAC_CATALYST_APP_DEVELOPMENT`, `MAC_CATALYST_APP_STORE`, `MAC_CATALYST_APP_DIRECT`
- `expirationDate` (date-time)

## See Also

### Objects
- [object Profile.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/profile/attributes-data.dictionary)*