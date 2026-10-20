# Get a Thumbnail

**Framework**: ClassKit Catalog API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch the image for one of your app’s assignable activities.

**Availability**:
- ClassKit 1.0+

## Endpoint

`GET https://classkit-catalog.apple.com/v1/thumbnails`

## Parameters

### Query Parameters

- `environment` (string) *(required)*: The development or production environment to use for this access. For details, see [Testing Your ClassKit Catalog Implementation](./testing-your-classkit-catalog-implementation.md).

  **Allowed Values**: `development`, `production`
- `thumbnailId` (string) *(required)*: The thumbnail identifier for the thumbnail to retrieve. Format this value as a URL-encoded string.

## Responses

- `200` OK: The request succeeded.
- `202` Accepted: The API accepted but hasn’t completed the request. To ask for a status update later, see [`Get Status`](./get-status.md).
- `400` Bad Request: The request contained an error.
- `403` Forbidden: The request wasn’t authorized.

## See Also

### Uploading Thumbnails
- [Create or Replace a Thumbnail](./create-or-replace-a-thumbnail.md)
  Store an image that represents one of your app’s assignable activities.
- [Delete a Thumbnail](./delete-a-thumbnail.md)
  Remove one of the images for your app’s assignable activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/get-a-thumbnail)*