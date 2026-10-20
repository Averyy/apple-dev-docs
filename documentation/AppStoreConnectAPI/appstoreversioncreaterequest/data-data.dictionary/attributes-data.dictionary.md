# AppStoreVersionCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that you set that describe the new resource.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```
object AppStoreVersionCreateRequest.Data.Attributes
```

## Properties

- `copyright` (string)
- `earliestReleaseDate` (date-time)
- `platform` (Platform) *(required)*
- `releaseType` (string): **Allowed Values**: `MANUAL`, `AFTER_APPROVAL`, `SCHEDULED`
- `reviewType` (string): **Allowed Values**: `APP_STORE`, `NOTARIZATION`
- `usesIdfa` (boolean) *(deprecated)*
- `versionString` (string) *(required)*

## See Also

### Objects
- [object AppStoreVersionCreateRequest.Data.Relationships](./relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstoreversioncreaterequest/data-data.dictionary/attributes-data.dictionary)*