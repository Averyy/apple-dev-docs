# Working with subscription group versions

**Framework**: App Store Connect API

Manage draft versions of a subscription group’s localized metadata before submitting for App Review.

#### Overview

A subscription group version is a draft container for the group’s localized names — the display names and optional custom app names that customers see for the whole subscription group. Group versions carry only localizations; they don’t have review images. Create a version, attach localizations to it, then submit the version through the review submissions workflow. The parent subscription group holds properties that stay stable across versions — its reference name and app relationship — while each version captures the reviewable metadata for a single review cycle.

> **Note**:  The pre-4.4.1 workflow that posts localizations directly to the subscription group (`POST /v1/subscriptionGroupLocalizations`) is deprecated as of 4.4.1 but remains available for existing integrations. For guidance on moving to the version-based workflow, see [`Migrating in-app purchase metadata to v2`](migrating-in-app-purchase-metadata-to-v2.md).

Group-level localizations submit to App Review with the subscriptions they belong to. Submit a subscription group version independently only when you change group-level localization without changing any subscription in the group.

##### Understand the Version Lifecycle

A version moves through these states, exposed on `SubscriptionGroupVersion/Attributes/state`:

- `PREPARE_FOR_SUBMISSION`: the version is being edited. Localizations can be added, changed, or removed.
- `READY_FOR_REVIEW`: the version is attached to a review submission and awaiting the submission to be marked `submitted`.
- `WAITING_FOR_REVIEW`: the review submission has been submitted and the version is queued.
- `IN_REVIEW`: App Review is actively reviewing the version.
- `ACCEPTED` or `APPROVED`: the version passed review.
- `REJECTED` or `DEVELOPER_REJECTED`: the version was rejected by App Review or withdrawn by the developer.
- `REPLACED_WITH_NEW_VERSION`: a newer version supersedes this one.

Versions are read-only after creation. To change a version’s contents, create a new version.

##### Create a Version

Create a draft version with `POST /v1/subscriptionGroupVersions` ([`Create a subscription group version`](post-v1-subscriptiongroupversions.md)). Relate it to the subscription group whose metadata you’re updating:

```json
{
  "data": {
    "type": "subscriptionGroupVersions",
    "relationships": {
      "subscriptionGroup": {
        "data": {
          "type": "subscriptionGroups",
          "id": "2000036297"
        }
      }
    }
  }
}
```

The response returns the new version’s `id` and a `state` of `PREPARE_FOR_SUBMISSION`. Note the `id` — every subsequent step references it.

##### Attach a Localization to the Version

Add a localized display name and optional custom app name with `POST /v2/subscriptionGroupLocalizations` ([`Create a subscription group localization`](post-v2-subscriptiongrouplocalizations.md)). The payload relates the localization to the version, not the parent subscription group:

```json
{
  "data": {
    "type": "subscriptionGroupLocalizations",
    "attributes": {
      "locale": "en-AU",
      "name": "Ukulele Lessons",
      "customAppName": "The Best Ukulele Lessons"
    },
    "relationships": {
      "version": {
        "data": {
          "type": "subscriptionGroupVersions",
          "id": "${subscriptionGroupVersionId}"
        }
      }
    }
  }
}
```

Repeat for each locale you support. To list the localizations attached to a version, use `GET /v1/subscriptionGroupVersions/{id}/localizations` ([`List the localizations of a subscription group version`](get-v1-subscriptiongroupversions-_id_-localizations.md)).

##### List All Versions for a Subscription Group

To see every version on a parent subscription group, use `GET /v1/subscriptionGroups/{id}/versions` ([`List the versions of a subscription group`](get-v1-subscriptiongroups-_id_-versions.md)). The response includes each version’s state, so you can find the current draft, the most recently approved version, and any versions currently in review.

##### Submit the Version

Submit a completed version through the review submissions workflow. Create a review submission for the app, add the version as an item, and mark the submission as `submitted`. For step-by-step instructions, see [`Submitting subscriptions and subscription groups for App Review`](submitting-subscriptions-and-subscription-groups-for-app-review.md).

When you mark the submission `submitted`, the version moves from `READY_FOR_REVIEW` to `WAITING_FOR_REVIEW`. Poll `GET /v1/subscriptionGroupVersions/{id}` ([`Read subscription group version information`](get-v1-subscriptiongroupversions-_id_.md)) to watch it continue to `IN_REVIEW` and then `APPROVED` or `REJECTED`.

## See Also

- [Creating auto-renewable subscription groups](creating-auto-renewable-subscription-groups.md)
  Configure subscription groups with the App Store Connect API.
- [Subscription Group Versions](subscription-group-versions.md)
  Create and read draft versions of a subscription group with their localized metadata.
- [Subscription Groups](subscription-groups.md)
  Create, modify, and delete subscription groups for your app.
- [Subscription Group Localizations](subscription-group-localizations.md)
  Create, modify, and delete localized metadata for subscription groups.
- [Subscription group localizations (v1)](subscription-group-localizations-v1.md)
  Create, modify, and delete localized metadata for subscription groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/working-with-subscription-group-versions)*