# CIPerspectiveTransformWithExtent

**Framework**: Core Image  
**Kind**: protocol  
**Role**: Protocol

The properties you use to configure a perspective transform with extent filter.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol CIPerspectiveTransformWithExtent : CIFourCoordinateGeometryFilter
```

```objc
@protocol CIPerspectiveTransformWithExtent <CIFourCoordinateGeometryFilter>
```

## Topics

### Instance Properties
- [var extent: CGRect](./ciperspectivetransformwithextent/extent.md)
  A rectangle that defines the extent of the effect.

## Relationships

### Inherits From
- [CIFilterProtocol](./cifilterprotocol.md)
- [CIFourCoordinateGeometryFilter](./cifourcoordinategeometryfilter.md)

## See Also

### Related Documentation
- [class func perspectiveTransformWithExtent() -> any CIFilter & CIPerspectiveTransformWithExtent](./cifilter-swift.class/perspectivetransformwithextent%28%29.md)
  Alters an image’s geometry to adjust the perspective while applying constraints.
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
- [protocol CIPerspectiveRotate](./ciperspectiverotate.md)
  The properties you use to configure a perspective rotate filter.
- [protocol CIPerspectiveTransform](./ciperspectivetransform.md)
  The properties you use to configure a perspective transform filter.
- [protocol CIStraighten](./cistraighten.md)
  The properties you use to configure a straighten filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciperspectivetransformwithextent)*