# com.apple.developer.avfoundation.multitasking-camera-access

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an app may continue using the camera at the same time as another foreground app.

**Availability**:
- iOS 13.5+
- iPadOS 13.5+

#### Discussion

When your app enters a multitasking mode, this entitlement allows it to continue using the camera. Multitasking modes include Slide Over, Split View, and Picture in Picture (PiP). For information about Picture in Picture, see [`Adopting Picture in Picture for video calls`](https://developer.apple.com/documentation/AVKit/adopting-picture-in-picture-for-video-calls).

> ❗ **Important**: Your app needs to run on iOS 13.5 or later to use this entitlement. Usage of this entitlement is restricted to apps that use `voip` as one of their [`UIBackgroundModes`](information-property-list/uibackgroundmodes.md).

Your app needs to run on iOS 13.5 or later to use this entitlement. Usage of this entitlement is restricted to apps that use `voip` as one of their [`UIBackgroundModes`](information-property-list/uibackgroundmodes.md).

## See Also

- [Media Device Discovery Extension](entitlements/com.apple.developer.media-device-discovery-extension.md)
  An entitlement for an app extension that adds a specific third-party media receiver to a system device-picker UI.
- [com.apple.developer.coremotion.head-pose](entitlements/com.apple.developer.coremotion.head-pose.md)
  An entitlement that enables someone’s head movement to determine the orientation of spatialized sound output.
- [com.apple.developer.spatial-audio.profile-access](entitlements/com.apple.developer.spatial-audio.profile-access.md)
  An entitlement that enables your app to use the personalized spatial audio profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.avfoundation.multitasking-camera-access)*