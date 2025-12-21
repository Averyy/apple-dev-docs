# CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.Calibration

**Framework**: Core Media  
**Kind**: struct

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Calibration
```

## Topics

### Initializers
- [init(algorithmKind: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.AlgorithmKind, identifier: Int32, domain: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.LensDomain, role: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.LensRole, distortionCoefficients: SIMD4<Float>, xFrameAdjustmentsPolynomial: SIMD3<Float>, yFrameAdjustmentsPolynomial: SIMD3<Float>, radialAngleLimit: Float, intrinsicMatrix: simd_float3x3, intrinsicMatrixProjectionOffset: Float, intrinsicMatrixReferenceDimensions: CGSize, extrinsicOriginSource: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.ExtrinsicOriginSource, extrinsicOrientationQuaternion: SIMD3<Float>)](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/init(algorithmkind:identifier:domain:role:distortioncoefficients:xframeadjustmentspolynomial:yframeadjustmentspolynomial:radialanglelimit:intrinsicmatrix:intrinsicmatrixprojectionoffset:intrinsicmatrixreferencedimensions:extrinsicoriginsour-4ejrv.md)
### Instance Properties
- [var algorithmKind: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.AlgorithmKind](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/algorithmkind.md)
  The camera calibration methodology.
- [var distortionCoefficients: SIMD4<Float>](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/distortioncoefficients.md)
  The first and second radial distortion coefficients (k1 and k2) used to correct the distortion that appeared as curved lines for straight lines and the first and second tangential distortion coefficients (p1 and p2) used to correct the distortion caused by a lens’s improper alignment of physical elements.
- [var domain: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.LensDomain](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/domain.md)
  Specifies the kind of lens (e.g., color).
- [var extrinsicOrientationQuaternion: SIMD3<Float>](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/extrinsicorientationquaternion.md)
  Camera’s orientation to a world or scene coordinate system. The orientation value is a unit quaternion (ix, iy, and iz) instead of the classical 3x3 matrix.
- [var extrinsicOriginSource: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.ExtrinsicOriginSource](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/extrinsicoriginsource.md)
  Identifies how the origin of the camera system’s extrinsics are determined.
- [var identifier: Int32](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/identifier.md)
  Unique number associated with a lens.
- [var intrinsicMatrix: simd_float3x3](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/intrinsicmatrix.md)
  The 3x3 camera intrinsic matrix for camera calibration.
- [var intrinsicMatrixProjectionOffset: Float](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/intrinsicmatrixprojectionoffset.md)
  Offset of the point of perspective relative to the rectilinear projection.
- [var intrinsicMatrixReferenceDimensions: CGSize](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/intrinsicmatrixreferencedimensions.md)
  Image dimensions to which the camera’s intrinsic matrix values are relative.
- [var radialAngleLimit: Float](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/radialanglelimit.md)
  Outer limit of the calibration validity in degrees of angle eccentric from the optical axis.
- [var role: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.LensRole](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/role.md)
  Specifies the particular use of the lens in the camera system (e.g., left or right for a stereo system).
- [var xFrameAdjustmentsPolynomial: SIMD3<Float>](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/xframeadjustmentspolynomial.md)
  Three element polynomial for mapping x axis UV parameters with an adjustment using the equation `x' = polynomialX[0] + polynomialX[1]*x + polynomialX[2]*x^3`.
- [var yFrameAdjustmentsPolynomial: SIMD3<Float>](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/yframeadjustmentspolynomial.md)
  Three element polynomial for mapping y axis UV parameters with an adjustment using the equation `y' = polynomialY[0] + polynomialY[1]*y + polynomialY[2]*y^3`.

## Relationships

### Conforms To
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration)*