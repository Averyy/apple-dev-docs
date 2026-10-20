# NSHandsTrackingUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A message that tells people why the app is requesting access to track their hand position and location.

**Availability**:
- visionOS 1.0+

## Details

- **Name**: `NSHandsTrackingUsageDescription` (Privacy - Hands Tracking Usage Description)
- **Type**: string

#### Discussion

Use this key to indicate that your app requires access to hand-tracking data. This includes hand skeleton, wrist, and forearm position and location. The first time your app tries to access hand-tracking data, the system prompts for permission. Provide a string for the prompt that explains why your app needs access. For more information on setting up ARKit for hand tracking, see [Setting up access to ARKit data](../../visionOS/setting-up-access-to-arkit-data.md).

## See Also

### Vision
- [NSWorldSensingUsageDescription](./nsworldsensingusagedescription.md)
  A message that tells people why the app is requesting access to image tracking, plane detection, or scene reconstruction.
- [NSAccessoryTrackingUsageDescription](./nsaccessorytrackingusagedescription.md)
  A message that tells a person why the app is requesting access to track accessory position and location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nshandstrackingusagedescription)*