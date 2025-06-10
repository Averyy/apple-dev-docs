# CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection

**Framework**: Core Media  
**Kind**: enum

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
enum CameraCalibrationDataLensCollection
```

## Topics

### Structures
- [CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.Calibration](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration.md)
### Enumeration Cases
- [case mono(CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.Calibration)](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/mono(_:).md)
  Lens calibration for a single camera
- [case stereo(left: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.Calibration, right: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.Calibration)](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/stereo(left:right:).md)
  Lens calibration for stereo cameras
### Enumerations
- [CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.AlgorithmKind](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/algorithmkind.md)
  Specifies the camera calibration methodology.
- [CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.ExtrinsicOriginSource](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/extrinsicoriginsource.md)
  Identifies how the origin of the camera system’s extrinsics are determined.
- [CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.LensDomain](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/lensdomain.md)
  Specifies the kind of lens
- [CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.LensRole](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/lensrole.md)
  Specifies the particular use of the lens in the camera system (e.g., left or right for a stereo system).

## Relationships

### Conforms To
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection)*