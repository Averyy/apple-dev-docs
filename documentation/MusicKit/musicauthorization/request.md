# request()

**Framework**: MusicKit  
**Kind**: method

Asks the user for permission for the current app to access MusicKit.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func request() async -> MusicAuthorization.Status
```

#### Discussion

Before using any other MusicKit API in your app, make sure the user grants your app access to their Apple Music data, You can do this either by comparing [`currentStatus`](musicauthorization/currentstatus.md) to [`MusicAuthorization.Status.authorized`](musicauthorization/status/authorized.md), or by simply calling [`request()`](musicauthorization/request().md) regardless of the current authorization status value. Calling [`request()`](musicauthorization/request().md) results in presenting a standard user consent dialog to the user when necessary.

Requesting authorization to use MusicKit requires the inclusion of a short description of the app’s reason for using MusicKit. You need to add this purpose string to the app’s `Info.plist` file using the [`NSAppleMusicUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription) key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicauthorization/request())*