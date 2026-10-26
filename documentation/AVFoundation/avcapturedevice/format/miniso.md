# minISO

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A floating-point number that indicates the minimum supported exposure ISO value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var minISO: Float { get }
```

```objc
@property (nonatomic, readonly) float minISO;
```

## See Also

### Determining exposure support
- [var systemRecommendedExposureBiasRange: ClosedRange<Float>?](./systemrecommendedexposurebiasrange.md)
  The system’s recommended exposure bias range for this device format.
- [var maxISO: Float](./maxiso.md)
  A floating-point number that indicates the maximum supported exposure ISO value.
- [var minExposureDuration: CMTime](./minexposureduration.md)
  A time value that indicates the minimum supported exposure duration.
- [var maxExposureDuration: CMTime](./maxexposureduration.md)
  A time value that indicates the maximum supported exposure duration.
- [systemRecommendedExposureBiasRange](../../avcapturedeviceformat/systemrecommendedexposurebiasrange.md)
  The system’s recommended exposure bias range for this device format.
- [AVExposureBiasRange](../../avexposurebiasrange.md)
  An object that expresses an inclusive range of supported exposure bias values, in EV units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/miniso)*