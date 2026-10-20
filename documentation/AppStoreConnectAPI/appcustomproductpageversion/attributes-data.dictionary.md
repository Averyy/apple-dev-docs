# AppCustomProductPageVersion.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe an app custom product page version resource.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```
object AppCustomProductPageVersion.Attributes
```

## Properties

- `deepLink` (uri)
- `state` (string): **Allowed Values**: `PREPARE_FOR_SUBMISSION`, `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `ACCEPTED`, `APPROVED`, `REPLACED_WITH_NEW_VERSION`, `REJECTED`
- `version` (string)

## See Also

### Objects
- [object AppCustomProductPageVersion.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appcustomproductpageversion/attributes-data.dictionary)*