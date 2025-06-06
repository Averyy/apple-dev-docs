# systemRecommendedExposureBiasRange

**Framework**: Avfoundation  
**Kind**: property

The system’s recommended exposure bias range for this device format.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
@nonobjc
var systemRecommendedExposureBiasRange: ClosedRange<Float>? { get }
```

#### Discussion

Use this value to create a slider in your app’s user interface that controls a device’s exposure bias within a system-recommended range. When a recommendation isn’t available, this property returns `nil`.

> **Note**:  The framework uses this value to define the range of an [`AVCaptureSystemExposureBiasSlider`](avcapturesystemexposurebiasslider.md) control.

## See Also

- [var minISO: Float](avcapturedevice/format/miniso.md)
  A floating-point number that indicates the minimum supported exposure ISO value.
- [var maxISO: Float](avcapturedevice/format/maxiso.md)
  A floating-point number that indicates the maximum supported exposure ISO value.
- [var minExposureDuration: CMTime](avcapturedevice/format/minexposureduration.md)
  A time value that indicates the minimum supported exposure duration.
- [var maxExposureDuration: CMTime](avcapturedevice/format/maxexposureduration.md)
  A time value that indicates the maximum supported exposure duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/systemrecommendedexposurebiasrange)*