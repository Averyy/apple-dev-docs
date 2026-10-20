# CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection

**Framework**: Core Media  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum CameraCalibrationDataLensCollection
```

## Topics

### Structures
- [CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.Calibration](./cameracalibrationdatalenscollection/calibration.md)
### Enumeration Cases
- [case mono(CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.Calibration)](./cameracalibrationdatalenscollection/mono%28_%29.md)
  Lens calibration for a single camera
- [case stereo(left: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.Calibration, right: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.Calibration)](./cameracalibrationdatalenscollection/stereo%28left,right%29.md)
  Lens calibration for stereo cameras
### Enumerations
- [CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.AlgorithmKind](./cameracalibrationdatalenscollection/algorithmkind.md)
  Specifies the camera calibration methodology.
- [CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.ExtrinsicOriginSource](./cameracalibrationdatalenscollection/extrinsicoriginsource.md)
  Identifies how the origin of the camera system’s extrinsics are determined.
- [CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.LensDomain](./cameracalibrationdatalenscollection/lensdomain.md)
  Specifies the kind of lens
- [CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.LensRole](./cameracalibrationdatalenscollection/lensrole.md)
  Specifies the particular use of the lens in the camera system (e.g., left or right for a stereo system).

## Relationships

### Conforms To
- [RawRepresentable](../../../../Swift/rawrepresentable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection)*