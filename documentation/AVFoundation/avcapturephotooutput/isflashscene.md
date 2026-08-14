# isFlashScene

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether the scene currently being previewed by the camera warrants use of the flash.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isFlashScene: Bool { get }
```

#### Discussion

This property’s value changes depending on the scene currently visible to the camera. For example, you might use this property to highlight the flash control in your app’s camera UI, indicating to the user that the scene is dark enough that enabling the flash might be desirable.

If the photo capture output’s [`supportedFlashModes`](avcapturephotooutput/supportedflashmodes-4u69s.md) value is [`AVCaptureDevice.FlashMode.off`](avcapturedevice/flashmode-swift.enum/off.md), this property’s value is always [`false`](https://developer.apple.com/documentation/swift/false).

This property supports key-value observing.

## See Also

- [var photoSettingsForSceneMonitoring: AVCapturePhotoSettings?](avcapturephotooutput/photosettingsforscenemonitoring.md)
  A photo settings object that controls how the photo output detects and handles automatic flash and stabilization modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isflashscene)*