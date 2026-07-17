# Create an image for a subscription (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest

Reserve an image asset to appear in the App Store, representing a subscription.

**Availability**:
- App Store Connect API 3.6+

## Mentions

- [Creating and configuring win-back offers](creating-and-configuring-win-back-offers.md)

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionImages`

## See Also

- [Read subscription image information (v1)](get-v1-subscriptionimages-_id_.md)
  Read details about a specific subscription image.
- [List Subscription Images](get-v1-subscriptions-_id_-images.md)
  List all images for a specific subscription.
- [List subscription image ids](get-v1-subscriptions-_id_-relationships-images.md)
  List all images IDs for a specific subscription.
- [Commit a subscription image (v1)](patch-v1-subscriptionimages-_id_.md)
  Commit an uploaded subscription image.
- [Delete a subscription image (v1)](delete-v1-subscriptionimages-_id_.md)
  Delete the image asset that appears on the App Store listing that represents a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptionimages)*