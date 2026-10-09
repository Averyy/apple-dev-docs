# Migrating to the App Asset Library

**Framework**: App Store Connect API

Move your screenshots, app previews, and in-app event media from the deprecated set-based resources to the asset library.

#### Overview

The asset library replaces an approach where each App Store surface owned its own media. When you use the asset library, you upload each image or video once into a per-app library, then create placements that position it on surfaces.

In the previous approach, you created an app screenshot set for a specific display target, uploaded screenshots into it, and repeated the whole process for every localization, every custom product page, and every in-app event. The same image uploaded ten times became ten separate records. This article maps the concepts from the new approach onto the previous one and walks through converting an existing integration.

For more information about the App Asset Library, see [`Understanding the App Asset Library`](understanding-the-app-asset-library.md).

#### Compare the Two Models

The asset library replaces the set-based resources, which are deprecated:

| Asset library | Deprecated resource |
| --- | --- |
| Placement type and placement group on a placement | [`App Screenshot Sets`](app-screenshot-sets.md) |
| [`App Asset Library images`](app-asset-library-images.md) plus a placement | [`App Screenshots`](app-screenshots.md) |
| Placement type and placement group on a placement | [`App Preview Sets`](app-preview-sets.md) |
| [`App Asset Library videos`](app-asset-library-videos.md) plus a placement | [`App Previews`](app-previews.md) |
| [`App Asset Library images`](app-asset-library-images.md) plus a placement | [`App Event Screenshots`](app-event-screenshots.md) |
| [`App Asset Library videos`](app-asset-library-videos.md) plus a placement | [`App Event Video Clips`](app-event-video-clips.md) |
| Placement type and placement group on a placement | [`App Custom Product Page Screenshot Sets`](app-custom-product-page-screenshot-sets.md) |
| [`App Asset Library images`](app-asset-library-images.md) plus a placement | [`App Custom Product Page Screenshots`](app-custom-product-page-screenshots.md) |
| Placement type and placement group on a placement | [`App Custom Product Page App Preview Sets`](app-custom-product-page-app-preview-sets.md) |
| [`App Asset Library videos`](app-asset-library-videos.md) plus a placement | [`App Custom Product Page App Previews`](app-custom-product-page-app-previews.md) |

There are several conceptual shifts with the new asset library approach:

- **Sets disappear.** A set existed to group media by display target within one localization. A placement carries its `placementType` and `placementGroup` directly, so there’s no container to create first. One fewer resource, one fewer round trip.
- **Assets are separate from their position.** Previously, a screenshot record *was* its position on a product page. Now, an asset lives in the library and a placement points at it, which makes reuse possible.
- **Display targets become placement groups.** Placement group identifiers that you read from the reference data replace the old display-type enumeration values.
- **Checksums go away.** Committing an upload takes `uploaded` alone. There’s no `sourceFileChecksum` to compute.
- **Ordering is explicit.** Instead of patching an ordered list of relationships on a set, post an ordering request naming the placements in sequence.

#### Rewrite the Upload Sequence

The new sequence removes the set and the checksum that the previous approach used. Previously, a screenshot upload took four resource-touching steps: find or create the screenshot set, reserve the screenshot against that set, upload the parts, then commit with a filename, size, and checksum.

Now, the steps are:

1. Read the app’s asset library once with `GET /v1/apps/{id}/assetLibrary` ([`Read related asset library`](get-v1-apps-_id_-assetlibrary.md)). Cache the `id`; every asset you create relates to it. The library ID is stable for the life of the app.
2. Reserve the asset with `POST /v1/appAssetLibraryImages` ([`Create an app asset library image`](post-v1-appassetlibraryimages.md)) or `POST /v1/appAssetLibraryVideos` ([`Create an app asset library video`](post-v1-appassetlibraryvideos.md)), relating it to the library rather than to a set.
3. Upload the parts exactly as before, using the returned `uploadOperations`.
4. Commit with `uploaded: true`, and nothing else.
5. Create a placement with `POST /v1/appAssetLibraryPlacements` ([`Create an app asset library placement`](post-v1-appassetlibraryplacements.md)) naming the `placementType`, the `placementGroup`, the asset, and the target localization.

Steps 1 through 4 run once per distinct file. Step 5 repeats for each place the file appears, which is where the savings come from.

#### Replace Display Targets with Placement Groups

One of the biggest changes with the asset library approach is that display-target constants become runtime lookups. Your code now reads `placementProfileGroups` and `placementTypes` from the reference data and maps a target device family to a placement group identifier such as `IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE`; previously, it held a table of display types.

Do this lookup rather than hard-coding the strings. Apple adds new device families to the reference data without an API version change, so an integration that reads the catalog picks them up and one that hard-codes it doesn’t.

Specifications behave the same way. You no longer decide which specification a file satisfies; App Store Connect matches the file during processing and reports the result as `specId`. Read that value back and confirm it’s the specification you intended. For more information about specifications, see [`Discovering asset specifications`](discovering-asset-specifications.md).

#### Understand Asset Library Deduplication

The asset library makes manual deduplication unnecessary: upload each file once, then create a placement per surface. You no longer need to hash each file, remember which localizations already have it, and can skip redundant uploads.

The practical consequence of the new approach is that your local bookkeeping changes shape. Instead of tracking “which screenshot record belongs to which set,” track “which library asset backs which placements.” Query it directly rather than storing it: `GET /v1/appAssetLibraryImages/{id}/placements` ([`List related placements`](get-v1-appassetlibraryimages-_id_-placements.md)) returns every placement that uses an asset.

#### Watch the Deletion Order

Asset library deletes don’t cascade like set-based deletes do, where removing a screenshot set removed its screenshots. You can’t delete an asset that has placements; the request fails with the code `STATE_ERROR.ASSET_HAS_PLACEMENTS`.

> ❗ **Important**:  Delete the placements first, then the asset. This reverses the previous deletion order, where you deleted a set and let its media go with it. Cleanup code that you carry over unchanged fails on the asset delete.

#### Plan the Transition

A migration that runs in one pass per app works well:

1. Read the reference data and build your device-family-to-placement-group map.
2. Read the app’s asset library ID.
3. For each distinct source file, upload it once and record the returned asset ID against your own identifier for that file.
4. Create a placement referring to the corresponding asset for each localization and display target you previously populated.
5. Post an ordering request per placement group to restore the display order.
6. Verify by reading each localization’s `placements` relationship with `sort=placementGroupPosition`.

You can only create placements while the parent surface is editable, so migrate against an App Store version in `PREPARE_FOR_SUBMISSION` rather than one that’s already approved.

> **Note**:  Migrate per app and verify before moving on. A partial migration leaves uploaded assets with no placements. That’s harmless, and because assets and placements are separate resources, you can resume by creating the missing placements rather than re-uploading.

## See Also

- [Understanding the App Asset Library](understanding-the-app-asset-library.md)
  Upload an image or video once, then reuse it across your app’s App Store surfaces with per-surface placements.
- [Uploading and managing image assets](uploading-and-managing-image-assets.md)
  Reserve, upload, and commit an image to your app’s asset library, then update, archive, or delete it.
- [Uploading and managing video assets](uploading-and-managing-video-assets.md)
  Reserve, upload, and commit a video to your app’s asset library, set its preview frame, then update, archive, or delete it.
- [Placing assets on your App Store surfaces](placing-assets-on-your-app-store-surfaces.md)
  Create placements that position library assets on App Store surfaces, then set their display order within a localization.
- [Discovering asset specifications](discovering-asset-specifications.md)
  Query the asset library reference data to learn the valid dimensions, formats, placement groups, and limits before you upload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/migrating-to-the-app-asset-library)*