# com.apple.developer.coremotion.head-pose

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that enables someone’s head movement to determine the orientation of spatialized sound output.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+

#### Discussion

This entitlement changes the orientation of spatial audio output to match the person’s head pose via compatible AirPods for the following APIs:

- [`AVAudioEnvironmentNode`](https://developer.apple.com/documentation/AVFAudio/AVAudioEnvironmentNode), when you set the [`isListenerHeadTrackingEnabled`](https://developer.apple.com/documentation/AVFAudio/AVAudioEnvironmentNode/isListenerHeadTrackingEnabled) property to `true`
- [`Audio Toolbox`](https://developer.apple.com/documentation/AudioToolbox) (see [`AUSpatialMixer Parameters`](https://developer.apple.com/documentation/AudioToolbox/1390073-auspatialmixer-parameters)), when you set the [`kAudioUnitProperty_SpatialMixerEnableHeadTracking`](https://developer.apple.com/documentation/AudioToolbox/kAudioUnitProperty_SpatialMixerEnableHeadTracking) property to `true`
- [`PHASEListener`](https://developer.apple.com/documentation/PHASE/PHASEListener), when you set the new [`automaticHeadTrackingFlags`](https://developer.apple.com/documentation/PHASE/PHASEListener/automaticHeadTrackingFlags) property to orientation

Add this entitlement to your app by enabling the Head Pose capability in Xcode.

## See Also

- [Media Device Discovery Extension](entitlements/com.apple.developer.media-device-discovery-extension.md)
  An entitlement for an app extension that adds a specific third-party media receiver to a system device-picker UI.
- [com.apple.developer.spatial-audio.profile-access](entitlements/com.apple.developer.spatial-audio.profile-access.md)
  An entitlement that enables your app to use the personalized spatial audio profile.
- [com.apple.developer.avfoundation.multitasking-camera-access](entitlements/com.apple.developer.avfoundation.multitasking-camera-access.md)
  A Boolean value that indicates whether an app may continue using the camera at the same time as another foreground app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.coremotion.head-pose)*