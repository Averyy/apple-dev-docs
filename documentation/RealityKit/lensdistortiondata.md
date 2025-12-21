# LensDistortionData

**Framework**: RealityKit  
**Kind**: struct

A description of estimated lens distortion that can be used to rectify images.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
struct LensDistortionData
```

#### Overview

See also: `AVCameraCalibrationData`

Example of a per-pixel undistort function using this data:

```None
func undistortPoint(lensDistortionData: LensDistortionData,
                    imageSize: SIMD2<Float>,
                    point: SIMD2<Float>) -> SIMD2<Float> {
   // The lookup table holds the relative radial magnification for n linearly spaced radii.
   // The first position corresponds to radius = 0
   // The last position corresponds to the largest radius found in the image.

   // Determine the maximum radius.
   let opticalCenter: SIMD2<Float> = lensDistortionData.center
   let deltaXMax: Float = max(opticalCenter.x, imageSize.x  - opticalCenter.x)
   let deltaYMax: Float = max(opticalCenter.y, imageSize.y - opticalCenter.y)
   let radiusMax: Float = sqrt(deltaXMax * deltaXMax + deltaYMax * deltaYMax)

   // Determine the vector from the optical center to the given point.
   let centerToPoint: SIMD2<Float> = point - opticalCenter

   // Determine the radius of the given point.
   let pointRadius: Float = length(centerToPoint)

   // Look up the relative radial magnification to apply in the provided lookup table
   var magnification: Float = 1.0
   let radialLut = lensDistortionData.radialLookupTable
   if pointRadius < radiusMax {
       // Linear interpolation based on piecewise linear function of normalized radius
       let value = pointRadius * Float(radialLut.count - 1) / radiusMax
       let index = Int(value)
       let fraction  = value - Float(index)

       let magLeft = radialLut[index]
       let magRight = radialLut[index + 1]

       magnification = ( 1.0 - fraction ) * magLeft + fraction * magRight
   } else {
       magnification = radialLut[radialLut.count - 1]
   }

   // Apply radial magnification
   let centerToRectifiedPoint: SIMD2<Float> = centerToPoint + magnification * centerToPoint

   // Construct output
   return opticalCenter + centerToRectifiedPoint
 }
```

## Topics

### Initializers
- [init(center: SIMD2<Float>, radialLookupTable: [Float])](lensdistortiondata/init(center:radiallookuptable:).md)
  Initializes a new immutable data structure describing lens distortion estimation.
### Instance Properties
- [let center: SIMD2<Float>](lensdistortiondata/center.md)
  The center pixel of the radial distortion mapping.
- [let radialLookupTable: [Float]](lensdistortiondata/radiallookuptable.md)
  A linear interpolation lookup table from the `center` to the maximum distance corner of the image.  This describes the magnification of radius at a given radius. This is the same structure as `lensDistortionLookupTable` in `AVCameraCalibrationData` and can be used in a similar manner, with the data already converted into a float array.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct HoverEffectComponent](hovereffectcomponent.md)
  A component that applies a visual effect to a hierarchy of entities when a person looks at or selects an entity.
- [struct BillboardComponent](billboardcomponent.md)
  A component that orients an entity instance so that it continuously points toward the active camera.
- [struct EnvironmentBlendingComponent](environmentblendingcomponent.md)
  A component that controls how an entity blends visually with objects in the local environment.
- [struct ImagePresentationComponent](imagepresentationcomponent.md)
  A component that supports general image presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lensdistortiondata)*