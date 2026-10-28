# lensDistortionCenter

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The offset of the distortion center of the camera lens from the top-left corner of the image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var lensDistortionCenter: CGPoint { get }
```

```objc
@property (nonatomic, readonly) CGPoint lensDistortionCenter;
```

## Discussion

Due to geometric distortions in the image, the center of the distortion may not be equal to the optical center (principal point) of the lens. When making an image rectilinear, use the distortion center rather than the optical center of the image.

## See Also

### Correcting for lens distortion
- [var lensDistortionLookupTable: Data?](./lensdistortionlookuptable.md)
  A map of floating-point values describing radial distortions imparted by the camera lens, for use in rectifying camera images.
- [var inverseLensDistortionLookupTable: Data?](./inverselensdistortionlookuptable.md)
  A map of floating-point values describing radial distortions for use in reapplying camera geometry to a rectified image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata/lensdistortioncenter)*