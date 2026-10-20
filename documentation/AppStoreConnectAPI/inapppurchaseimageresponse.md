# InAppPurchaseImageResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing a single image for an In-App Purchase.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This object is deprecated. Use [`InAppPurchaseImageV2Response`](./inapppurchaseimagev2response.md) instead.

## Declaration

```
object InAppPurchaseImageResponse
```

## Properties

- `data` (InAppPurchaseImage) *(required)*
- `included` ([InAppPurchaseV2])
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object InAppPurchaseImage](./inapppurchaseimage.md)
  A screenshot or image associated with an In-App Purchase or subscription, displayed on the App Store product page.
- [object InAppPurchaseImageCreateRequest](./inapppurchaseimagecreaterequest.md)
  The request body you use to create an In-App Purchase image reservation.
- [object InAppPurchaseImageUpdateRequest](./inapppurchaseimageupdaterequest.md)
  The request body for updating the upload state or file content of an In-App Purchase image.
- [object InAppPurchaseImagesResponse](./inapppurchaseimagesresponse.md)
  A response containing a list of images for an In-App Purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseimageresponse)*