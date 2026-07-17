# InAppPurchaseImagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of images for an in-app purchase.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object InAppPurchaseImagesResponse
```

## Properties

- `data` ([InAppPurchaseImage]) *(required)*
- `included` ([InAppPurchaseV2])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object InAppPurchaseImage](inapppurchaseimage.md)
  A screenshot or image associated with an in-app purchase or subscription, displayed on the App Store product page.
- [object InAppPurchaseImageCreateRequest](inapppurchaseimagecreaterequest.md)
  The request body you use to create an in-app purchase image reservation.
- [object InAppPurchaseImageResponse](inapppurchaseimageresponse.md)
  A response containing a single image for an in-app purchase.
- [object InAppPurchaseImageUpdateRequest](inapppurchaseimageupdaterequest.md)
  The request body for updating the upload state or file content of an in-app purchase image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseimagesresponse)*