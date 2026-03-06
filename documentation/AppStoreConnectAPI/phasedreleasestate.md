# PhasedReleaseState

**Framework**: App Store Connect API  
**Kind**: typealias

String that represents the progress of a phased release for an app version.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
string PhasedReleaseState
```

#### Possible Values

- **INACTIVE**: The phased release hasn’t started.
- **ACTIVE**: The app version is released. During a phased release, the App Store releases the update over a 7- termday period to a percentage of your users, randomly selected. The phased release applies to macOS and iOS devices with automatic updates enabled. Users can also manually download the app version.
- **PAUSED**: The App Store paused the phased release, at your request.
- **COMPLETE**: The process released the update to all devices that have automatic updates enabled. The phased- termrelease process is complete.

#### Discussion

For more information about phased releases including pausing an update, see [`Release a version update in phases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases/).

## See Also

- [object AppStoreVersionPhasedRelease](appstoreversionphasedrelease.md)
  The data structure that represent an App Store Version Phased Releases resource.
- [object AppStoreVersionPhasedReleaseCreateRequest](appstoreversionphasedreleasecreaterequest.md)
  The request body you use to create an App Store Version Phased Release.
- [object AppStoreVersionPhasedReleaseResponse](appstoreversionphasedreleaseresponse.md)
  A response that contains a single App Store Version Phased Releases resource.
- [object AppStoreVersionPhasedReleaseWithoutIncludesResponse](appstoreversionphasedreleasewithoutincludesresponse.md)
- [object AppStoreVersionPhasedReleaseUpdateRequest](appstoreversionphasedreleaseupdaterequest.md)
  The request body you use to update an App Store Version Phased Release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/phasedreleasestate)*