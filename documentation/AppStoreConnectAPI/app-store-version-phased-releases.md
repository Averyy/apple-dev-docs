# App Store Version Phased Releases

**Framework**: App Store Connect API

Manage phased releases of updates to your app.

#### Overview

`appStoreVersionPhasedReleases` handles your process of releasing app updates to customers in stages. Use this resource to set up your process for an app update. This resource is not available for the first version of an app, only for subsequent releases.

For more information, see [`Release a version update in phases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases).

## Topics

### Managing Phased Releases
- [Create an App Store Version Phased Release](post-v1-appstoreversionphasedreleases.md)
  Enable phased release for an App Store version.
- [Modify an App Store Version Phased Release](patch-v1-appstoreversionphasedreleases-_id_.md)
  Pause or resume a phased release, or immediately release an app.
### Canceling Phased Releases
- [Delete an App Store Version Phased Release](delete-v1-appstoreversionphasedreleases-_id_.md)
  Cancel a planned phased release that has not been started.
### Objects and Data Types
- [object AppStoreVersionPhasedRelease](appstoreversionphasedrelease.md)
  The data structure that represent an App Store Version Phased Releases resource.
- [object AppStoreVersionPhasedReleaseCreateRequest](appstoreversionphasedreleasecreaterequest.md)
  The request body you use to create an App Store Version Phased Release.
- [object AppStoreVersionPhasedReleaseResponse](appstoreversionphasedreleaseresponse.md)
  A response that contains a single App Store Version Phased Releases resource.
- [object AppStoreVersionPhasedReleaseWithoutIncludesResponse](appstoreversionphasedreleasewithoutincludesresponse.md)
- [object AppStoreVersionPhasedReleaseUpdateRequest](appstoreversionphasedreleaseupdaterequest.md)
  The request body you use to update an App Store Version Phased Release.
- [type PhasedReleaseState](phasedreleasestate.md)
  String that represents the progress of a phased release for an app version.

## See Also

- [App Store Version Release Requests](app-store-version-release-requests.md)
  Manually release an App Store approved version of your app to the App Store.
- [App Pre-Orders](app-pre-orders.md)
  Manage the settings that make your app available for pre-order.
- [App availability](app-availability.md)
  Manage territory and date settings that make your app available for pre-order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-version-phased-releases)*