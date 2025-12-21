# applyingContentHeadroom(_:)

**Framework**: UIKit  
**Kind**: method

Reinterpret the color by applying a new `contentHeadroom` without changing the color components. Changing the `contentHeadroom` redefines the color relative to a different peak white, changing its behavior under tone mapping and the result of calling `standardDynamicRangeColor`. The new color will have a `contentHeadroom` >= 1.0.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func applyingContentHeadroom(_ contentHeadroom: CGFloat) -> UIColor
```

## See Also

- [var standardDynamicRange: UIColor](uicolor/standarddynamicrange.md)
  In some cases it is useful to recover the color that was base SDR color that was exposed to generate the given HDR color. If a color’s `linearExposure` is >1, then this will return the base SDR color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/applyingcontentheadroom(_:))*