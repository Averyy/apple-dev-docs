# NSWorldSensingUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

**Availability**:
- visionOS 1.0+



**Type**: string

#### Discussion

Use this key to indicate that your app requires access to world-sensing data. This includes plane detection, image tracking, and scene-reconstruction anchors. The first time your app tries to access world-sensing data, the system prompts for permission. Provide a string for the prompt that explains why your app needs access. For more information on setting up ARKit for world sensing, see [`Setting up access to ARKit data`](https://developer.apple.com/documentation/visionOS/setting-up-access-to-arkit-data).

> **Note**:  World tracking — unlike world sensing — doesn’t require authorization. For more information, see [`Tracking specific points in world space`](https://developer.apple.com/documentation/visionOS/tracking-points-in-world-space).

## See Also

- [NSHandsTrackingUsageDescription](information-property-list/nshandstrackingusagedescription.md)
- [NSAccessoryTrackingUsageDescription](information-property-list/nsaccessorytrackingusagedescription.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsworldsensingusagedescription)*