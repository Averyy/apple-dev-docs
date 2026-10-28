# AVExposureBiasRange

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that expresses an inclusive range of supported exposure bias values, in EV units.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```objc
@interface AVExposureBiasRange : NSObject
```

## Overview

A [`AVCaptureSystemExposureBiasSlider`](./avcapturesystemexposurebiasslider.md) defines its range using this type.

## Topics

### Inspecting the exposure bias range
- [minExposureBias](./avexposurebiasrange/minexposurebias.md)
  The minimum exposure bias in EV units that this range supports.
- [maxExposureBias](./avexposurebiasrange/maxexposurebias.md)
  The maximum exposure bias in EV units that this range supports.
- [- containsExposureBias:](./avexposurebiasrange/containsexposurebias_.md)
  Determines whether the range contains the specified exposure bias.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Determining exposure support
- [systemRecommendedExposureBiasRange](./avcapturedeviceformat/systemrecommendedexposurebiasrange.md)
  The system’s recommended exposure bias range for this device format.
- [var minISO: Float](./avcapturedevice/format/miniso.md)
  A floating-point number that indicates the minimum supported exposure ISO value.
- [var maxISO: Float](./avcapturedevice/format/maxiso.md)
  A floating-point number that indicates the maximum supported exposure ISO value.
- [var minExposureDuration: CMTime](./avcapturedevice/format/minexposureduration.md)
  A time value that indicates the minimum supported exposure duration.
- [var maxExposureDuration: CMTime](./avcapturedevice/format/maxexposureduration.md)
  A time value that indicates the maximum supported exposure duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexposurebiasrange)*