# Get the asset library ID for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the asset library resource ID for a specific app.

**Availability**:
- App Store Connect API 4.5+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/1234567890/relationships/assetLibrary
```

**Response**:

```json
{
  "data" : {
    "type" : "appAssetLibraries",
    "id" : "1234567890"
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/apps/1234567890/relationships/assetLibrary",
    "related" : "https://api.appstoreconnect.apple.com/v1/apps/1234567890/assetLibrary"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/relationships/assetLibrary`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Read related asset library](get-v1-apps-_id_-assetlibrary.md)
  Get the asset library for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-relationships-assetlibrary)*