# InAppPurchaseImage

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a in-app purchase image resource.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object InAppPurchaseImage
```

## Topics

### Objects
- [object InAppPurchaseImage.Attributes](inapppurchaseimage/attributes-data.dictionary.md)
  Attributes that describe a subscription image resource.
- [object InAppPurchaseImage.Relationships](inapppurchaseimage/relationships-data.dictionary.md)
  The data structure that represents the relationships of a subscription image resource.

## Properties

- `attributes` (InAppPurchaseImage.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (InAppPurchaseImage.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [object InAppPurchaseImageCreateRequest](inapppurchaseimagecreaterequest.md)
  The request body you use to create a in-app purchase purchase image reservation.
- [object InAppPurchaseImageResponse](inapppurchaseimageresponse.md)
  A response that contains a single in-app purchase images resource.
- [object InAppPurchaseImageUpdateRequest](inapppurchaseimageupdaterequest.md)
  The data structure that represents a in-app purchase image resource.
- [object InAppPurchaseImagesResponse](inapppurchaseimagesresponse.md)
  A response that contains a list of in-app purchase image resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseimage)*