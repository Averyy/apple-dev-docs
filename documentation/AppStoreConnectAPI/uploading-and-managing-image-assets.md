# Uploading and managing image assets

**Framework**: App Store Connect API

Reserve, upload, and commit an image to your app’s asset library, then update, archive, or delete it.

#### Overview

An asset library image is a reusable image you upload once and place across your App Store surfaces. Uploading one follows the same reserve-upload-commit pattern as other App Store Connect assets: you create a reservation that returns upload operations, transfer the bytes to those URLs, then commit the reservation so App Store Connect can process the file. This article walks through that workflow and the management operations that follow.

For the shared four-step asset delivery model, see [`Uploading Assets to App Store Connect`](uploading-assets-to-app-store-connect.md). For the broader asset library concept, see [`Understanding the App Asset Library`](understanding-the-app-asset-library.md).

#### Confirm Specifications Before You Begin

Find your app’s asset library and confirm the image specifications:

- Read the library with `GET /v1/apps/{id}/assetLibrary` ([`Read related asset library`](get-v1-apps-_id_-assetlibrary.md)) and note the returned `appAssetLibraries` `id`. You relate every image you upload to this library.
- Query the reference data with `GET /v1/appAssetLibraryRefData` ([`List app asset library ref data`](get-v1-appassetlibraryrefdata.md)) to read the valid `imageSpecs` (dimensions, aspect ratios, allowed file extensions, and maximum file sizes) for the placement types you’re targeting. For more information about specifications, see [`Discovering asset specifications`](discovering-asset-specifications.md).

Image specifications state exact dimensions, not ranges. Resize your file to match a specification before you reserve it; App Store Connect matches the file you upload against the catalog during processing.

#### Reserve the Image

Create the image with `POST /v1/appAssetLibraryImages` ([`Create an app asset library image`](post-v1-appassetlibraryimages.md)). Supply the filename, the file size in bytes, and a category ([`AppAssetLibraryAssetCategory`](appassetlibraryassetcategory.md)), and relate the image to your asset library. The `referenceName` attribute is optional and helps you identify the asset later.

```json
{
  "data": {
    "type": "appAssetLibraryImages",
    "attributes": {
      "fileName": "ync-menu-6-9.png",
      "fileSize": 14619,
      "category": "APP_SCREENSHOTS_AND_PREVIEWS",
      "referenceName": "Menu screen — iPhone 6.9\""
    },
    "relationships": {
      "assetLibrary": {
        "data": {
          "type": "appAssetLibraries",
          "id": "1234567890"
        }
      }
    }
  }
}
```

A successful response returns the image `id`, a `state` of `AWAITING_UPLOAD`, and an `uploadOperations` array. Each operation specifies the HTTP `method`, `url`, `length`, `offset`, and `requestHeaders` to use when you transfer the bytes:

```json
{
  "data": {
    "type": "appAssetLibraryImages",
    "id": "f4000005-e036-8f0b-8018-d259974bee61",
    "attributes": {
      "category": "APP_SCREENSHOTS_AND_PREVIEWS",
      "createdDate": "2026-08-11T22:44:12.019637Z",
      "lastModifiedDate": "2026-08-11T22:44:12.019637Z",
      "fileName": "ync-menu-6-9.png",
      "fileSize": 14619,
      "imageAsset": null,
      "referenceName": "Menu screen — iPhone 6.9\"",
      "specId": null,
      "state": "AWAITING_UPLOAD",
      "stateDetails": null,
      "uploadOperations": [
        {
          "method": "PUT",
          "url": "https://store-030.blobstore.apple.com/...",
          "length": 14619,
          "offset": 0,
          "requestHeaders": [
            { "name": "Content-Type", "value": "image/png" }
          ]
        }
      ]
    }
  }
}
```

Note the `id`; you use it to upload, commit, and later manage the image. `imageAsset` and `specId` are `null` at this stage; App Store Connect fills both in after processing.

#### Upload the Image

Transfer the file to the URLs from `uploadOperations`. For each operation, make an HTTP request using the specified `method`, `url`, and `requestHeaders`, and send the bytes from the given `offset` and `length` in the request body. Large files return multiple operations; upload the parts concurrently and in any order to improve performance. The upload URLs are unauthenticated and time-limited, so you don’t send a JSON Web Token (JWT), and you don’t share them.

The image stays in `AWAITING_UPLOAD` while you transfer the parts.

#### Commit the Upload

After every part uploads, commit the reservation with `PATCH /v1/appAssetLibraryImages/{id}` ([`Modify an app asset library image`](patch-v1-appassetlibraryimages-_id_.md)) by setting `uploaded` to `true`:

```json
{
  "data": {
    "type": "appAssetLibraryImages",
    "id": "f4000005-e036-8f0b-8018-d259974bee61",
    "attributes": {
      "uploaded": true
    }
  }
}
```

> ❗ **Important**:  Asset library commits take `uploaded` alone. Unlike the deprecated `appScreenshots` flow, there’s no `sourceFileChecksum` attribute to send. App Store Connect validates the transfer against the `fileSize` you declared in the reservation, so the commit fails if the bytes received don’t match.

The image moves to `UPLOAD_COMPLETE`, and processing begins.

#### Verify Processing

Processing is asynchronous. Re-fetch the image with `GET /v1/appAssetLibraryImages/{id}` ([`Read an app asset library image`](get-v1-appassetlibraryimages-_id_.md)) to check its `state`:

- `UPLOAD_COMPLETE`: App Store Connect received the file and is processing it.
- `PREPARE_FOR_SUBMISSION`: Processing succeeded and the image is ready to place.
- `FAILED`: Processing didn’t succeed. Read `stateDetails` for the reason, then delete the image and start over with a new reservation.

When processing succeeds, three attributes become readable. Here’s the example response, truncated for clarity:

```json
{
  "fileName": "ync-menu-6-9.png",
  "state": "PREPARE_FOR_SUBMISSION",
  "specId": "f56c777c-99ea-5760-97ae-27c5f8cbb884",
  "imageAsset": {
    "templateUrl": "https://is1.mzstatic.com/image/thumb/AOsFKpK1JfF_vrxSCSbIew/{w}x{h}bb.{f}",
    "width": 1290,
    "height": 2796
  }
}
```

`specId` is the specification to which App Store Connect matched your file, in this case the 1290×2796 iPhone screenshot specification. You never send `specId` yourself. Compare the returned value against the reference data to confirm your file landed on the specification you intended, because a file that matches a different specification limits which placement groups accept it.

Read `imageAsset` for the processed image: substitute width, height, and format into `templateUrl` to render a thumbnail.

#### Update an Image

Use `PATCH /v1/appAssetLibraryImages/{id}` ([`Modify an app asset library image`](patch-v1-appassetlibraryimages-_id_.md)) to change an image’s `referenceName`. The image binary is immutable after commit; to change the picture, upload a new asset and replace the placements that use it.

```json
{
  "data": {
    "type": "appAssetLibraryImages",
    "id": "f4000005-e036-8f0b-8018-d259974bee61",
    "attributes": {
      "referenceName": "Menu screen (Fall 2026)"
    }
  }
}
```

#### Archive an Image

To retire an image without removing its record, set `archived` to `true` with the same `PATCH` endpoint. Archiving moves the image to `ARCHIVED` and hides it from active use.

Archiving works only on an approved asset. Archiving one that’s still in `PREPARE_FOR_SUBMISSION` returns a 409:

```json
{
  "errors": [
    {
      "status": "409",
      "code": "STATE_ERROR.INVALID_ASSET_STATE",
      "title": "The request cannot be fulfilled because of the state of another resource.",
      "detail": "Only an approved asset can be archived."
    }
  ]
}
```

#### Delete an Image

To remove an image entirely, use `DELETE /v1/appAssetLibraryImages/{id}` ([`Delete an app asset library image`](delete-v1-appassetlibraryimages-_id_.md)), which returns `204 No Content` on success.

> ❗ **Important**:  Deleting an asset doesn’t cascade to its placements. Delete every placement that uses the image first, or the request returns a 409 with the code `STATE_ERROR.ASSET_HAS_PLACEMENTS` and the detail `The asset cannot be deleted while placements still use it. Delete those placements first.`

#### Find Image Placements

To see the placements that reuse an image, use `GET /v1/appAssetLibraryImages/{id}/placements` ([`List related placements`](get-v1-appassetlibraryimages-_id_-placements.md)), or fetch just the relationship linkages with `GET /v1/appAssetLibraryImages/{id}/relationships/placements` ([`List the placement IDs for an app asset library image`](get-v1-appassetlibraryimages-_id_-relationships-placements.md)).

This is also the check to run before a delete. Filter by surface, for example, `filter[appStoreVersionLocalization]`, or by `filter[placementType]` and `filter[placementGroup]` to narrow the results.

#### List the Images in Your Library

Read the whole library with `GET /v1/appAssetLibraries/{id}/images` ([`List related images`](get-v1-appassetlibraries-_id_-images.md)). Useful filters and sorts:

- `filter[state]`: Find assets stuck in `AWAITING_UPLOAD`, or list only `APPROVED` ones.
- `filter[category]`, `filter[specId]`, `filter[referenceName]`, `filter[id]`.
- `sort` by `createdDate`, `lastModifiedDate`, or `referenceName`. Prefix with `-` to reverse.

Filtering on `filter[state]=AWAITING_UPLOAD` is a practical way to find abandoned reservations and clean them up.

After your image reaches `PREPARE_FOR_SUBMISSION`, place it on a surface. For more information, see [`Placing assets on your App Store surfaces`](placing-assets-on-your-app-store-surfaces.md).

## See Also

- [Understanding the App Asset Library](understanding-the-app-asset-library.md)
  Upload an image or video once, then reuse it across your app’s App Store surfaces with per-surface placements.
- [Uploading and managing video assets](uploading-and-managing-video-assets.md)
  Reserve, upload, and commit a video to your app’s asset library, set its preview frame, then update, archive, or delete it.
- [Placing assets on your App Store surfaces](placing-assets-on-your-app-store-surfaces.md)
  Create placements that position library assets on App Store surfaces, then set their display order within a localization.
- [Discovering asset specifications](discovering-asset-specifications.md)
  Query the asset library reference data to learn the valid dimensions, formats, placement groups, and limits before you upload.
- [Migrating to the App Asset Library](migrating-to-the-app-asset-library.md)
  Move your screenshots, app previews, and in-app event media from the deprecated set-based resources to the asset library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/uploading-and-managing-image-assets)*