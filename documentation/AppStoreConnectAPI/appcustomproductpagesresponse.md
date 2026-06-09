# AppCustomProductPagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list custom App Store product pages for an app.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppCustomProductPagesResponse
```

## Properties

- `data` ([AppCustomProductPage]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppCustomProductPage](appcustomproductpage.md)
  A custom variant of an app’s App Store product page, used for targeted marketing campaigns.
- [object AppCustomProductPageCreateRequest](appcustomproductpagecreaterequest.md)
  The request body you use to create an app custom product page.
- [object AppCustomProductPageResponse](appcustomproductpageresponse.md)
  The response body for endpoints that create, read, or modify a single custom App Store product page.
- [object AppCustomProductPageUpdateRequest](appcustomproductpageupdaterequest.md)
  The request body you use to update an app custom product page.
- [object AppCustomProductPageAppCustomProductPageVersionsLinkagesResponse](appcustomproductpageappcustomproductpageversionslinkagesresponse.md)
  A response containing the resource identifiers of versions for a custom App Store product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appcustomproductpagesresponse)*