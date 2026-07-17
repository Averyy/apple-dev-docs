# Create a subscription group version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create a draft version of a subscription group, capturing its current localized metadata for App Review submission.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](app-store-connect-api-4-4-1-release-notes.md)
- [Creating auto-renewable subscription groups](creating-auto-renewable-subscription-groups.md)
- [Submitting subscriptions and subscription groups for App Review](submitting-subscriptions-and-subscription-groups-for-app-review.md)
- [Working with subscription group versions](working-with-subscription-group-versions.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionGroupVersions`

## See Also

- [Read subscription group version information](get-v1-subscriptiongroupversions-_id_.md)
  Get information about a specific draft version of a subscription group.
- [List the localizations of a subscription group version](get-v1-subscriptiongroupversions-_id_-localizations.md)
  List the localized custom names captured in a draft version of a subscription group.
- [Get the resource IDs of the localizations of a subscription group version](get-v1-subscriptiongroupversions-_id_-relationships-localizations.md)
  Get the related resource IDs for the localizations captured in a draft version of a subscription group.
- [List the versions of a subscription group](get-v1-subscriptiongroups-_id_-versions.md)
  List the draft versions of a subscription group.
- [Get the resource IDs of the versions of a subscription group](get-v1-subscriptiongroups-_id_-relationships-versions.md)
  Get the related resource IDs for the draft versions of a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptiongroupversions)*