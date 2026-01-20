# CIKeystoneCorrectionCombined

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a keystone correction combined filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIKeystoneCorrectionCombined : CIFourCoordinateGeometryFilter
```

## Topics

### Instance Properties
- [var focalLength: Float](cikeystonecorrectioncombined/focallength.md)
  The 35mm equivalent focal length of the input image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)
- [CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md)

## See Also

- [class func keystoneCorrectionCombined() -> any CIFilter & CIKeystoneCorrectionCombined](cifilter-swift.class/keystonecorrectioncombined.md)
  Adjusts the image vertically and horizontally to remove distortion.
- [protocol CIBicubicScaleTransform](cibicubicscaletransform.md)
  The properties you use to configure a bicubic scale transform filter.
- [protocol CIEdgePreserveUpsample](ciedgepreserveupsample.md)
  The properties you use to configure an edge preserve upsample filter.
- [protocol CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md)
  The properties you use to configure a geometry adjustment filters that requires four coordinates.
- [protocol CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md)
  The properties you use to configure a keystone correction horizontal filter.
- [protocol CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md)
  The properties you use to configure a keystone correction vertical filter.
- [protocol CILanczosScaleTransform](cilanczosscaletransform.md)
  The properties you use to configure a Lanczos scale transform filter.
- [protocol CIPerspectiveCorrection](ciperspectivecorrection.md)
  The properties you use to configure a perspective correction filter.
- [protocol CIPerspectiveRotate](ciperspectiverotate.md)
  The properties you use to configure a perspective rotate filter.
- [protocol CIPerspectiveTransform](ciperspectivetransform.md)
  The properties you use to configure a perspective transform filter.
- [protocol CIPerspectiveTransformWithExtent](ciperspectivetransformwithextent.md)
  The properties you use to configure a perspective transform with extent filter.
- [protocol CIStraighten](cistraighten.md)
  The properties you use to configure a straighten filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikeystonecorrectioncombined)*