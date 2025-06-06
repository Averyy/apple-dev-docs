# writeMask

**Framework**: Metal  
**Kind**: property

A bitmask that restricts which color channels are written into the texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var writeMask: MTLColorWriteMask { get set }
```

#### Discussion

The default value of `writeMask` is all ones, [`all`](mtlcolorwritemask/all.md), which allows all color channels to be blended. The `MTLColorWriteMask` values `MTLColorWriteMaskRed`, `MTLColorWriteMaskGreen`, `MTLColorWriteMaskBlue`, and `MTLColorWriteMaskAlpha` limit blending to one color channel, and these values can be bitwise combined. `MTLColorWriteMaskNone` does not allow any color channels to be blended.

## See Also

- [var pixelFormat: MTLPixelFormat](mtlrenderpipelinecolorattachmentdescriptor/pixelformat.md)
  The pixel format of the color attachment’s texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/writemask)*