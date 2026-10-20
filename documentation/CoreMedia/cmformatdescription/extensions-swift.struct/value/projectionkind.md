# CMFormatDescription.Extensions.Value.ProjectionKind

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

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
struct ProjectionKind
```

## Topics

### Type Properties
- [static let appleImmersiveVideo: CMFormatDescription.Extensions.Value.ProjectionKind](./projectionkind/appleimmersivevideo.md)
  Indicates a proprietary projection used for Apple Immersive Video.
- [static let equirectangular: CMFormatDescription.Extensions.Value.ProjectionKind](./projectionkind/equirectangular.md)
  Indicates equirectangular projection of a 360 degree sphere to a rectangular plane, where longitude and latitude of the sphere are mapped linearly to the x,y axes of the plane.
- [static let halfEquirectangular: CMFormatDescription.Extensions.Value.ProjectionKind](./projectionkind/halfequirectangular.md)
  Indicates half equirectangular projection of a 180 degree hemisphere to a rectangular plane, where longitude and latitude of the sphere are mapped linearly to the x,y axes of the plane
- [static let parametricImmersive: CMFormatDescription.Extensions.Value.ProjectionKind](./projectionkind/parametricimmersive.md)
  Indicates a projection described mathematically by a model of camera lens calibration parameters. Parameters may be found in lens calibration metadata in [`cameraCalibrationDataLensCollection`](../key/cameracalibrationdatalenscollection.md) with algorithmKind being [`CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection.AlgorithmKind.parametric`](./cameracalibrationdatalenscollection/algorithmkind/parametric.md).
- [static let rectilinear: CMFormatDescription.Extensions.Value.ProjectionKind](./projectionkind/rectilinear.md)
  Indicates rectilinear projection. Generally less than 90 degree field of view with no barrel distortion.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [RawRepresentable](../../../../Swift/rawrepresentable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/extensions-swift.struct/value/projectionkind)*