# inverseLensDistortionLookupTable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A map of floating-point values describing radial distortions for use in reapplying camera geometry to a rectified image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var inverseLensDistortionLookupTable: Data? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSData * inverseLensDistortionLookupTable;
```

#### Discussion

If you’ve rectified an image by removing the distortions characterized by the [`lensDistortionLookupTable`](./lensdistortionlookuptable.md) property, and now wish to go back to a geometrically distorted image (for example, to render visual effects into the camera image or perform computer vision tasks such as scene reconstruction), use this inverse lookup table.

## See Also

### Correcting for lens distortion
- [var lensDistortionLookupTable: Data?](./lensdistortionlookuptable.md)
  A map of floating-point values describing radial distortions imparted by the camera lens, for use in rectifying camera images.
- [var lensDistortionCenter: CGPoint](./lensdistortioncenter.md)
  The offset of the distortion center of the camera lens from the top-left corner of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata/inverselensdistortionlookuptable)*