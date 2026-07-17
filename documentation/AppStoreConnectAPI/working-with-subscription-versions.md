# Working with subscription versions

**Framework**: App Store Connect API

Manage draft versions of an auto-renewable subscription’s localized metadata and review images before submitting for App Review.

#### Overview

A subscription version is a draft container that groups the localized metadata and review images that go through App Review together. Create a version, attach localizations and images to it, then submit the version through the review submissions workflow. The parent subscription resource holds properties that stay stable across versions — its product ID, subscription duration, group, and pricing — while each version captures the reviewable metadata for a single review cycle.

> **Note**:  The pre-4.4.1 workflow that posts localizations and images directly to the subscription (`POST /v1/subscriptionLocalizations`, `POST /v1/subscriptionImages`) is deprecated as of 4.4.1 but remains available for existing integrations. For guidance on moving to the version-based workflow, see [`Migrating in-app purchase metadata to v2`](migrating-in-app-purchase-metadata-to-v2.md).

##### Understand the Version Lifecycle

A version moves through these states, exposed on `SubscriptionVersion/Attributes/state`:

- `PREPARE_FOR_SUBMISSION`: the version is being edited. Localizations and images can be added, changed, or removed.
- `READY_FOR_REVIEW`: the version is attached to a review submission and awaiting the submission to be marked `submitted`.
- `WAITING_FOR_REVIEW`: the review submission has been submitted and the version is queued.
- `IN_REVIEW`: App Review is actively reviewing the version.
- `ACCEPTED` or `APPROVED`: the version passed review.
- `REJECTED` or `DEVELOPER_REJECTED`: the version was rejected by App Review or withdrawn by the developer.
- `REPLACED_WITH_NEW_VERSION`: a newer version supersedes this one.

Versions are read-only after creation. To change a version’s contents, create a new version.

##### Create a Version

Create a draft version with `POST /v1/subscriptionVersions` ([`Create a subscription version`](post-v1-subscriptionversions.md)). Relate it to the subscription whose metadata you’re updating:

```json
{
  "data": {
    "type": "subscriptionVersions",
    "relationships": {
      "subscription": {
        "data": {
          "type": "subscriptions",
          "id": "6446671421"
        }
      }
    }
  }
}
```

The response returns the new version’s `id` and a `state` of `PREPARE_FOR_SUBMISSION`. Note the `id` — every subsequent step references it.

##### Attach a Localization to the Version

Add a localized display name and description with `POST /v2/subscriptionLocalizations` ([`Create a subscription localization`](post-v2-subscriptionlocalizations.md)). The payload relates the localization to the version, not the parent subscription:

```json
{
  "data": {
    "type": "subscriptionLocalizations",
    "attributes": {
      "locale": "en-US",
      "name": "All Access — Monthly",
      "description": "Unlimited lessons across every instrument."
    },
    "relationships": {
      "version": {
        "data": {
          "type": "subscriptionVersions",
          "id": "${subscriptionVersionId}"
        }
      }
    }
  }
}
```

Repeat for each locale you support. To list the localizations attached to a version, use `GET /v1/subscriptionVersions/{id}/localizations` ([`List localizations for a subscription version`](get-v1-subscriptionversions-_id_-localizations.md)).

##### Attach a Review Image to the Version

A subscription version can carry review images that show the promotion image customers see on the App Store product page. Reserve, upload, and commit each image in three steps.

Reserve an image with `POST /v2/subscriptionImages` ([`Create a subscription image`](post-v2-subscriptionimages.md)):

```json
{
  "data": {
    "type": "subscriptionImages",
    "attributes": {
      "fileName": "all-access-promo.png",
      "fileSize": 245670
    },
    "relationships": {
      "version": {
        "data": {
          "type": "subscriptionVersions",
          "id": "${subscriptionVersionId}"
        }
      }
    }
  }
}
```

The response returns an `id` for the image and a set of `uploadOperations` describing how to `PUT` the file bytes.

Upload the image bytes to the URL from `uploadOperations`. Then commit the upload with `PATCH /v2/subscriptionImages/{id}` ([`Modify a subscription image`](patch-v2-subscriptionimages-_id_.md)):

```json
{
  "data": {
    "type": "subscriptionImages",
    "id": "${subscriptionImageId}",
    "attributes": {
      "uploaded": true
    }
  }
}
```

Read image metadata with `GET /v2/subscriptionImages/{id}` ([`Read subscription image information`](get-v2-subscriptionimages-_id_.md)). Remove an image with `DELETE /v2/subscriptionImages/{id}` ([`Delete a subscription image`](delete-v2-subscriptionimages-_id_.md)).

For more on the reserve-upload-commit pattern, see [`Uploading Assets to App Store Connect`](uploading-assets-to-app-store-connect.md).

##### List All Versions for a Subscription

To see every version on a parent subscription, use `GET /v1/subscriptions/{id}/versions` ([`List versions for a subscription`](get-v1-subscriptions-_id_-versions.md)). The response includes each version’s state, so you can find the current draft, the most recently approved version, and any versions currently in review.

##### Submit the Version

Submit a completed version through the review submissions workflow. Create a review submission for the app, add the version as an item, and mark the submission as `submitted`. For step-by-step instructions, see [`Submitting subscriptions and subscription groups for App Review`](submitting-subscriptions-and-subscription-groups-for-app-review.md).

When you mark the submission `submitted`, the version moves from `READY_FOR_REVIEW` to `WAITING_FOR_REVIEW`. Poll `GET /v1/subscriptionVersions/{id}` ([`Read subscription version information`](get-v1-subscriptionversions-_id_.md)) to watch it continue to `IN_REVIEW` and then `APPROVED` or `REJECTED`.

## See Also

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
- [Configuring subscription prices across territories](configuring-subscription-prices-across-territories.md)
  Set plan types and equalized prices for an auto-renewable subscription with the App Store Connect API.
- [Querying adjusted subscription price equalizations](querying-adjusted-subscription-price-equalizations.md)
  Compare a subscription price point against the equalized price points that Apple recommends across territories, adjusted for local pricing rules.
- [Subscription Versions](subscription-versions.md)
  Create and read draft versions of an auto-renewable subscription, with their localized metadata and review images.
- [Subscriptions](subscriptions.md)
  Create, modify, and delete auto-renewable subscriptions for your app.
- [Subscription Localizations](subscription-localizations.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription localizations (v1)](subscription-localizations-v1.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription price points and subscription prices](subscription-price-points-and-subscription-prices.md)
  Manage scheduled price changes for auto-renewable subscriptions and get price point information.
- [Subscription images](subscription-images.md)
  Create, modify, and delete promotion images for auto-renewable subscriptions.
- [Subscription images (v1)](subscription-images-v1.md)
  Create, modify, and delete promotion images for your auto-renewable subscription.
- [Subscription availability](subscription-availability.md)
  Read and modify territory availability for an auto-renewable subscription.
- [Subscription plan availability](subscription-plan-availability.md)
  Create and manage subscription plan availability for auto-renewable subscriptions.
- [Billing Grace Periods](billing-grace-periods.md)
  Get information about the grace period and modify the opt-in value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/working-with-subscription-versions)*