# kCMFormatDescriptionCameraCalibration_IntrinsicMatrix

**Framework**: Core Media  
**Kind**: var

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
let kCMFormatDescriptionCameraCalibration_IntrinsicMatrix: CFString
```

#### Discussion

Specifies the 3x3 camera intrinsic matrix for camera calibration.

Camera intrinsic matrix is a CFData containing a matrix_float3x3, which is column-major. Each element is in IEEE754 native-endian 32-bit floating point. It has the following contents: fx	s	cx 0	fy	cy 0	0	1 fx and fy are the focal length in pixels. For square pixels, they will have the same value. cx and cy are the coordinates of the principal point. The origin is the upper left of the frame. s is an optional skew factor.

## See Also

- [let kCMFormatDescriptionExtension_CameraCalibrationDataLensCollection: CFString](kcmformatdescriptionextension_cameracalibrationdatalenscollection.md)
- [let kCMFormatDescriptionCameraCalibration_ExtrinsicOrientationQuaternion: CFString](kcmformatdescriptioncameracalibration_extrinsicorientationquaternion.md)
- [let kCMFormatDescriptionCameraCalibration_ExtrinsicOriginSource: CFString](kcmformatdescriptioncameracalibration_extrinsicoriginsource.md)
- [let kCMFormatDescriptionCameraCalibration_IntrinsicMatrixProjectionOffset: CFString](kcmformatdescriptioncameracalibration_intrinsicmatrixprojectionoffset.md)
- [let kCMFormatDescriptionCameraCalibration_IntrinsicMatrixReferenceDimensions: CFString](kcmformatdescriptioncameracalibration_intrinsicmatrixreferencedimensions.md)
- [let kCMFormatDescriptionCameraCalibration_LensAlgorithmKind: CFString](kcmformatdescriptioncameracalibration_lensalgorithmkind.md)
- [let kCMFormatDescriptionCameraCalibration_LensDistortions: CFString](kcmformatdescriptioncameracalibration_lensdistortions.md)
- [let kCMFormatDescriptionCameraCalibration_LensDomain: CFString](kcmformatdescriptioncameracalibration_lensdomain.md)
- [let kCMFormatDescriptionCameraCalibration_LensFrameAdjustmentsPolynomialX: CFString](kcmformatdescriptioncameracalibration_lensframeadjustmentspolynomialx.md)
- [let kCMFormatDescriptionCameraCalibration_LensFrameAdjustmentsPolynomialY: CFString](kcmformatdescriptioncameracalibration_lensframeadjustmentspolynomialy.md)
- [let kCMFormatDescriptionCameraCalibration_LensIdentifier: CFString](kcmformatdescriptioncameracalibration_lensidentifier.md)
- [let kCMFormatDescriptionCameraCalibration_LensRole: CFString](kcmformatdescriptioncameracalibration_lensrole.md)
- [let kCMFormatDescriptionCameraCalibration_RadialAngleLimit: CFString](kcmformatdescriptioncameracalibration_radialanglelimit.md)
- [let kCMFormatDescriptionCameraCalibrationExtrinsicOriginSource_StereoCameraSystemBaseline: CFString](kcmformatdescriptioncameracalibrationextrinsicoriginsource_stereocamerasystembaseline.md)
- [let kCMFormatDescriptionCameraCalibrationLensAlgorithmKind_ParametricLens: CFString](kcmformatdescriptioncameracalibrationlensalgorithmkind_parametriclens.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncameracalibration_intrinsicmatrix)*