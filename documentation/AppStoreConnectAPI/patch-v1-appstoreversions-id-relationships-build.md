# Modify the build for an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Change the build that is attached to a specific App Store version.

**Availability**:
- App Store Connect API 1.2+

#### Discussion

Use this endpoint to associate a build with a version. The build you specify represents the build that’s installed when a customer purchases the app on the App Store.

##### Attach a Build to a Version

**Request**:

```None
PATCH https://api.appstoreconnect.apple.com/v1/appStoreVersions/f5b10fc0-afda-4b31-b3e8-cdbcbe945622/relationships/build
{
  "data": {
    "type": "builds",
    "id": "b539f38f-8af4-4fbd-b5fc-fde89aab410f"
  }
}

```

**Response**:

```json
{
  "data": {
    "type": "builds",
    "id": "b539f38f-8af4-4fbd-b5fc-fde89aab410f"
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/f5b10fc0-afda-4b31-b3e8-cdbcbe945622/relationships/build",
    "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/f5b10fc0-afda-4b31-b3e8-cdbcbe945622/build"
  }
}
```

##### Remove the Build From a Version

**Request**:

```None
PATCH /v1/appStoreVersions/f5b10fc0-afda-4b31-b3e8-cdbcbe945622/relationships/build
{
  "data": null
}
```

**Response**:

```json
{
  "data": null,
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/f5b10fc0-afda-4b31-b3e8-cdbcbe945622/relationships/build",
    "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/f5b10fc0-afda-4b31-b3e8-cdbcbe945622/build"
  }
}
```

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/relationships/build`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version resource ID from the [`List all app store versions for an app`](get-v1-apps-_id_-appstoreversions.md) response.

## See Also

- [Read the build information of an app store version](get-v1-appstoreversions-_id_-build.md)
  Get the build that is attached to a specific App Store version.
- [Get the build id for an app store version](get-v1-appstoreversions-_id_-relationships-build.md)
  Get the ID of the build that is attached to a specific App Store version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appstoreversions-_id_-relationships-build)*