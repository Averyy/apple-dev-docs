# AppCustomProductPageVersionInlineCreate

**Framework**: App Store Connect API  
**Kind**: dictionary

An inline object for specifying a custom product page version when creating or updating a related resource.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppCustomProductPageVersionInlineCreate
```

## Topics

### Objects
- [object AppCustomProductPageVersionInlineCreate.Attributes](appcustomproductpageversioninlinecreate/attributes-data.dictionary.md)
  Attributes that describe an app custom product page version inline create resource.
- [object AppCustomProductPageVersionInlineCreate.Relationships](appcustomproductpageversioninlinecreate/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppCustomProductPageVersionInlineCreate.Attributes)
- `id` (string)
- `relationships` (AppCustomProductPageVersionInlineCreate.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppCustomProductPageVersion](appcustomproductpageversion.md)
  A version of a custom App Store product page, containing its localizations and review status.
- [object AppCustomProductPageVersionCreateRequest](appcustomproductpageversioncreaterequest.md)
  The request body you use to create an app custom product page version.
- [object AppCustomProductPageVersionUpdateRequest](appcustomproductpageversionupdaterequest.md)
  The request body you use to update an app custom product page version.
- [object AppCustomProductPageVersionResponse](appcustomproductpageversionresponse.md)
  The response body for endpoints that create, read, or modify a single custom product page version.
- [object AppCustomProductPageVersionsResponse](appcustomproductpageversionsresponse.md)
  The response body for endpoints that list versions of a custom App Store product page.
- [object AppCustomProductPageVersionAppCustomProductPageLocalizationsLinkagesResponse](appcustomproductpageversionappcustomproductpagelocalizationslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appcustomproductpageversioninlinecreate)*