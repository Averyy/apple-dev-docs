# Get a Thumbnail

**Framework**: ClassKit Catalog API  
**Kind**: httpRequest

Fetch the image for one of your app’s assignable activities.

**Availability**:
- ClassKit 1.0+

## Endpoint

`GET https://classkit-catalog.apple.com/v1/thumbnails`

## Parameters

- `environment` (string) *(required)*: The development or production environment to use for this access. For details, see [`Testing Your ClassKit Catalog Implementation`](testing-your-classkit-catalog-implementation.md).
- `thumbnailId` (string) *(required)*: The thumbnail identifier for the thumbnail to retrieve. Format this value as a URL-encoded string.

## See Also

- [Create or Replace a Thumbnail](create-or-replace-a-thumbnail.md)
  Store an image that represents one of your app’s assignable activities.
- [Delete a Thumbnail](delete-a-thumbnail.md)
  Remove one of the images for your app’s assignable activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/get-a-thumbnail)*