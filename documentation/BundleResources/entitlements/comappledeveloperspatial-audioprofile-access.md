# com.apple.developer.spatial-audio.profile-access

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that enables your app to use the personalized spatial audio profile.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

#### Discussion

This entitlement applies the personalized spatial audio profile someone makes in Settings to your app’s audio output for the following APIs:

- [`AVAudioEngine`](https://developer.apple.com/documentation/AVFAudio/AVAudioEngine)
- AUSpatialMixer in [`Audio Toolbox`](https://developer.apple.com/documentation/AudioToolbox) (see [`AUSpatialMixer Parameters`](https://developer.apple.com/documentation/AudioToolbox/1390073-auspatialmixer-parameters))
- [`PHASE`](https://developer.apple.com/documentation/PHASE)

Add this entitlement to your app by enabling the Spatial Audio Profile capability in Xcode.

> **Note**:  In iOS 18 and tvOS 18 and later, the system automatically adds spatial audio to the output for games. To opt out of automatic spatial  audio and support just your preferred spatial audio setup, add the [`AVGameBypassSystemSpatialAudio`](information-property-list/avgamebypasssystemspatialaudio.md) key to your app’s `Info.plist`.

## See Also

- [Media Device Discovery Extension](entitlements/com.apple.developer.media-device-discovery-extension.md)
  An entitlement for an app extension that adds a specific third-party media receiver to a system device-picker UI.
- [com.apple.developer.coremotion.head-pose](entitlements/com.apple.developer.coremotion.head-pose.md)
  An entitlement that enables someone’s head movement to determine the orientation of spatialized sound output.
- [com.apple.developer.avfoundation.multitasking-camera-access](entitlements/com.apple.developer.avfoundation.multitasking-camera-access.md)
  A Boolean value that indicates whether an app may continue using the camera at the same time as another foreground app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.spatial-audio.profile-access)*