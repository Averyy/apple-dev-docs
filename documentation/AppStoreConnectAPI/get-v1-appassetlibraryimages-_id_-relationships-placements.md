# List the placement IDs for an app asset library image

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of placement resource IDs for a specific app asset library image.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [Uploading and managing image assets](./uploading-and-managing-image-assets.md)

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61/relationships/placements?limit=2
```

**Response**:

```json
{
  "data" : [ {
    "type" : "appAssetLibraryPlacements",
    "id" : "2e000005-e036-8f0b-8f25-6dbc2baa784a"
  }, {
    "type" : "appAssetLibraryPlacements",
    "id" : "1e800005-e036-8f0b-8f37-9c5cc67e23a1"
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61/relationships/placements",
    "related" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61/placements"
  },
  "meta" : {
    "paging" : {
      "total" : 2,
      "limit" : 2
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/{id}/relationships/placements`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

### Query Parameters

- `limit` (integer): The maximum number of app asset library placement resource identifiers to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AppAssetLibraryImagePlacementsLinkagesResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting images and reading information
- [Read an app asset library image](./get-v1-appassetlibraryimages-_id_.md)
  Get information about an app asset library image.
- [List related placements](./get-v1-appassetlibraryimages-_id_-placements.md)
  List the placements that reuse an app asset library image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appassetlibraryimages-_id_-relationships-placements)*