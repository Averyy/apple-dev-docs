# maxExposureDuration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A time value that indicates the maximum supported exposure duration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var maxExposureDuration: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime maxExposureDuration;
```

## See Also

### Determining exposure support
- [var systemRecommendedExposureBiasRange: ClosedRange<Float>?](./systemrecommendedexposurebiasrange.md)
  The system’s recommended exposure bias range for this device format.
- [var minISO: Float](./miniso.md)
  A floating-point number that indicates the minimum supported exposure ISO value.
- [var maxISO: Float](./maxiso.md)
  A floating-point number that indicates the maximum supported exposure ISO value.
- [var minExposureDuration: CMTime](./minexposureduration.md)
  A time value that indicates the minimum supported exposure duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/maxexposureduration)*