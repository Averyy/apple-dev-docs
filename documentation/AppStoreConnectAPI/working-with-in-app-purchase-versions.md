# Working with In-App Purchase versions

**Framework**: App Store Connect API

Manage draft versions of an In-App Purchase’s localized metadata and review images before submitting for App Review.

#### Overview

An In-App Purchase version is a draft container that groups the localized metadata and review images that go through App Review together. Create a version, attach localizations and images to it, then submit the version through the review submissions workflow. The parent In-App Purchase resource holds properties that stay stable across versions — its product ID, In-App Purchase type, and pricing — while each version captures the reviewable metadata for a single review cycle.

> **Note**:  The pre-4.4.1 workflow that posts localizations and images directly to the In-App Purchase (`POST /v1/inAppPurchaseLocalizations`, `POST /v1/inAppPurchaseImages`) is deprecated as of 4.4.1 but remains available for existing integrations. For guidance on moving to the version-based workflow, see [`Migrating In-App Purchase metadata to v2`](migrating-in-app-purchase-metadata-to-v2.md).

##### Understand the Version Lifecycle

A version moves through these states, exposed on `InAppPurchaseVersion/Attributes/state`:

- `PREPARE_FOR_SUBMISSION`: The version is open for editing. You can add, change, or remove localizations and images.
- `READY_FOR_REVIEW`: The version belongs to a review submission and is waiting for you to mark that submission `submitted`.
- `WAITING_FOR_REVIEW`: You submitted the review submission, and the version is queued.
- `IN_REVIEW`: App Review is actively reviewing the version.
- `ACCEPTED` or `APPROVED`: The version passed review.
- `REJECTED` or `DEVELOPER_REJECTED`: App Review rejected the version, or you withdrew it.
- `REPLACED_WITH_NEW_VERSION`: A newer version supersedes this one.

Versions are read-only after creation. To change a version’s contents, create a new version.

##### Create a Version

Create a draft version with `POST /v1/inAppPurchaseVersions` ([`Create an In-App Purchase version`](post-v1-inapppurchaseversions.md)). Relate it to the In-App Purchase whose metadata you’re updating:

```json
{
  "data": {
    "type": "inAppPurchaseVersions",
    "relationships": {
      "inAppPurchase": {
        "data": {
          "type": "inAppPurchases",
          "id": "6446452615"
        }
      }
    }
  }
}
```

The response returns the new version’s `id` and a `state` of `PREPARE_FOR_SUBMISSION`. Note the `id` — every subsequent step references it.

##### Attach a Localization to the Version

Add a localized display name and description with `POST /v2/inAppPurchaseLocalizations` ([`Create an In-App Purchase localization`](post-v2-inapppurchaselocalizations.md)). The payload relates the localization to the version, not the parent In-App Purchase:

```json
{
  "data": {
    "type": "inAppPurchaseLocalizations",
    "attributes": {
      "locale": "en-US",
      "name": "Seattle Neighborhood Coffee Map",
      "description": "This is a neighborhood map for helping to find awesome coffee shops."
    },
    "relationships": {
      "version": {
        "data": {
          "type": "inAppPurchaseVersions",
          "id": "${inAppPurchaseVersionId}"
        }
      }
    }
  }
}
```

Repeat for each locale you support. To list the localizations attached to a version, use `GET /v1/inAppPurchaseVersions/{id}/localizations` ([`List localizations for an In-App Purchase version`](get-v1-inapppurchaseversions-_id_-localizations.md)).

##### Attach a Review Image to the Version

An In-App Purchase version can carry review images that show the promotion image customers see on the App Store product page. Reserve, upload, and commit each image in three steps.

Reserve an image with `POST /v2/inAppPurchaseImages` ([`Create an In-App Purchase image`](post-v2-inapppurchaseimages.md)):

```json
{
  "data": {
    "type": "inAppPurchaseImages",
    "attributes": {
      "fileName": "coffee-map-promo.png",
      "fileSize": 245670
    },
    "relationships": {
      "version": {
        "data": {
          "type": "inAppPurchaseVersions",
          "id": "${inAppPurchaseVersionId}"
        }
      }
    }
  }
}
```

The response returns an `id` for the image and a set of `uploadOperations` describing how to `PUT` the file bytes.

Upload the image bytes to the URL from `uploadOperations`. Then commit the upload with `PATCH /v2/inAppPurchaseImages/{id}` ([`Modify an In-App Purchase image`](patch-v2-inapppurchaseimages-_id_.md)):

```json
{
  "data": {
    "type": "inAppPurchaseImages",
    "id": "${inAppPurchaseImageId}",
    "attributes": {
      "uploaded": true
    }
  }
}
```

Read image metadata with `GET /v2/inAppPurchaseImages/{id}` ([`Read In-App Purchase image information`](get-v2-inapppurchaseimages-_id_.md)). Remove an image with `DELETE /v2/inAppPurchaseImages/{id}` ([`Delete an In-App Purchase image`](delete-v2-inapppurchaseimages-_id_.md)).

For more on the reserve-upload-commit pattern, see [`Uploading Assets to App Store Connect`](uploading-assets-to-app-store-connect.md).

##### List All Versions for an in App Purchase

To see every version on a parent In-App Purchase, use `GET /v2/inAppPurchases/{id}/versions` ([`List the versions of an In-App Purchase`](get-v2-inapppurchases-_id_-versions.md)). The response includes each version’s state, so you can find the current draft, the most recently approved version, and any versions currently in review.

##### Submit the Version

Submit a completed version through the review submissions workflow. Create a review submission for the app, add the version as an item, and mark the submission as `submitted`. For step-by-step instructions, see [`Managing In-App Purchases`](managing-in-app-purchases.md).

When you mark the submission `submitted`, the version moves from `READY_FOR_REVIEW` to `WAITING_FOR_REVIEW`. Poll `GET /v1/inAppPurchaseVersions/{id}` ([`Read In-App Purchase version information`](get-v1-inapppurchaseversions-_id_.md)) to watch it continue to `IN_REVIEW` and then `APPROVED` or `REJECTED`.

## See Also

- [Managing In-App Purchases](managing-in-app-purchases.md)
  Create In-App Purchases, configure their metadata and pricing, submit them for review, and promote them with the App Store Connect API.
- [Migrating In-App Purchase metadata to v2](migrating-in-app-purchase-metadata-to-v2.md)
  Update an existing integration from the pre-4.4.1 metadata workflow to the version-based v2 workflow.
- [In-App Purchase Versions](in-app-purchase-versions.md)
  Create and read draft versions of an In-App Purchase, with their localized metadata and review images.
- [In-App Purchases](in-app-purchases.md)
  Create, modify, and delete In-App Purchases for your app.
- [In-App Purchase Localizations](in-app-purchase-localizations.md)
  Create, modify, and delete localized metadata for In-App Purchase versions.
- [In-App Purchase localizations (v1)](in-app-purchase-localizations-v1.md)
  Create, modify, and delete localized metadata for In-App Purchases.
- [In-App Purchase price schedules](in-app-purchase-price-schedules.md)
  Create a scheduled price change for an In-App Purchase, and get information about scheduled price changes.
- [In-App Purchase availability](in-app-purchase-availability.md)
  Read and modify territory availability for an In-App Purchase.
- [In-App Purchase images](in-app-purchase-images.md)
  Create, modify, and delete promotion images for In-App Purchases.
- [In-App Purchase images (v1)](in-app-purchase-images-v1.md)
  Create, modify, and delete promotion images for your In-App Purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/working-with-in-app-purchase-versions)*