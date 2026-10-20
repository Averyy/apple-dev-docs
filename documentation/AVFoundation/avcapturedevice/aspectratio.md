# AVCaptureDevice.AspectRatio

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

String constants describing the different video aspect ratios you can configure for a particular device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct AspectRatio
```

```c
typedef NSString * AVCaptureAspectRatio;
```

## Topics

### Aspect ratios
- [static let ratio16x9: AVCaptureDevice.AspectRatio](./aspectratio/ratio16x9.md)
  An aspect ratio of 16x9.
- [static let ratio1x1: AVCaptureDevice.AspectRatio](./aspectratio/ratio1x1.md)
  An aspect ratio of 1x1.
- [static let ratio3x4: AVCaptureDevice.AspectRatio](./aspectratio/ratio3x4.md)
  An aspect ratio of 3x4.
- [static let ratio4x3: AVCaptureDevice.AspectRatio](./aspectratio/ratio4x3.md)
  An aspect ratio of 4x3.
- [static let ratio9x16: AVCaptureDevice.AspectRatio](./aspectratio/ratio9x16.md)
  An aspect ratio of 9x16.
### Initializers
- [init(rawValue: String)](./aspectratio/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring dynamic aspect ratio
- [func setDynamicAspectRatio(AVCaptureDevice.AspectRatio, completionHandler: ((CMTime, (any Error)?) -> Void)?)](./setdynamicaspectratio%28_,completionhandler%29.md)
  Updates the dynamic aspect ratio of the device.
- [var dynamicAspectRatio: AVCaptureDevice.AspectRatio?](./dynamicaspectratio.md)
  A key-value observable property indicating the current aspect ratio for a device.
- [var dynamicDimensions: CMVideoDimensions](./dynamicdimensions.md)
  A key-value observable property describing the output dimensions of the video buffer based on the device’s dynamic aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/aspectratio)*