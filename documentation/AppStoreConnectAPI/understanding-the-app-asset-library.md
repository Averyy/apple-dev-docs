# Understanding the App Asset Library

**Framework**: App Store Connect API

Upload an image or video once, then reuse it across your app’s App Store surfaces with per-surface placements.

#### Overview

The App Asset Library gives your app a single, shared collection of marketing and product media. Instead of uploading the same screenshot or app preview separately to every App Store version, custom product page, and in-app event, you upload each asset once into the library and then create *placements* that position it on specific surfaces. One asset can back many placements at the same time.

This article explains how the pieces fit together. For the step-by-step workflows, see [`Uploading and managing image assets`](uploading-and-managing-image-assets.md), [`Uploading and managing video assets`](uploading-and-managing-video-assets.md), and [`Placing assets on your App Store surfaces`](placing-assets-on-your-app-store-surfaces.md). For a comparison of the App Asset Library and the previous approach, see [`Migrating to the App Asset Library`](migrating-to-the-app-asset-library.md).

#### Understand the Model

The asset library is built from a small set of resources:

- **Asset library**: The per-app container that holds every reusable asset. Each app has exactly one library, reachable through the app’s `assetLibrary` relationship. For more information, see [`App Asset Libraries`](app-asset-libraries.md).
- **Image and video assets**: The reusable media you upload. You upload each [`AppAssetLibraryImage`](appassetlibraryimage.md) or [`AppAssetLibraryVideo`](appassetlibraryvideo.md) once, and App Store Connect processes it once. The asset then lives in the library independently of where it appears. For more information, see [`App Asset Library images`](app-asset-library-images.md) and [`App Asset Library videos`](app-asset-library-videos.md).
- **Placements**: A placement ([`AppAssetLibraryPlacement`](appassetlibraryplacement.md)) positions one asset on one App Store surface: an App Store version localization, a custom product page localization, an in-app event localization, or an App Store version experiment treatment localization. For more information, see [`App Asset Library placements`](app-asset-library-placements.md).
- **Ordering requests**: A single request that sets the display order of placements within one localization and placement group, such as the order of screenshots. For more information, see [`App Asset Library placement ordering requests`](app-asset-library-placement-ordering-requests.md).
- **Reference data**: A machine-readable catalog of valid specifications: dimensions, aspect ratios, file formats, placement groups, and per-placement limits. Query it instead of hard-coding requirements. For more information, see [`App Asset Library reference data`](app-asset-library-reference-data.md).

#### Learn the Vocabulary of a Placement

Three values describe where an asset appears. You supply the first two when you create a placement, and App Store Connect provides the third:

- **Placement type ([`AppAssetLibraryPlacementType`](appassetlibraryplacementtype.md))**: Names the kind of slot: `APP_SCREENSHOT`, `APP_PREVIEW`, `PRODUCT_PAGE_HEADER_ASSET`, `EVENT_CARD_ASSET`, and so on.
- **Placement group**: Narrows that slot to a family of devices. Group identifiers are strings such as `IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE` or `MAC_PROFILE`, and the full list comes from the reference data. Each group maps to a platform ([`AppAssetLibraryPlacementPlatform`](appassetlibraryplacementplatform.md)) and a display class ([`AppAssetLibraryDisplayClass`](appassetlibrarydisplayclass.md)).
- **Specification**: Describes the file itself: exact pixel dimensions, aspect ratio, formats, and maximum size. You don’t choose a specification; App Store Connect matches your uploaded file to one during processing and reports it back as the asset’s `specId`.

Placement group identifiers and their limits come from the reference data rather than an enumeration, so you need to read them at runtime. For more information, see [`Discovering asset specifications`](discovering-asset-specifications.md).

#### Follow the End to End Workflow

A typical integration moves through these stages:

1. **Find the library.** Read the app’s asset library with `GET /v1/apps/{id}/assetLibrary` ([`Read related asset library`](get-v1-apps-_id_-assetlibrary.md)) and note its `id`. You relate every asset you upload to this library.
2. **Check the specifications.** Query the reference data with `GET /v1/appAssetLibraryRefData` ([`List app asset library ref data`](get-v1-appassetlibraryrefdata.md)) to learn the dimensions, formats, placement groups, and limits that apply to the surfaces you’re targeting.
3. **Upload your assets.** Reserve, upload, and commit each image or video, then wait for processing. For more information, see [`Uploading and managing image assets`](uploading-and-managing-image-assets.md) and [`Uploading and managing video assets`](uploading-and-managing-video-assets.md).
4. **Place the assets.** Create placements that link each asset to a target localization, then set their order within each placement group. For more information, see [`Placing assets on your App Store surfaces`](placing-assets-on-your-app-store-surfaces.md).
5. **Submit for review.** Placements travel through App Review as part of their parent surface. A placement’s state reflects the review state of that parent.

#### Track Asset State

Every image and video reports a `state` ([`AppAssetLibraryAssetState`](appassetlibraryassetstate.md)). Reserving, uploading, and processing an asset moves it through:

`AWAITING_UPLOAD` → `UPLOAD_COMPLETE` → `PREPARE_FOR_SUBMISSION`

After the asset reaches `PREPARE_FOR_SUBMISSION`, it’s processed and you can place it. Submitting the parent surface for review advances the asset through `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `ACCEPTED`, and `APPROVED`.

Three states sit outside that progression:

- **`FAILED`**: Processing didn’t succeed. Read `stateDetails` for the reason.
- **`REJECTED`**: App Review declined the asset.
- **`ARCHIVED`**: You retired an approved asset from active use.

Re-fetch an asset at any time to read its current `state` and `stateDetails`. Placements track their own `state` ([`AppAssetLibraryPlacementState`](appassetlibraryplacementstate.md)), which mirrors the review state of the parent surface, from `ASSET_PROCESSING` through `PARENT_APPROVED`.

#### Choose an Asset Category

When you create an asset, you assign it a category ([`AppAssetLibraryAssetCategory`](appassetlibraryassetcategory.md)):

- **`APP_SCREENSHOTS_AND_PREVIEWS`**: Screenshots and app previews for your product pages.
- **`CREATIVE_ASSETS`**: Other marketing media, such as in-app event artwork and product page header assets.

The category determines the placement types for which an asset is eligible. Each placement type in the reference data lists the categories it accepts in `acceptsAssetCategories`, and creating a placement with a category that doesn’t match that list returns an error.

#### Review Roles and Access

To manage the asset library with the App Store Connect API, you need one of the following user roles:

- `ACCOUNT_HOLDER`
- `ADMIN`
- `APP_MANAGER`

For the full list of App Store Connect user roles, see [`UserRole`](userrole.md) and [`Program Roles`](https://developer.apple.comhttps://developer.apple.com/support/roles). If you’re new to the API, see [`Creating API Keys for App Store Connect API`](creating-api-keys-for-app-store-connect-api.md), [`Generating Tokens for API Requests`](generating-tokens-for-api-requests.md), and [`Identifying Rate Limits`](identifying-rate-limits.md).

## Topics

### Uploading assets
- [Uploading and managing image assets](uploading-and-managing-image-assets.md)
  Reserve, upload, and commit an image to your app’s asset library, then update, archive, or delete it.
- [Uploading and managing video assets](uploading-and-managing-video-assets.md)
  Reserve, upload, and commit a video to your app’s asset library, set its preview frame, then update, archive, or delete it.
### Placing assets
- [Placing assets on your App Store surfaces](placing-assets-on-your-app-store-surfaces.md)
  Create placements that position library assets on App Store surfaces, then set their display order within a localization.
- [Discovering asset specifications](discovering-asset-specifications.md)
  Query the asset library reference data to learn the valid dimensions, formats, placement groups, and limits before you upload.
### Migrating existing media
- [Migrating to the App Asset Library](migrating-to-the-app-asset-library.md)
  Move your screenshots, app previews, and in-app event media from the deprecated set-based resources to the asset library.

## See Also

- [Uploading and managing image assets](uploading-and-managing-image-assets.md)
  Reserve, upload, and commit an image to your app’s asset library, then update, archive, or delete it.
- [Uploading and managing video assets](uploading-and-managing-video-assets.md)
  Reserve, upload, and commit a video to your app’s asset library, set its preview frame, then update, archive, or delete it.
- [Placing assets on your App Store surfaces](placing-assets-on-your-app-store-surfaces.md)
  Create placements that position library assets on App Store surfaces, then set their display order within a localization.
- [Discovering asset specifications](discovering-asset-specifications.md)
  Query the asset library reference data to learn the valid dimensions, formats, placement groups, and limits before you upload.
- [Migrating to the App Asset Library](migrating-to-the-app-asset-library.md)
  Move your screenshots, app previews, and in-app event media from the deprecated set-based resources to the asset library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/understanding-the-app-asset-library)*