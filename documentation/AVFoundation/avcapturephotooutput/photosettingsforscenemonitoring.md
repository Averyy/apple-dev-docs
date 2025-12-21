# photoSettingsForSceneMonitoring

**Framework**: AVFoundation  
**Kind**: property

A photo settings object that controls how the photo output detects and handles automatic flash and stabilization modes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
@NSCopying
var photoSettingsForSceneMonitoring: AVCapturePhotoSettings? { get set }
```

#### Discussion

Set the [`flashMode`](avcapturephotosettings/flashmode.md) and [`isAutoStillImageStabilizationEnabled`](avcapturephotosettings/isautostillimagestabilizationenabled.md) properties of this photo settings object to influence the values of the photo output’s scene monitoring properties ([`isFlashScene`](avcapturephotooutput/isflashscene.md) and [`isStillImageStabilizationScene`](avcapturephotooutput/isstillimagestabilizationscene.md)). For example, if you set the [`flashMode`](avcapturephotosettings/flashmode.md) property of this photo settings object to [`AVCaptureDevice.FlashMode.off`](avcapturedevice/flashmode-swift.enum/off.md), the photo output’s [`isFlashScene`](avcapturephotooutput/isflashscene.md) property reports [`false`](https://developer.apple.com/documentation/Swift/false) regardless of lighting conditions in the visible scene. If you set this photo settings object’s [`flashMode`](avcapturephotosettings/flashmode.md) property to [`AVCaptureDevice.FlashMode.auto`](avcapturedevice/flashmode-swift.enum/auto.md) or [`AVCaptureDevice.FlashMode.on`](avcapturedevice/flashmode-swift.enum/on.md), the photo output’s [`isFlashScene`](avcapturephotooutput/isflashscene.md) property reverts to its default behavior of returning [`true`](https://developer.apple.com/documentation/Swift/true) or [`false`](https://developer.apple.com/documentation/Swift/false) based on the visible light level.

> **Note**:  There is some overlap in the light level ranges that benefit from still image stabilization and flash. If this photo settings object indicates that the scene should be monitored for both still image stabilization and flash, still image stabilization takes precedence, and the [`isFlashScene`](avcapturephotooutput/isflashscene.md) property becomes [`true`](https://developer.apple.com/documentation/Swift/true) at lower overall light levels.

The default value is an [`AVCapturePhotoSettings`](avcapturephotosettings.md) object with the following settings:

- [`flashMode`](avcapturephotosettings/flashmode.md): [`AVCaptureDevice.FlashMode.auto`](avcapturedevice/flashmode-swift.enum/auto.md)
- [`isAutoStillImageStabilizationEnabled`](avcapturephotosettings/isautostillimagestabilizationenabled.md): [`true`](https://developer.apple.com/documentation/Swift/true)

The photo output ignores all other properties of this photo settings object. To control other photo settings when requesting capture, create a photo settings object to pass to the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method.

## See Also

- [var isFlashScene: Bool](avcapturephotooutput/isflashscene.md)
  A Boolean value indicating whether the scene currently being previewed by the camera warrants use of the flash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/photosettingsforscenemonitoring)*