# NSPrivacyTrackingDomains

**Framework**: Bundle Resources  
**Kind**: typealias

A list of the internet domains your app or third-party SDK uses for tracking.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

#### Overview

If the user has not granted tracking permission through the App Tracking Transparency framework, network requests to these domains fail and your app receives an error. To provide a list of internet domains in `NSPrivacyTrackingDomains`, set [`NSPrivacyTracking`](app-privacy-configuration/nsprivacytracking.md) to `true`. For more information, see [`User Privacy and Data Use`](https://developer.apple.comhttps://developer.apple.com/app-store/user-privacy-and-data-use/).

## See Also

- [NSPrivacyTracking](app-privacy-configuration/nsprivacytracking.md)
  A Boolean value that indicates whether your app or third-party SDK uses data for tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacytrackingdomains)*