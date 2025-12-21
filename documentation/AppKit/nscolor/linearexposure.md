# linearExposure

**Framework**: AppKit  
**Kind**: property

For HDR colors, the linear brightness multiplier that was applied when generating the color. Colors created with an exposure by NSColor create CGColors that are tagged with a contentHeadroom value. While CGColors created without a contentHeadroom tag will return 0 from CGColorGetHeadroom, NSColors generated in a similar fashion return a linearExposure of 1.0.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var linearExposure: CGFloat { get }
```

## See Also

- [var standardDynamicRange: NSColor](nscolor/standarddynamicrange.md)
  In some cases it is useful to recover the color that was base the SDR color that was exposed to generate an HDR color. If a color’s `linearExposure` is > 1, then this will return the base SDR color. If the color is not an HDR color, this will return `self`.
- [func applyingContentHeadroom(CGFloat) -> NSColor](nscolor/applyingcontentheadroom(_:).md)
  Reinterpret the color by applying a new `contentHeadroom` without changing the color components. Changing the `contentHeadroom` redefines the color relative to a different peak white, changing its behavior under tone mapping and the result of calling `standardDynamicRangeColor`. The new color will have a `contentHeadroom` >= 1.0. If called on a color with a color space that does not support extended range, or does not have an equivalent extended range counterpart, this will return `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/linearexposure)*