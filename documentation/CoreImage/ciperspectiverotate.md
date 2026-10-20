# CIPerspectiveRotate

**Framework**: Core Image  
**Kind**: protocol  
**Role**: Protocol

The properties you use to configure a perspective rotate filter.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol CIPerspectiveRotate : CIFilterProtocol
```

```objc
@protocol CIPerspectiveRotate <CIFilter>
```

## Topics

### Instance Properties
- [var focalLength: Float](./ciperspectiverotate/focallength.md)
  The 35mm equivalent focal length of the input image.
- [var inputImage: CIImage?](./ciperspectiverotate/inputimage.md)
  The image to process.
- [var pitch: Float](./ciperspectiverotate/pitch.md)
  The pitch angle, in radians.
- [var roll: Float](./ciperspectiverotate/roll.md)
  The roll angle, in radians.
- [var yaw: Float](./ciperspectiverotate/yaw.md)
  The yaw angle, in radians.

## Relationships

### Inherits From
- [CIFilterProtocol](./cifilterprotocol.md)

## See Also

### Related Documentation
- [class func perspectiveRotate() -> any CIFilter & CIPerspectiveRotate](./cifilter-swift.class/perspectiverotate%28%29.md)
  Rotates an image in a 3D space.
### Protocols
- [protocol CIBicubicScaleTransform](./cibicubicscaletransform.md)
  The properties you use to configure a bicubic scale transform filter.
- [protocol CIEdgePreserveUpsample](./ciedgepreserveupsample.md)
  The properties you use to configure an edge preserve upsample filter.
- [protocol CIFourCoordinateGeometryFilter](./cifourcoordinategeometryfilter.md)
  The properties you use to configure a geometry adjustment filters that requires four coordinates.
- [protocol CIKeystoneCorrectionCombined](./cikeystonecorrectioncombined.md)
  The properties you use to configure a keystone correction combined filter.
- [protocol CIKeystoneCorrectionHorizontal](./cikeystonecorrectionhorizontal.md)
  The properties you use to configure a keystone correction horizontal filter.
- [protocol CIKeystoneCorrectionVertical](./cikeystonecorrectionvertical.md)
  The properties you use to configure a keystone correction vertical filter.
- [protocol CILanczosScaleTransform](./cilanczosscaletransform.md)
  The properties you use to configure a Lanczos scale transform filter.
- [protocol CIPerspectiveCorrection](./ciperspectivecorrection.md)
  The properties you use to configure a perspective correction filter.
- [protocol CIPerspectiveTransform](./ciperspectivetransform.md)
  The properties you use to configure a perspective transform filter.
- [protocol CIPerspectiveTransformWithExtent](./ciperspectivetransformwithextent.md)
  The properties you use to configure a perspective transform with extent filter.
- [protocol CIStraighten](./cistraighten.md)
  The properties you use to configure a straighten filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciperspectiverotate)*