# kCGImagePropertyDNGBlackLevel

**Framework**: Image I/O  
**Kind**: var

The zero light encoding level, specified as a repeating pattern.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let kCGImagePropertyDNGBlackLevel: CFString
```

## See Also

- [let kCGImagePropertyDNGBlackLevelRepeatDim: CFString](kcgimagepropertydngblacklevelrepeatdim.md)
  The repeat pattern size for the black level tag.
- [let kCGImagePropertyDNGBlackLevelDeltaH: CFString](kcgimagepropertydngblackleveldeltah.md)
  The difference between the zero-light encoding level for each column and the baseline zero-light encoding level.
- [let kCGImagePropertyDNGBlackLevelDeltaV: CFString](kcgimagepropertydngblackleveldeltav.md)
  The difference between the zero-light encodoing level for each row and the baseline zero-light encoding level.
- [let kCGImagePropertyDNGWhiteLevel: CFString](kcgimagepropertydngwhitelevel.md)
  The saturated encoding level for the raw sample values.
- [let kCGImagePropertyDNGCalibrationIlluminant1: CFString](kcgimagepropertydngcalibrationilluminant1.md)
  The illuminant for the first set of color calibration tags.
- [let kCGImagePropertyDNGCalibrationIlluminant2: CFString](kcgimagepropertydngcalibrationilluminant2.md)
  The illuminant for an optional second set of color calibration tags.
- [let kCGImagePropertyDNGColorMatrix1: CFString](kcgimagepropertydngcolormatrix1.md)
  A transformation matrix that converts XYZ values to reference camera native color spaces, under the first calibration illuminant.
- [let kCGImagePropertyDNGColorMatrix2: CFString](kcgimagepropertydngcolormatrix2.md)
  A transformation matrix that converts XYZ values to reference camera native color spaces, under the second calibration illuminant.
- [let kCGImagePropertyDNGCameraCalibration1: CFString](kcgimagepropertydngcameracalibration1.md)
  A matrix that transforms reference camera native space values to camera-native space values under the first calibration illuminant.
- [let kCGImagePropertyDNGCameraCalibration2: CFString](kcgimagepropertydngcameracalibration2.md)
  A matrix that transforms reference camera native space values to camera-native space values under the second calibration illuminant.
- [let kCGImagePropertyDNGReductionMatrix1: CFString](kcgimagepropertydngreductionmatrix1.md)
  A reduction matrix that converts color camera-native space values to XYZ values, under the first calibration illuminant.
- [let kCGImagePropertyDNGReductionMatrix2: CFString](kcgimagepropertydngreductionmatrix2.md)
  A reduction matrix that converts color camera-native space values to XYZ values, under the second calibration illuminant.
- [let kCGImagePropertyDNGAsShotICCProfile: CFString](kcgimagepropertydngasshoticcprofile.md)
  A profile that specifies default color rendering from camera color-space coordinates into the ICC profile space.
- [let kCGImagePropertyDNGAsShotPreProfileMatrix: CFString](kcgimagepropertydngasshotpreprofilematrix.md)
  A matrix to apply to the camera color-space coordinates before processing values through the ICC profile.
- [let kCGImagePropertyDNGCurrentICCProfile: CFString](kcgimagepropertydngcurrenticcprofile.md)
  A profile that specifies default color rendering from camera color-space coordinates into the ICC profile space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertydngblacklevel)*