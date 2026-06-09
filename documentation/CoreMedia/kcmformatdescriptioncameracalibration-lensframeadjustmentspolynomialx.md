# kCMFormatDescriptionCameraCalibration_LensFrameAdjustmentsPolynomialX

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
let kCMFormatDescriptionCameraCalibration_LensFrameAdjustmentsPolynomialX: CFString
```

#### Discussion

Specifies a three element polynomial for mapping x axis UV parameters with an adjustment using the equation `x' = polynomialX[0] + polynomialX[1]*x + polynomialX[2]*x^3`.

The values are in a CFArray of three CFNumbers(float) in the order polynomialX[0], polynomialX[1] & polynomialX[2]. The polynomial transform origin is at the center of the frame. The default values of elements of polynomialX[] are [0.0, 1.0, 0.0].

## See Also

- [let kCMFormatDescriptionExtension_CameraCalibrationDataLensCollection: CFString](kcmformatdescriptionextension_cameracalibrationdatalenscollection.md)
- [let kCMFormatDescriptionCameraCalibration_ExtrinsicOrientationQuaternion: CFString](kcmformatdescriptioncameracalibration_extrinsicorientationquaternion.md)
- [let kCMFormatDescriptionCameraCalibration_ExtrinsicOriginSource: CFString](kcmformatdescriptioncameracalibration_extrinsicoriginsource.md)
- [let kCMFormatDescriptionCameraCalibration_IntrinsicMatrix: CFString](kcmformatdescriptioncameracalibration_intrinsicmatrix.md)
- [let kCMFormatDescriptionCameraCalibration_IntrinsicMatrixProjectionOffset: CFString](kcmformatdescriptioncameracalibration_intrinsicmatrixprojectionoffset.md)
- [let kCMFormatDescriptionCameraCalibration_IntrinsicMatrixReferenceDimensions: CFString](kcmformatdescriptioncameracalibration_intrinsicmatrixreferencedimensions.md)
- [let kCMFormatDescriptionCameraCalibration_LensAlgorithmKind: CFString](kcmformatdescriptioncameracalibration_lensalgorithmkind.md)
- [let kCMFormatDescriptionCameraCalibration_LensDistortions: CFString](kcmformatdescriptioncameracalibration_lensdistortions.md)
- [let kCMFormatDescriptionCameraCalibration_LensDomain: CFString](kcmformatdescriptioncameracalibration_lensdomain.md)
- [let kCMFormatDescriptionCameraCalibration_LensFrameAdjustmentsPolynomialY: CFString](kcmformatdescriptioncameracalibration_lensframeadjustmentspolynomialy.md)
- [let kCMFormatDescriptionCameraCalibration_LensIdentifier: CFString](kcmformatdescriptioncameracalibration_lensidentifier.md)
- [let kCMFormatDescriptionCameraCalibration_LensRole: CFString](kcmformatdescriptioncameracalibration_lensrole.md)
- [let kCMFormatDescriptionCameraCalibration_RadialAngleLimit: CFString](kcmformatdescriptioncameracalibration_radialanglelimit.md)
- [let kCMFormatDescriptionCameraCalibrationExtrinsicOriginSource_StereoCameraSystemBaseline: CFString](kcmformatdescriptioncameracalibrationextrinsicoriginsource_stereocamerasystembaseline.md)
- [let kCMFormatDescriptionCameraCalibrationLensAlgorithmKind_ParametricLens: CFString](kcmformatdescriptioncameracalibrationlensalgorithmkind_parametriclens.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncameracalibration_lensframeadjustmentspolynomialx)*