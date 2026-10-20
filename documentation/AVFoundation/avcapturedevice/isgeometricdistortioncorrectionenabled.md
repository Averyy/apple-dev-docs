# isGeometricDistortionCorrectionEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether geometric distortion correction is enabled for this device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isGeometricDistortionCorrectionEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isGeometricDistortionCorrectionEnabled) BOOL geometricDistortionCorrectionEnabled;
```

#### Discussion

When the device supports geometric distortion correction (GDC), the default value is [`true`](../../Swift/true.md).

## See Also

### Enabling geometric distortion correction
- [var isGeometricDistortionCorrectionSupported: Bool](./isgeometricdistortioncorrectionsupported.md)
  A Boolean value that indicates whether this device supports geometric distortion correction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isgeometricdistortioncorrectionenabled)*