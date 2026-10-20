# Media Device Discovery Extension

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An entitlement for an app extension that adds a specific third-party media receiver to a system device-picker UI.

**Availability**:
- iOS 16.0+ - Deprecated in 27.0
- iPadOS 16.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: This entitlement is deprecated. For Media Sharing Extensions, use [com.apple.developer.media-device-extension](./com.apple.developer.media-device-extension.md) instead.

## Details

- **Name**: `com.apple.developer.media-device-discovery-extension`
- **Type**: boolean

#### Discussion

To add this entitlement to your app extension, enable the Media Device Discovery capability in Xcode. For more information, see [Configuring media device discovery](../../Xcode/configuring-media-device-discovery.md).

## See Also

### Media
- [com.apple.developer.media-device-extension](./com.apple.developer.media-device-extension.md)
  An array of media sharing protocol identifiers that an extension supports.
- [com.apple.developer.coremotion.head-pose](./com.apple.developer.coremotion.head-pose.md)
  An entitlement that enables someone’s head movement to determine the orientation of spatialized sound output.
- [com.apple.developer.spatial-audio.profile-access](./com.apple.developer.spatial-audio.profile-access.md)
  An entitlement that enables your app to use the personalized spatial audio profile.
- [com.apple.developer.avfoundation.multitasking-camera-access](./com.apple.developer.avfoundation.multitasking-camera-access.md)
  A Boolean value that indicates whether an app may continue using the camera at the same time as another foreground app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.media-device-discovery-extension)*