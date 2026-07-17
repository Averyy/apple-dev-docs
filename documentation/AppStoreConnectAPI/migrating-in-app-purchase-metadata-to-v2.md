# Migrating in-app purchase metadata to v2

**Framework**: App Store Connect API

Update an existing integration from the pre-4.4.1 metadata workflow to the version-based v2 workflow.

#### Overview

Before 4.4.1, localizations and review images attached directly to an in-app purchase, subscription, or subscription group. In 4.4.1, they attach to a *version* — a draft container that groups the metadata and images that go through App Review together. The pre-4.4.1 endpoints remain available for existing integrations, but new work uses the version-based path.

The version model separates a product’s stable properties (product ID, type, pricing) from its reviewable metadata (localized names, descriptions, review images). Each review cycle produces one version. When you need to change any localization or image, you create a new version rather than editing the live product.

##### Endpoint Mapping

Each deprecated v1 endpoint has a v2 equivalent that targets a version. The v1 endpoint keeps working; use it only for existing integrations that haven’t moved yet.

In-app purchase metadata and submission:

| Deprecated (v1) | Replacement (v2) |
| --- | --- |
| `POST /v1/inAppPurchaseLocalizations` | `POST /v2/inAppPurchaseLocalizations` (relates to an `inAppPurchaseVersion`) |
| `GET /v1/inAppPurchaseLocalizations/{id}` | `GET /v2/inAppPurchaseLocalizations/{id}` |
| `PATCH /v1/inAppPurchaseLocalizations/{id}` | `PATCH /v2/inAppPurchaseLocalizations/{id}` |
| `DELETE /v1/inAppPurchaseLocalizations/{id}` | `DELETE /v2/inAppPurchaseLocalizations/{id}` |
| `POST /v1/inAppPurchaseImages` | `POST /v2/inAppPurchaseImages` (relates to an `inAppPurchaseVersion`) |
| `GET /v1/inAppPurchaseImages/{id}` | `GET /v2/inAppPurchaseImages/{id}` |
| `PATCH /v1/inAppPurchaseImages/{id}` | `PATCH /v2/inAppPurchaseImages/{id}` |
| `DELETE /v1/inAppPurchaseImages/{id}` | `DELETE /v2/inAppPurchaseImages/{id}` |
| `POST /v1/inAppPurchaseSubmissions` | `POST /v1/reviewSubmissions` + `POST /v1/reviewSubmissionItems` with an `inAppPurchaseVersion` |

Subscription metadata and submission:

| Deprecated (v1) | Replacement (v2) |
| --- | --- |
| `POST /v1/subscriptionLocalizations` | `POST /v2/subscriptionLocalizations` (relates to a `subscriptionVersion`) |
| `POST /v1/subscriptionImages` | `POST /v2/subscriptionImages` (relates to a `subscriptionVersion`) |
| `POST /v1/subscriptionSubmissions` | `POST /v1/reviewSubmissions` + `POST /v1/reviewSubmissionItems` with a `subscriptionVersion` |

Subscription group metadata and submission:

| Deprecated (v1) | Replacement (v2) |
| --- | --- |
| `POST /v1/subscriptionGroupLocalizations` | `POST /v2/subscriptionGroupLocalizations` (relates to a `subscriptionGroupVersion`) |
| `POST /v1/subscriptionGroupSubmissions` | `POST /v1/reviewSubmissions` + `POST /v1/reviewSubmissionItems` with a `subscriptionGroupVersion` |

Nested read endpoints on the parent product are also deprecated in the same window:

- `GET /v2/inAppPurchases/{id}/inAppPurchaseLocalizations` and its `.../relationships/...` variant
- `GET /v2/inAppPurchases/{id}/images` and its `.../relationships/...` variant
- `GET /v1/subscriptions/{id}/subscriptionLocalizations`, `.../images`, and their relationship variants
- `GET /v1/subscriptionGroups/{id}/subscriptionGroupLocalizations` and its relationship variant

Read localizations and images through the version instead:

- `GET /v1/inAppPurchaseVersions/{id}/localizations` and `.../images`
- `GET /v1/subscriptionVersions/{id}/localizations` and `.../images`
- `GET /v1/subscriptionGroupVersions/{id}/localizations`

##### Migrate an in App Purchase Integration

The pre-4.4.1 flow posts a localization directly against the in-app purchase:

```other
POST /v1/inAppPurchaseLocalizations
{
  "data": {
    "type": "inAppPurchaseLocalizations",
    "attributes": {
      "locale": "en-US",
      "name": "Seattle Neighborhood Coffee Map",
      "description": "Find awesome coffee shops."
    },
    "relationships": {
      "inAppPurchaseV2": {
        "data": { "type": "inAppPurchases", "id": "6446452615" }
      }
    }
  }
}
```

In the version-based flow, create the version first, then post the localization against it:

```other
POST /v1/inAppPurchaseVersions
{
  "data": {
    "type": "inAppPurchaseVersions",
    "relationships": {
      "inAppPurchase": {
        "data": { "type": "inAppPurchases", "id": "6446452615" }
      }
    }
  }
}
```

```other
POST /v2/inAppPurchaseLocalizations
{
  "data": {
    "type": "inAppPurchaseLocalizations",
    "attributes": {
      "locale": "en-US",
      "name": "Seattle Neighborhood Coffee Map",
      "description": "Find awesome coffee shops."
    },
    "relationships": {
      "version": {
        "data": { "type": "inAppPurchaseVersions", "id": "${inAppPurchaseVersionId}" }
      }
    }
  }
}
```

The relationship key changes from `inAppPurchaseV2` (targeting the parent product) to `version` (targeting the draft version). The same shape applies to `POST /v2/inAppPurchaseImages`.

##### Migrate a Submission

The pre-4.4.1 flow submits an in-app purchase directly:

```other
POST /v1/inAppPurchaseSubmissions
{
  "data": {
    "type": "inAppPurchaseSubmissions",
    "relationships": {
      "inAppPurchaseV2": {
        "data": { "type": "inAppPurchases", "id": "6446452615" }
      }
    }
  }
}
```

In the version-based flow, submission is a three-step review-submissions process. Create a review submission for the app, add the version as an item, and mark the submission as `submitted`:

```other
POST /v1/reviewSubmissions
{
  "data": {
    "type": "reviewSubmissions",
    "attributes": { "platform": "IOS" },
    "relationships": {
      "app": { "data": { "type": "apps", "id": "6446148572" } }
    }
  }
}
```

```other
POST /v1/reviewSubmissionItems
{
  "data": {
    "type": "reviewSubmissionItems",
    "relationships": {
      "reviewSubmission": {
        "data": { "type": "reviewSubmissions", "id": "${reviewSubmissionId}" }
      },
      "inAppPurchaseVersion": {
        "data": { "type": "inAppPurchaseVersions", "id": "${inAppPurchaseVersionId}" }
      }
    }
  }
}
```

```other
PATCH /v1/reviewSubmissions/{id}
{
  "data": {
    "type": "reviewSubmissions",
    "id": "${reviewSubmissionId}",
    "attributes": { "submitted": true }
  }
}
```

The subscription and subscription group submission paths follow the same three-step pattern, with `subscriptionVersion` or `subscriptionGroupVersion` as the review submission item.

##### Update Your Polling Code

Before 4.4.1, integrations tracked submission status by reading the parent product’s state. Now, track the version’s `state` field on `InAppPurchaseVersion`, `SubscriptionVersion`, or `SubscriptionGroupVersion`. The transitions are `PREPARE_FOR_SUBMISSION` → `READY_FOR_REVIEW` → `WAITING_FOR_REVIEW` → `IN_REVIEW` → `APPROVED` or `REJECTED`. Poll the version with `GET /v1/inAppPurchaseVersions/{id}` (or the equivalent for subscriptions and groups).

##### What Doesnt Change

These pieces of the workflow are unchanged in 4.4.1:

- The in-app purchase resource: `POST /v2/inAppPurchases`, `GET`, and `PATCH`.
- The subscription resource: `POST /v1/subscriptions`, `GET`, and `PATCH`.
- The subscription group resource: `POST /v1/subscriptionGroups`, `GET`, and `PATCH`.
- Pricing: `/v1/inAppPurchasePriceSchedules` and `/v1/subscriptionPricePoints` remain the same.
- App Review screenshots: `/v1/inAppPurchaseAppStoreReviewScreenshots` and `/v1/subscriptionAppStoreReviewScreenshots` still target the parent product, not the version.
- Promoted purchases: `/v1/promotedPurchases` is unaffected.

For the full version workflow, see [`Working with in-app purchase versions`](working-with-in-app-purchase-versions.md), [`Working with subscription versions`](working-with-subscription-versions.md), and [`Working with subscription group versions`](working-with-subscription-group-versions.md).

## See Also

- [Managing in-app purchases](managing-in-app-purchases.md)
  Create in-app purchases, configure their metadata and pricing, submit them for review, and promote them with the App Store Connect API.
- [Working with in-app purchase versions](working-with-in-app-purchase-versions.md)
  Manage draft versions of an in-app purchase’s localized metadata and review images before submitting for App Review.
- [In-App Purchase Versions](in-app-purchase-versions.md)
  Create and read draft versions of an in-app purchase, with their localized metadata and review images.
- [In-App Purchases](in-app-purchases.md)
  Create, modify, and delete in-app purchases for your app.
- [In-App Purchase Localizations](in-app-purchase-localizations.md)
  Create, modify, and delete localized metadata for in-app purchase versions.
- [In-app purchase localizations (v1)](in-app-purchase-localizations-v1.md)
  Create, modify, and delete localized metadata for in-app purchases.
- [In-App purchase price schedules](in-app-purchase-price-schedules.md)
  Create a scheduled price change for an in-app purchase, and get information about scheduled price changes.
- [In-app purchase availability](in-app-purchase-availability.md)
  Read and modify territory availability for an in-app purchase.
- [In-app purchase images](in-app-purchase-images.md)
  Create, modify, and delete promotion images for in-app purchases.
- [In-app purchase images (v1)](in-app-purchase-images-v1.md)
  Create, modify, and delete promotion images for your in-app purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/migrating-in-app-purchase-metadata-to-v2)*