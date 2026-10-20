# Profile.Attributes

**Framework**: Enterprise Program API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a Profiles resource.

## Declaration

```
object Profile.Attributes
```

## Properties

- `createdDate` (date-time)
- `expirationDate` (date-time)
- `name` (string)
- `platform` (BundleIdPlatform)
- `profileContent` (string)
- `profileState` (string): **Allowed Values**: `ACTIVE`, `INVALID`
- `profileType` (string): **Allowed Values**: `IOS_APP_DEVELOPMENT`, `IOS_APP_STORE`, `IOS_APP_ADHOC`, `IOS_APP_INHOUSE`, `MAC_APP_DEVELOPMENT`, `MAC_APP_STORE`, `MAC_APP_DIRECT`, `TVOS_APP_DEVELOPMENT`, `TVOS_APP_STORE`, `TVOS_APP_ADHOC`, `TVOS_APP_INHOUSE`, `MAC_CATALYST_APP_DEVELOPMENT`, `MAC_CATALYST_APP_STORE`, `MAC_CATALYST_APP_DIRECT`
- `uuid` (string)

## See Also

### Objects
- [object Profile.Relationships](./relationships-data.dictionary.md)
  The relationships you included in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/profile/attributes-data.dictionary)*