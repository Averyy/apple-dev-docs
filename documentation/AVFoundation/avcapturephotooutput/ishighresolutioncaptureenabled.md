# isHighResolutionCaptureEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether to configure the capture pipeline for high resolution still image capture.

**Availability**:
- iOS 10.0+ - Deprecated in 16.0
- iPadOS 10.0+ - Deprecated in 16.0
- Mac Catalyst 14.0+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 13.0

> **Deprecated**: Use [`maxPhotoDimensions`](./maxphotodimensions.md) instead.

## Declaration

```swift
var isHighResolutionCaptureEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isHighResolutionCaptureEnabled) BOOL highResolutionCaptureEnabled;
```

## Discussion

Some capture formats support output of still images at a resolution higher than the resolution they use for live preview and video capture (see the [`AVCaptureDevice.Format`](../avcapturedevice/format.md) [`highResolutionStillImageDimensions`](../avcapturedevice/format/highresolutionstillimagedimensions.md) property). Under some conditions, a capture session needs to set up its internal rendering pipeline differently to support high resolution still image capture.

If you intend to take high resolution still images at all, set this property to  before calling the [`AVCaptureSession`](../avcapturesession.md)  [`startRunning()`](../avcapturesession/startrunning%28%29.md) method. Changing this property while the session is running requires a lengthy reconfiguration of the capture render pipeline: Live Photo captures in progress will end immediately, unfulfilled photo requests will abort, and video preview will temporarily freeze.

You must enable this option before initiating a photo capture with the [`isHighResolutionPhotoEnabled`](../avcapturephotosettings/ishighresolutionphotoenabled.md) property of your photo settings object set to [`true`](../../Swift/true.md). However, after you’ve enabled this option, you are free to issue photo capture requests with any [`isHighResolutionPhotoEnabled`](../avcapturephotosettings/ishighresolutionphotoenabled.md) setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/ishighresolutioncaptureenabled)*