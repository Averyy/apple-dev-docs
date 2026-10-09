# Discovering asset specifications

**Framework**: App Store Connect API

Query the asset library reference data to learn the valid dimensions, formats, placement groups, and limits before you upload.

#### Overview

The App Asset Library validates every asset against a catalog of specifications, and it exposes that catalog through the `appAssetLibraryRefData` resource. Reading it at runtime is the difference between an integration that keeps working and one that falls behind when Apple adds a device. An integration that hard-codes specifications or placement group identifiers can’t target a new device family, and may reject files that a new specification accepts, until you ship an update. The catalog is large. It holds dozens of image specifications, more than a dozen video specifications, and dozens of placement groups, and it changes as the App Store changes.

Reference data is read-only, and its identifiers are strings rather than enumerations precisely so new device families can appear without an API change. Don’t hard-code them.

For the resource reference, see [`App Asset Library reference data`](app-asset-library-reference-data.md). For the concept, see [`Understanding the App Asset Library`](understanding-the-app-asset-library.md).

#### Read the Reference Data

Fetch the catalog with `GET /v1/appAssetLibraryRefData` ([`List app asset library ref data`](get-v1-appassetlibraryrefdata.md)). The collection holds a single [`AppAssetLibraryRefDatum`](appassetlibraryrefdatum.md) with attributes that are six parallel arrays:

- **`features`**: What each App Store feature supports, including the placement types available and the maximum number of assets per placement group.
- **`placementProfileGroups`**: Every placement group identifier, with the platform ([`AppAssetLibraryPlacementPlatform`](appassetlibraryplacementplatform.md)) and display class ([`AppAssetLibraryDisplayClass`](appassetlibrarydisplayclass.md)) to which it maps.
- **`imageSpecs`**: Image requirements, including dimensions, aspect ratio, permitted extensions and MIME types, maximum file size, and whether alpha is allowed.
- **`videoSpecs`**: Video requirements, including the same values as images, plus frame-rate ranges, duration bounds, and whether audio is required.
- **`placementTypes`**: For each placement type, the asset categories it accepts and a mapping from placement group to permitted specification IDs.
- **`displayClasses`**: Each display class with its device family and screen dimensions.

Narrow the response with `filter[features]`, `filter[placementTypes]`, `filter[placementProfileGroups]`, or `filter[specs]`, or use `fields[appAssetLibraryRefData]` to request only the arrays you need. Reading one array instead of all six keeps a routine specification check small:

```None
GET /v1/appAssetLibraryRefData?fields[appAssetLibraryRefData]=imageSpecs
```

#### Follow the Lookup Chain

The six arrays are designed for traversal in order. To find the file you need for an iPhone screenshot on an App Store version, walk them like this:

1. **Start with the feature.** Find `APP_STORE_VERSIONS` in `features`. Its `placementPolicies` list the placement types that feature supports, and for each one, `groupLimits` gives the `maxCount` allowed per set of `groupIds`.
2. **Pick a placement group.** Look up your target group in `placementProfileGroups` to confirm its platform and display class, for example, `IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE` or `MAC_PROFILE`.
3. **Map the group to specifications.** Find your placement type in `placementTypes`, then find your group in its `specMappings`. The `specs` array lists the specification IDs that group accepts.
4. **Read the specification.** Look each ID up in `imageSpecs` or `videoSpecs` to get the actual requirements.

An image specification looks like this:

```json
{
  "specId": "f56c777c-99ea-5760-97ae-27c5f8cbb884",
  "shortName": "i1290x2796a0",
  "dimensions": {
    "minWidth": 1290, "maxWidth": 1290,
    "minHeight": 2796, "maxHeight": 2796
  },
  "aspectRatio": "6:13",
  "compatiblePlacementTypes": ["APP_SCREENSHOT", "IMESSAGE_APP_SCREENSHOT"],
  "alphaAllowed": false,
  "fileExtensions": [".jpg", ".jpeg", ".png"],
  "mimeTypes": ["image/jpeg", "image/png"],
  "maxFileSize": 524288000,
  "universalAsset": false
}
```

For screenshots and previews, `minWidth` equals `maxWidth` and `minHeight` equals `maxHeight`, so the dimensions are exact, not a range. Resize to match before you upload.

When you’re working backward from a file you already have, use `compatiblePlacementTypes` to skip the chain: Given a specification, it lists every placement type that accepts it.

#### Understand Universal Assets

A specification with `universalAsset` set to `true` satisfies several placement types at once. Check `compatiblePlacementTypes` on the specification to see which ones. Uploading one file at a universal specification and creating a placement per type is less work than producing a file for each.

#### Respect the Placement Limits

`groupLimits` caps how many assets a placement group holds. For `APP_STORE_VERSIONS`, the App Store allows 10 screenshots, 3 app previews, and 1 product page header asset per group. In-app events allow a single asset for each of their placement types.

Read the limit rather than assuming it. Creating placements past the cap fails, and the limits differ by feature: custom product pages and product page optimizations carry their own policies, and they don’t always match the App Store version policies.

#### Match the Asset Category

Each entry in `placementTypes` lists an `acceptsAssetCategories` array. `APP_SCREENSHOT` and `IMESSAGE_APP_SCREENSHOT` accept `APP_SCREENSHOTS_AND_PREVIEWS`; the creative placement types such as `EVENT_CARD_ASSET` and `PRODUCT_PAGE_HEADER_ASSET` accept `CREATIVE_ASSETS`. Because you set an asset’s `category` when you reserve it and can’t change it afterward, check this before uploading. You can’t place an asset where you intend if it has the wrong category.

> **Note**:  [`AppAssetLibraryFeature`](appassetlibraryfeature.md) enumerates more features than the reference data currently returns. Iterate over the `features` array you receive rather than over the enumeration, and treat a feature that’s absent as unavailable for your app.

#### Cache with Care

The catalog is stable within a session but not permanent; Apple adds specifications and groups as new devices ship. Fetch it when your integration starts rather than embedding a copy, and key your logic on the identifiers you read back. Two habits make the difference:

- Resolve a `specId` returned on an asset by looking it up in the catalog, instead of comparing against a hard-coded list.
- Treat an unrecognized placement group or specification ID as a signal to refresh, not as an error.

To read a specific reference data resource by ID, use `GET /v1/appAssetLibraryRefData/{id}` ([`Read an app asset library ref data`](get-v1-appassetlibraryrefdata-_id_.md)).

After you know the specification you need, upload the asset. For more information, see [`Uploading and managing image assets`](uploading-and-managing-image-assets.md) and [`Uploading and managing video assets`](uploading-and-managing-video-assets.md).

## See Also

- [Understanding the App Asset Library](understanding-the-app-asset-library.md)
  Upload an image or video once, then reuse it across your app’s App Store surfaces with per-surface placements.
- [Uploading and managing image assets](uploading-and-managing-image-assets.md)
  Reserve, upload, and commit an image to your app’s asset library, then update, archive, or delete it.
- [Uploading and managing video assets](uploading-and-managing-video-assets.md)
  Reserve, upload, and commit a video to your app’s asset library, set its preview frame, then update, archive, or delete it.
- [Placing assets on your App Store surfaces](placing-assets-on-your-app-store-surfaces.md)
  Create placements that position library assets on App Store surfaces, then set their display order within a localization.
- [Migrating to the App Asset Library](migrating-to-the-app-asset-library.md)
  Move your screenshots, app previews, and in-app event media from the deprecated set-based resources to the asset library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/discovering-asset-specifications)*