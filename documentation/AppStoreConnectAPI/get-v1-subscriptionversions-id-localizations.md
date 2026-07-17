# List localizations for a subscription version

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the localized display names and descriptions captured in a draft version of an auto-renewable subscription.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](app-store-connect-api-4-4-1-release-notes.md)
- [Working with subscription versions](working-with-subscription-versions.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionVersions/{id}/localizations`

## Parameters

- `fields[subscriptionLocalizations]` ([string])
- `fields[subscriptionVersions]` ([string])
- `limit` (integer)
- `include` ([string])

## See Also

- [Create a subscription version](post-v1-subscriptionversions.md)
  Create a draft version of an auto-renewable subscription, capturing its current localized metadata and review images for App Review submission.
- [Read subscription version information](get-v1-subscriptionversions-_id_.md)
  Get information about a specific draft version of an auto-renewable subscription.
- [Read the image for a subscription version](get-v1-subscriptionversions-_id_-image.md)
  Get the review image attached to a draft version of an auto-renewable subscription.
- [List images for a subscription version](get-v1-subscriptionversions-_id_-images.md)
  List the review images attached to a draft version of an auto-renewable subscription.
- [Read the image ID for a subscription version](get-v1-subscriptionversions-_id_-relationships-image.md)
  Get the related resource ID for the review image attached to a draft version of an auto-renewable subscription.
- [List image IDs for a subscription version](get-v1-subscriptionversions-_id_-relationships-images.md)
  Get the related resource IDs for the review images attached to a draft version of an auto-renewable subscription.
- [List localization IDs for a subscription version](get-v1-subscriptionversions-_id_-relationships-localizations.md)
  Get the related resource IDs for the localizations captured in a draft version of an auto-renewable subscription.
- [List versions for a subscription](get-v1-subscriptions-_id_-versions.md)
  List the draft versions of an auto-renewable subscription.
- [List version IDs for a subscription](get-v1-subscriptions-_id_-relationships-versions.md)
  Get the related resource IDs for the draft versions of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionversions-_id_-localizations)*