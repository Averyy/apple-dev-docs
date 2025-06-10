# radialLookupTable

**Framework**: RealityKit  
**Kind**: property

A linear interpolation lookup table from the `center` to the maximum distance corner of the image.  This describes the magnification of radius at a given radius. This is the same structure as `lensDistortionLookupTable` in `AVCameraCalibrationData` and can be used in a similar manner, with the data already converted into a float array.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
let radialLookupTable: [Float]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lensdistortiondata/radiallookuptable)*