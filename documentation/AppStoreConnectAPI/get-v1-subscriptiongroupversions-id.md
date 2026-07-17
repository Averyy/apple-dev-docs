# Read subscription group version information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific draft version of a subscription group.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](app-store-connect-api-4-4-1-release-notes.md)
- [Working with subscription group versions](working-with-subscription-group-versions.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionGroupVersions/{id}`

## Parameters

- `fields[subscriptionGroupVersions]` ([string])
- `fields[subscriptionGroups]` ([string])
- `fields[subscriptionGroupLocalizations]` ([string])
- `include` ([string])
- `limit[localizations]` (integer)

## See Also

- [Create a subscription group version](post-v1-subscriptiongroupversions.md)
  Create a draft version of a subscription group, capturing its current localized metadata for App Review submission.
- [List the localizations of a subscription group version](get-v1-subscriptiongroupversions-_id_-localizations.md)
  List the localized custom names captured in a draft version of a subscription group.
- [Get the resource IDs of the localizations of a subscription group version](get-v1-subscriptiongroupversions-_id_-relationships-localizations.md)
  Get the related resource IDs for the localizations captured in a draft version of a subscription group.
- [List the versions of a subscription group](get-v1-subscriptiongroups-_id_-versions.md)
  List the draft versions of a subscription group.
- [Get the resource IDs of the versions of a subscription group](get-v1-subscriptiongroups-_id_-relationships-versions.md)
  Get the related resource IDs for the draft versions of a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptiongroupversions-_id_)*