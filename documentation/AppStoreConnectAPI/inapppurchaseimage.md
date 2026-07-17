# InAppPurchaseImage

**Framework**: App Store Connect API  
**Kind**: dictionary

A screenshot or image associated with an in-app purchase or subscription, displayed on the App Store product page.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object InAppPurchaseImage
```

## Topics

### Objects
- [object InAppPurchaseImage.Attributes](inapppurchaseimage/attributes-data.dictionary.md)
  Attributes that describe a subscription image resource.
- [object InAppPurchaseImage.Relationships](inapppurchaseimage/relationships-data.dictionary.md)
  The relationships for an in-app purchase image, linking it to its associated in-app purchase.

## Properties

- `attributes` (InAppPurchaseImage.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (InAppPurchaseImage.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [object InAppPurchaseImageCreateRequest](inapppurchaseimagecreaterequest.md)
  The request body you use to create an in-app purchase image reservation.
- [object InAppPurchaseImageResponse](inapppurchaseimageresponse.md)
  A response containing a single image for an in-app purchase.
- [object InAppPurchaseImageUpdateRequest](inapppurchaseimageupdaterequest.md)
  The request body for updating the upload state or file content of an in-app purchase image.
- [object InAppPurchaseImagesResponse](inapppurchaseimagesresponse.md)
  A response containing a list of images for an in-app purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseimage)*