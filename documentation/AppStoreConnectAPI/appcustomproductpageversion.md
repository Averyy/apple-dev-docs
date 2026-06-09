# AppCustomProductPageVersion

**Framework**: App Store Connect API  
**Kind**: dictionary

A version of a custom App Store product page, containing its localizations and review status.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppCustomProductPageVersion
```

## Topics

### Objects
- [object AppCustomProductPageVersion.Attributes](appcustomproductpageversion/attributes-data.dictionary.md)
  Attributes that describe an app custom product page version resource.
- [object AppCustomProductPageVersion.Relationships](appcustomproductpageversion/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppCustomProductPageVersion.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppCustomProductPageVersion.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppCustomProductPageVersionCreateRequest](appcustomproductpageversioncreaterequest.md)
  The request body you use to create an app custom product page version.
- [object AppCustomProductPageVersionInlineCreate](appcustomproductpageversioninlinecreate.md)
  An inline object for specifying a custom product page version when creating or updating a related resource.
- [object AppCustomProductPageVersionUpdateRequest](appcustomproductpageversionupdaterequest.md)
  The request body you use to update an app custom product page version.
- [object AppCustomProductPageVersionResponse](appcustomproductpageversionresponse.md)
  The response body for endpoints that create, read, or modify a single custom product page version.
- [object AppCustomProductPageVersionsResponse](appcustomproductpageversionsresponse.md)
  The response body for endpoints that list versions of a custom App Store product page.
- [object AppCustomProductPageVersionAppCustomProductPageLocalizationsLinkagesResponse](appcustomproductpageversionappcustomproductpagelocalizationslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appcustomproductpageversion)*