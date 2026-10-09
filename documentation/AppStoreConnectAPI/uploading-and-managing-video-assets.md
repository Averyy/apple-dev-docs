# Uploading and managing video assets

**Framework**: App Store Connect API

Reserve, upload, and commit a video to your app’s asset library, set its preview frame, then update, archive, or delete it.

#### Overview

An asset library video is a reusable video, for example, an app preview, that you upload once and place across your App Store surfaces. Uploading a video follows the same reserve-upload-commit pattern as an image: you create a reservation that returns upload operations, transfer the bytes to those URLs, then commit the reservation so App Store Connect can process the file. Videos add one step: a preview frame that represents the video before it plays.

For more information about the shared, four-step asset delivery model, see [`Uploading Assets to App Store Connect`](uploading-assets-to-app-store-connect.md). For the image walkthrough, which this article parallels closely, see [`Uploading and managing image assets`](uploading-and-managing-image-assets.md). For the broader concept, see [`Understanding the App Asset Library`](understanding-the-app-asset-library.md).

#### Confirm Specifications Before You Begin

Find your app’s asset library and look up the video specifications for the placement types you’re targeting:

- Read the library with `GET /v1/apps/{id}/assetLibrary` ([`Read related asset library`](get-v1-apps-_id_-assetlibrary.md)) and note the returned `appAssetLibraries` `id`.
- Query the reference data with `GET /v1/appAssetLibraryRefData` ([`List app asset library ref data`](get-v1-appassetlibraryrefdata.md)) to read the valid `videoSpecs` for those placement types. For more information about specifications, see [`Discovering asset specifications`](discovering-asset-specifications.md).

Video specifications constrain more than images do. In addition to dimensions and formats, each specification states permitted frame-rate ranges in `frameRates`, a `duration` range as ISO 8601 durations, and whether an audio track is required:

```json
{
  "specId": "1861fdcb-eb99-59e6-8c6c-5a07479d9a84",
  "shortName": "v1920x886f23~30t15~30u1",
  "dimensions": { "minWidth": 1920, "maxWidth": 1920, "minHeight": 886, "maxHeight": 886 },
  "aspectRatio": "13:6",
  "compatiblePlacementTypes": ["APP_PREVIEW"],
  "frameRates": [{ "minFps": 23, "maxFps": 30 }],
  "duration": { "min": "PT15S", "max": "PT30S" },
  "audioRequired": true,
  "fileExtensions": [".mp4", ".m4v", ".mov"],
  "mimeTypes": ["video/quicktime", "video/mp4", "video/x-m4v"],
  "maxFileSize": 524288000
}
```

Check your footage against all of these before you create the reservation. App Store Connect doesn’t validate the footage until after the upload, so a video that runs 12 seconds, or has no audio track where `audioRequired` is `true`, fails processing rather than being rejected up front.

#### Reserve the Video

Reserving a video creates its record in your asset library and returns the upload operations you use to send the file. The video stays in `AWAITING_UPLOAD` until you commit the upload. Create the video with `POST /v1/appAssetLibraryVideos` ([`Create an app asset library video`](post-v1-appassetlibraryvideos.md)). Supply the filename, the file size in bytes, and a category ([`AppAssetLibraryAssetCategory`](appassetlibraryassetcategory.md)), and relate the video to your asset library. If you want, set `previewFrameTimeCode` to choose the frame that represents the video, and `referenceName` to identify the asset later.

```json
{
  "data": {
    "type": "appAssetLibraryVideos",
    "attributes": {
      "fileName": "ync-preview.mp4",
      "fileSize": 31457280,
      "category": "APP_SCREENSHOTS_AND_PREVIEWS",
      "previewFrameTimeCode": "00:00:03:00",
      "referenceName": "Fall campaign preview"
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

A successful response returns the video `id`, a `state` of `AWAITING_UPLOAD`, and an `uploadOperations` array specifying the `method`, `url`, `length`, `offset`, and `requestHeaders` for each part. As with images, `videoAsset`, `previewFrameImage`, and `specId` are `null` until processing finishes.

#### Upload the Video

Transfer the file to the URLs from `uploadOperations`. For each operation, make an HTTP request using the specified `method`, `url`, and `requestHeaders`, and send the bytes from the given `offset` and `length` in the request body. Because videos are large, expect multiple operations; upload the parts concurrently and in any order, and resend any part that fails before you commit. The upload URLs are unauthenticated and time-limited, so you don’t send a JSON Web Token (JWT), and you don’t share them.

The video stays in `AWAITING_UPLOAD` while you transfer the parts.

#### Commit the Upload

After every part uploads, commit the reservation with `PATCH /v1/appAssetLibraryVideos/{id}` ([`Modify an app asset library video`](patch-v1-appassetlibraryvideos-_id_.md)) by setting `uploaded` to `true`:

```json
{
  "data": {
    "type": "appAssetLibraryVideos",
    "id": "c2d3e4f5-6789-01ab-cdef-234567890abc",
    "attributes": {
      "uploaded": true
    }
  }
}
```

> ❗ **Important**:  Asset library commits take `uploaded` alone. Unlike the deprecated `appPreviews` flow, there’s no `sourceFileChecksum` attribute to send. App Store Connect validates the transfer against the `fileSize` you declared in the reservation, so the commit fails if the bytes received don’t match.

The video moves to `UPLOAD_COMPLETE`, and processing begins.

#### Verify Processing

Processing is asynchronous. Re-fetch the video with `GET /v1/appAssetLibraryVideos/{id}` ([`Read an app asset library video`](get-v1-appassetlibraryvideos-_id_.md)) to check its `state`:

- `UPLOAD_COMPLETE`: App Store Connect received the file and is processing it.
- `PREPARE_FOR_SUBMISSION`: Processing succeeded and the video is ready to place.
- `FAILED`: Processing didn’t succeed. Read `stateDetails` for the reason, then delete the video and start over with a new reservation.

When processing succeeds, read `specId` for the specification to which App Store Connect matched your file, and `videoAsset` for the processed asset URL. You never send `specId` yourself; compare the returned value against the reference data to confirm your file landed on the specification you intended.

#### Set or Change the Preview Frame

The preview frame is the still image that represents the video before playback. Choose it by setting `previewFrameTimeCode` at creation, or by patching it later with `PATCH /v1/appAssetLibraryVideos/{id}` ([`Modify an app asset library video`](patch-v1-appassetlibraryvideos-_id_.md)):

```json
{
  "data": {
    "type": "appAssetLibraryVideos",
    "id": "c2d3e4f5-6789-01ab-cdef-234567890abc",
    "attributes": {
      "previewFrameTimeCode": "00:00:05:00"
    }
  }
}
```

Pick a time code that falls inside the video’s duration. App Store Connect then generates the frame asynchronously. Read `previewFrameImage` on the video to check progress; it carries a nested `state` of `PROCESSING`, `COMPLETE`, or `FAILED`, plus `errors` and `warnings` arrays, and an `image` with the same `templateUrl`, `width`, and `height` shape an image asset uses.

The preview frame belongs to the video, not to any one placement. Changing it changes what every placement of that video displays.

#### Update Archive or Delete a Video

Use `PATCH /v1/appAssetLibraryVideos/{id}` ([`Modify an app asset library video`](patch-v1-appassetlibraryvideos-_id_.md)) to change a video’s `referenceName` or `previewFrameTimeCode`, or to archive it by setting `archived` to `true`. Archiving works only on an approved asset; archiving one that’s still in `PREPARE_FOR_SUBMISSION` returns a 409 with the code `STATE_ERROR.INVALID_ASSET_STATE` and the detail `Only an approved asset can be archived.` The video binary is immutable after commit; to change the footage, upload a new asset and replace the placements that use it.

To remove a video entirely, use `DELETE /v1/appAssetLibraryVideos/{id}` ([`Delete an app asset library video`](delete-v1-appassetlibraryvideos-_id_.md)), which returns `204 No Content` on success.

> ❗ **Important**:  Deleting an asset doesn’t cascade to its placements. Delete every placement that uses the video first, or the request returns a 409 with the code `STATE_ERROR.ASSET_HAS_PLACEMENTS`.

#### Find Video Placements

To see the placements that reuse a video, use `GET /v1/appAssetLibraryVideos/{id}/placements` ([`List related placements`](get-v1-appassetlibraryvideos-_id_-placements.md)), or fetch just the relationship linkages with `GET /v1/appAssetLibraryVideos/{id}/relationships/placements` ([`List the placement IDs for an app asset library video`](get-v1-appassetlibraryvideos-_id_-relationships-placements.md)).

#### List the Videos in Your Library

Read every video in the library with `GET /v1/appAssetLibraries/{id}/videos` ([`List related videos`](get-v1-appassetlibraries-_id_-videos.md)). The same filters and sorts available for images apply: `filter[state]`, `filter[category]`, `filter[specId]`, `filter[referenceName]`, `filter[id]`, and `sort` by `createdDate`, `lastModifiedDate`, or `referenceName`.

After your video reaches `PREPARE_FOR_SUBMISSION`, place it on a surface. For more information, see [`Placing assets on your App Store surfaces`](placing-assets-on-your-app-store-surfaces.md).

## See Also

- [Understanding the App Asset Library](understanding-the-app-asset-library.md)
  Upload an image or video once, then reuse it across your app’s App Store surfaces with per-surface placements.
- [Uploading and managing image assets](uploading-and-managing-image-assets.md)
  Reserve, upload, and commit an image to your app’s asset library, then update, archive, or delete it.
- [Placing assets on your App Store surfaces](placing-assets-on-your-app-store-surfaces.md)
  Create placements that position library assets on App Store surfaces, then set their display order within a localization.
- [Discovering asset specifications](discovering-asset-specifications.md)
  Query the asset library reference data to learn the valid dimensions, formats, placement groups, and limits before you upload.
- [Migrating to the App Asset Library](migrating-to-the-app-asset-library.md)
  Move your screenshots, app previews, and in-app event media from the deprecated set-based resources to the asset library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/uploading-and-managing-video-assets)*