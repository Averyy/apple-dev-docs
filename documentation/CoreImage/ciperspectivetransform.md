# CIPerspectiveTransform

**Framework**: Core Image  
**Kind**: protocol  
**Role**: Protocol

The properties you use to configure a perspective transform filter.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol CIPerspectiveTransform : CIFourCoordinateGeometryFilter
```

```objc
@protocol CIPerspectiveTransform <CIFourCoordinateGeometryFilter>
```

## Relationships

### Inherits From
- [CIFilterProtocol](./cifilterprotocol.md)
- [CIFourCoordinateGeometryFilter](./cifourcoordinategeometryfilter.md)

## See Also

### Related Documentation
- [class func perspectiveTransform() -> any CIFilter & CIPerspectiveTransform](./cifilter-swift.class/perspectivetransform%28%29.md)
  Alters an image’s geometry to adjust the perspective.
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
- [protocol CIPerspectiveTransformWithExtent](./ciperspectivetransformwithextent.md)
  The properties you use to configure a perspective transform with extent filter.
- [protocol CIStraighten](./cistraighten.md)
  The properties you use to configure a straighten filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciperspectivetransform)*