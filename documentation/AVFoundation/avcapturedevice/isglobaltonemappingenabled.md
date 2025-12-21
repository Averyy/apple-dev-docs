# isGlobalToneMappingEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the device should use global tone mapping.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isGlobalToneMappingEnabled: Bool { get set }
```

#### Discussion

Tone mapping is a technique used to map the pixel levels in high dynamic range images to a reduced dynamic range (such as mapping from 16-bit to 8-bit), while still retaining an appearance as close to the original image as possible. Normally the active camera uses adaptive, local tone curves to preserve the highest image quality and adapt quickly to changing lighting conditions.

When this property value is true, the tone map adjusts dynamically depending on the current scene and applies to all pixels in an image. You can only enable this setting if the device’s active format’s [`isGlobalToneMappingSupported`](avcapturedevice/format/isglobaltonemappingsupported.md) property returns [`true`](https://developer.apple.com/documentation/Swift/true). If set to its default value of [`false`](https://developer.apple.com/documentation/Swift/false), the framework may apply different tone maps to different pixels in an image.

This property resets to its default value of [`false`](https://developer.apple.com/documentation/Swift/false) under the following conditions:

- You change the device’s active format.
- You add the device’s input to a session.
- You change the capture session’s preset value.

Key-value observe this property to observe automatic changes to its value.

> **Note**:  When you enable global tone mapping, an [`AVCapturePhotoOutput`](avcapturephotooutput.md) object connected to the device input’s session disables all forms of still image fusion, resulting in still images with no automatic stabilization applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isglobaltonemappingenabled)*