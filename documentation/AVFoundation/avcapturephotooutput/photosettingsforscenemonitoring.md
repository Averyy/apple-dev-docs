# photoSettingsForSceneMonitoring

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) AVCapturePhotoSettings * photoSettingsForSceneMonitoring;
```

## Discussion

Set the [`flashMode`](../avcapturephotosettings/flashmode.md) and [`isAutoStillImageStabilizationEnabled`](../avcapturephotosettings/isautostillimagestabilizationenabled.md) properties of this photo settings object to influence the values of the photo output’s scene monitoring properties ([`isFlashScene`](./isflashscene.md) and [`isStillImageStabilizationScene`](./isstillimagestabilizationscene.md)). For example, if you set the [`flashMode`](../avcapturephotosettings/flashmode.md) property of this photo settings object to [`AVCaptureDevice.FlashMode.off`](../avcapturedevice/flashmode-swift.enum/off.md), the photo output’s [`isFlashScene`](./isflashscene.md) property reports [`false`](../../Swift/false.md) regardless of lighting conditions in the visible scene. If you set this photo settings object’s [`flashMode`](../avcapturephotosettings/flashmode.md) property to [`AVCaptureDevice.FlashMode.auto`](../avcapturedevice/flashmode-swift.enum/auto.md) or [`AVCaptureDevice.FlashMode.on`](../avcapturedevice/flashmode-swift.enum/on.md), the photo output’s [`isFlashScene`](./isflashscene.md) property reverts to its default behavior of returning [`true`](../../Swift/true.md) or [`false`](../../Swift/false.md) based on the visible light level.

> **Note**:  There is some overlap in the light level ranges that benefit from still image stabilization and flash. If this photo settings object indicates that the scene should be monitored for both still image stabilization and flash, still image stabilization takes precedence, and the [`isFlashScene`](./isflashscene.md) property becomes [`true`](../../Swift/true.md) at lower overall light levels.

The default value is an [`AVCapturePhotoSettings`](../avcapturephotosettings.md) object with the following settings:

- [`flashMode`](../avcapturephotosettings/flashmode.md): [`AVCaptureDevice.FlashMode.auto`](../avcapturedevice/flashmode-swift.enum/auto.md)
- [`isAutoStillImageStabilizationEnabled`](../avcapturephotosettings/isautostillimagestabilizationenabled.md): [`true`](../../Swift/true.md)

The photo output ignores all other properties of this photo settings object. To control other photo settings when requesting capture, create a photo settings object to pass to the [`capturePhoto(with:delegate:)`](./capturephoto%28with,delegate%29.md) method.

## See Also

### Monitoring the visible scene
- [var isFlashScene: Bool](./isflashscene.md)
  A Boolean value indicating whether the scene currently being previewed by the camera warrants use of the flash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/photosettingsforscenemonitoring)*