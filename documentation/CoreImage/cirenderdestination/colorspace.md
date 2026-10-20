# colorSpace

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The destination’s color space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var colorSpace: CGColorSpace? { get set }
```

```objc
@property (nonatomic, nullable) CGColorSpaceRef colorSpace;
```

## See Also

### Customizing Rendering
- [var alphaMode: CIRenderDestinationAlphaMode](./alphamode.md)
  The render destination’s representation of alpha (transparency) values.
- [enum CIRenderDestinationAlphaMode](../cirenderdestinationalphamode.md)
  Different ways of representing alpha.
- [var blendKernel: CIBlendKernel?](./blendkernel.md)
  The destination’s blend kernel.
- [var blendsInDestinationColorSpace: Bool](./blendsindestinationcolorspace.md)
  Indicator of whether to blend in the destination’s color space.
- [var width: Int](./width.md)
  The render destination’s row width.
- [var height: Int](./height.md)
  The render destination’s buffer height.
- [var isClamped: Bool](./isclamped.md)
  Indicator of whether or not the destination clamps.
- [var isDithered: Bool](./isdithered.md)
  Indicator of whether or not the destination dithers.
- [var isFlipped: Bool](./isflipped.md)
  Indicator of whether the destination is flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination/colorspace)*