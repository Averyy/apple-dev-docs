# Placing assets on your App Store surfaces

**Framework**: App Store Connect API

Create placements that position library assets on App Store surfaces, then set their display order within a localization.

#### Overview

After an image or video finishes processing in your asset library, you make it appear on the App Store by creating a *placement*, which links one asset to one surface: an App Store version localization, a custom product page localization, an in-app event localization, or an App Store version experiment treatment localization. Because the placement references the asset rather than copying it, the same asset can back many placements at once.

This article covers creating, replacing, and removing placements, and setting their display order. For more information about assets, see [`Uploading and managing image assets`](uploading-and-managing-image-assets.md) and [`Uploading and managing video assets`](uploading-and-managing-video-assets.md). For more information about the asset library, see [`Understanding the App Asset Library`](understanding-the-app-asset-library.md).

#### Create a Placement

Create a placement with `POST /v1/appAssetLibraryPlacements` ([`Create an app asset library placement`](post-v1-appassetlibraryplacements.md)). A placement request combines four things:

- **`placementType` ([`AppAssetLibraryPlacementType`](appassetlibraryplacementtype.md))**: The type of the placement, for example, `APP_SCREENSHOT`, `APP_PREVIEW`, `PRODUCT_PAGE_HEADER_ASSET`, or `EVENT_CARD_ASSET`.
- **`placementGroup`**: The device family the placement targets, such as `IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE` or `MAC_PROFILE`. Read the valid identifiers from the reference data; they aren’t an enumeration. For more information, see [`Discovering asset specifications`](discovering-asset-specifications.md).
- **Exactly one asset relationship**: `image` for an [`AppAssetLibraryImage`](appassetlibraryimage.md) or `video` for an [`AppAssetLibraryVideo`](appassetlibraryvideo.md).
- **Exactly one target-surface relationship**: `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appEventLocalization`, or `appStoreVersionExperimentTreatmentLocalization`.

This example places an image as an iPhone screenshot on an App Store version localization:

```json
{
  "data": {
    "type": "appAssetLibraryPlacements",
    "attributes": {
      "placementType": "APP_SCREENSHOT",
      "placementGroup": "IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE"
    },
    "relationships": {
      "image": {
        "data": {
          "type": "appAssetLibraryImages",
          "id": "f4000005-e036-8f0b-8018-d259974bee61"
        }
      },
      "appStoreVersionLocalization": {
        "data": {
          "type": "appStoreVersionLocalizations",
          "id": "b3a9b4c2-d2de-43f4-ad8c-71c5ebe301d1"
        }
      }
    }
  }
}
```

To place a video instead, for example, an app preview, use the `video` relationship and the matching `placementType`:

```json
{
  "data": {
    "type": "appAssetLibraryPlacements",
    "attributes": {
      "placementType": "APP_PREVIEW",
      "placementGroup": "IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE"
    },
    "relationships": {
      "video": {
        "data": {
          "type": "appAssetLibraryVideos",
          "id": "c2d3e4f5-6789-01ab-cdef-234567890abc"
        }
      },
      "appStoreVersionLocalization": {
        "data": {
          "type": "appStoreVersionLocalizations",
          "id": "b3a9b4c2-d2de-43f4-ad8c-71c5ebe301d1"
        }
      }
    }
  }
}
```

The response returns the placement `id`, its `mediaType` (`IMAGE` or `VIDEO`, derived from which asset relationship you sent), and a `state` ([`AppAssetLibraryPlacementState`](appassetlibraryplacementstate.md)):

```json
{
  "data": {
    "type": "appAssetLibraryPlacements",
    "id": "2e000005-e036-8f0b-8f25-6dbc2baa784a",
    "attributes": {
      "mediaType": "IMAGE",
      "placementType": "APP_SCREENSHOT",
      "placementGroup": "IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE",
      "createdDate": "2026-08-11T22:45:27.092513Z",
      "lastModifiedDate": "2026-08-11T22:45:27.092513Z",
      "state": "PARENT_PREPARE_FOR_SUBMISSION",
      "stateDetails": null
    }
  }
}
```

A placement’s state mirrors the review state of its parent surface, from `ASSET_PROCESSING` through `PARENT_APPROVED`. If the linked asset hasn’t finished processing, the placement starts in `ASSET_PROCESSING`.

#### Reuse One Asset Across Surfaces

An asset can back several placements at once; that’s the point of the library. The same image can serve as both a standard screenshot and an iMessage screenshot, for instance, by creating a second placement with a different type and group:

```json
{
  "data": {
    "type": "appAssetLibraryPlacements",
    "attributes": {
      "placementType": "IMESSAGE_APP_SCREENSHOT",
      "placementGroup": "IMESSAGE_IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE"
    },
    "relationships": {
      "image": {
        "data": {
          "type": "appAssetLibraryImages",
          "id": "f4000005-e036-8f0b-8018-d259974bee61"
        }
      },
      "appStoreVersionLocalization": {
        "data": {
          "type": "appStoreVersionLocalizations",
          "id": "b3a9b4c2-d2de-43f4-ad8c-71c5ebe301d1"
        }
      }
    }
  }
}
```

Reading `GET /v1/appAssetLibraryImages/{id}/placements` ([`List related placements`](get-v1-appassetlibraryimages-_id_-placements.md)) then returns both placements. Replacing the artwork means uploading a new asset and updating the placements, because the placements point at one asset. The reverse is also true, and it’s why the library scales: App Store Connect stores and processes a screenshot once, even when you reuse it across ten localizations.

#### Handle Placement Errors

Three constraints account for most failures when creating a placement:

**The type, group, and asset category have to agree.** Each placement type in the reference data lists the categories it accepts. Pairing a `CREATIVE_ASSETS` placement type with an `APP_SCREENSHOTS_AND_PREVIEWS` asset, or naming a group that doesn’t belong to that type, returns:

```json
{
  "errors": [
    {
      "status": "409",
      "code": "ENTITY_ERROR.ATTRIBUTE.INVALID",
      "title": "The provided entity includes an attribute with an invalid value",
      "detail": "The requested 'placementType' and 'placementGroup' combination is not supported for this parent.",
      "source": { "pointer": "/data/attributes/placementType" }
    }
  ]
}
```

**The parent surface has to be editable.** You can’t add a placement to a custom product page version or App Store version that’s already approved:

```json
{
  "errors": [
    {
      "status": "409",
      "code": "STATE_ERROR.INVALID_STATE",
      "title": "Creating a placement is not permitted in AppCustomProductPageVersion's current state",
      "meta": { "state": "approved", "feature": "ASC_FEATURE_CUSTOM_PRODUCT_PAGES" }
    }
  ]
}
```

**Each group has a maximum count.** The reference data states per-group limits in `features[].placementPolicies[].groupLimits[].maxCount`; for App Store versions that’s 10 screenshots, 3 app previews, and 1 product page header asset per group. Read the limit before you create placements in a loop.

#### Read Placements

Read a single placement with `GET /v1/appAssetLibraryPlacements/{id}` ([`Read an app asset library placement`](get-v1-appassetlibraryplacements-_id_.md)). To list every placement on a surface, use that surface’s `placements` relationship, for example, `GET /v1/appStoreVersionLocalizations/{id}/placements` ([`List related placements`](get-v1-appstoreversionlocalizations-_id_-placements.md)).

Combine `include` with `fields` to fetch placements and their assets in one call:

```None
GET /v1/appStoreVersionLocalizations/b3a9b4c2-d2de-43f4-ad8c-71c5ebe301d1/placements
  ?filter[placementType]=APP_SCREENSHOT
  &filter[placementGroup]=IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE
  &sort=placementGroupPosition
  &include=image
  &fields[appAssetLibraryImages]=referenceName,state,imageAsset
```

Sorting by `placementGroupPosition` returns the placements in the order they display. There’s no `placementGroupPosition` attribute to read; it exists only as a sort key, so the sequence of the response is what tells you the order.

#### Replace a Placements Asset

You can’t change a placement after you create it. The asset it displays, its placement type, its placement group, and its target surface are all fixed at creation. To show a different asset in the same spot, delete the placement, create a new one that relates to the new asset, and then reorder the group so the new placement takes the old one’s position.

#### Delete a Placement

Remove a placement with `DELETE /v1/appAssetLibraryPlacements/{id}` ([`Delete an app asset library placement`](delete-v1-appassetlibraryplacements-_id_.md)), which returns `204 No Content`. This removes the asset from that surface but leaves the underlying asset in your library, along with any other placements that reuse it.

> ❗ **Important**:  To remove an asset, delete its placements first, then the asset. Deletion runs in one direction only. Deleting a placement leaves its asset intact, but deleting an asset that still has placements fails.

#### Order Placements Within a Group

Screenshots and app previews display in a specific order. Set that order in a single request with `POST /v1/appAssetLibraryPlacementOrderingRequests` ([`Create an app asset library placement ordering request`](post-v1-appassetlibraryplacementorderingrequests.md)). Provide the `placementGroup` you’re ordering, list the placement IDs in `orderedPlacements` in the sequence you want, and relate the request to the target localization:

```json
{
  "data": {
    "type": "appAssetLibraryPlacementOrderingRequests",
    "attributes": {
      "placementGroup": "IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE"
    },
    "relationships": {
      "orderedPlacements": {
        "data": [
          { "type": "appAssetLibraryPlacements", "id": "1e800005-e036-8f0b-8f37-9c5cc67e23a1" },
          { "type": "appAssetLibraryPlacements", "id": "2e000005-e036-8f0b-8f25-6dbc2baa784a" }
        ]
      },
      "appStoreVersionLocalization": {
        "data": {
          "type": "appStoreVersionLocalizations",
          "id": "b3a9b4c2-d2de-43f4-ad8c-71c5ebe301d1"
        }
      }
    }
  }
}
```

The order of the IDs in `orderedPlacements` becomes the display order. Ordering is scoped to one placement group within one localization, so reorder each group separately.

An ordering request targets an `appStoreVersionLocalization`, an `appCustomProductPageLocalization`, or an `appStoreVersionExperimentTreatmentLocalization`. In-app event localizations aren’t orderable, which follows from their limits; each in-app event placement type allows a single asset per group.

The response returns the ordering request `id`. Add `?include=orderedPlacements` to echo the placements back in their new sequence, or re-read the localization’s placements with `sort=placementGroupPosition` to confirm.

#### Submit for Review

Placements go through App Review as part of their parent surface: the App Store version, custom product page, or in-app event. Submit that parent as you normally would, and the placement’s `state` follows the parent’s review state through to `PARENT_APPROVED`.

## See Also

- [Understanding the App Asset Library](understanding-the-app-asset-library.md)
  Upload an image or video once, then reuse it across your app’s App Store surfaces with per-surface placements.
- [Uploading and managing image assets](uploading-and-managing-image-assets.md)
  Reserve, upload, and commit an image to your app’s asset library, then update, archive, or delete it.
- [Uploading and managing video assets](uploading-and-managing-video-assets.md)
  Reserve, upload, and commit a video to your app’s asset library, set its preview frame, then update, archive, or delete it.
- [Discovering asset specifications](discovering-asset-specifications.md)
  Query the asset library reference data to learn the valid dimensions, formats, placement groups, and limits before you upload.
- [Migrating to the App Asset Library](migrating-to-the-app-asset-library.md)
  Move your screenshots, app previews, and in-app event media from the deprecated set-based resources to the asset library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/placing-assets-on-your-app-store-surfaces)*