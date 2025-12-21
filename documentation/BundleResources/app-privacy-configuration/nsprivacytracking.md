# NSPrivacyTracking

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether your app or third-party SDK uses data for tracking.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

#### Overview

Set the value for this key to `true` if your app or third-party SDK uses data for tracking as defined under the App Tracking Transparency framework. When set to `true` you need to provide a list of internet domains in [`NSPrivacyTrackingDomains`](app-privacy-configuration/nsprivacytrackingdomains.md). For more information, see [`User Privacy and Data Use`](https://developer.apple.comhttps://developer.apple.com/app-store/user-privacy-and-data-use/).

## See Also

- [NSPrivacyTrackingDomains](app-privacy-configuration/nsprivacytrackingdomains.md)
  A list of the internet domains your app or third-party SDK uses for tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacytracking)*