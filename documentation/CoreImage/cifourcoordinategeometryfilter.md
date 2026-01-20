# CIFourCoordinateGeometryFilter

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a geometry adjustment filters that requires four coordinates.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIFourCoordinateGeometryFilter : CIFilterProtocol
```

## Topics

### Instance Properties
- [var bottomLeft: CGPoint](cifourcoordinategeometryfilter/bottomleft.md)
- [var bottomRight: CGPoint](cifourcoordinategeometryfilter/bottomright.md)
- [var inputImage: CIImage?](cifourcoordinategeometryfilter/inputimage.md)
  The image to use as an input image.
- [var topLeft: CGPoint](cifourcoordinategeometryfilter/topleft.md)
- [var topRight: CGPoint](cifourcoordinategeometryfilter/topright.md)

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)
### Inherited By
- [CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md)
- [CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md)
- [CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md)
- [CIPerspectiveCorrection](ciperspectivecorrection.md)
- [CIPerspectiveTransform](ciperspectivetransform.md)
- [CIPerspectiveTransformWithExtent](ciperspectivetransformwithextent.md)

## See Also

- [protocol CIBicubicScaleTransform](cibicubicscaletransform.md)
  The properties you use to configure a bicubic scale transform filter.
- [protocol CIEdgePreserveUpsample](ciedgepreserveupsample.md)
  The properties you use to configure an edge preserve upsample filter.
- [protocol CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md)
  The properties you use to configure a keystone correction combined filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifourcoordinategeometryfilter)*