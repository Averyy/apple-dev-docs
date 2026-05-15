# Read Subscription Image Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read details about a specific subscription image.

**Availability**:
- App Store Connect API 3.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionImages/{id}`

## Parameters

- `fields[subscriptionImages]` ([string])
- `fields[subscriptions]` ([string])
- `include` ([string])

## See Also

- [Create an Image for a Subscription](post-v1-subscriptionimages.md)
  Reserve an image asset to appear in the App Store, representing a subscription.
- [List Subscription Images](get-v1-subscriptions-_id_-images.md)
  List all images for a specific subscription.
- [GET /v1/subscriptions/{id}/relationships/images](get-v1-subscriptions-_id_-relationships-images.md)
- [Read Subscription Image Information](patch-v1-subscriptionimages-_id_.md)
  Read details about a specific subscription image.
- [Delete an Subscription Image](delete-v1-subscriptionimages-_id_.md)
  Delete the image asset that appears on the App Store listing that represents an subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionimages-_id_)*