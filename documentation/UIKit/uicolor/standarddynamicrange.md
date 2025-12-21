# standardDynamicRange

**Framework**: UIKit  
**Kind**: property

In some cases it is useful to recover the color that was base SDR color that was exposed to generate the given HDR color. If a color’s `linearExposure` is >1, then this will return the base SDR color.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@NSCopying
var standardDynamicRange: UIColor { get }
```

## See Also

- [func applyingContentHeadroom(CGFloat) -> UIColor](uicolor/applyingcontentheadroom(_:).md)
  Reinterpret the color by applying a new `contentHeadroom` without changing the color components. Changing the `contentHeadroom` redefines the color relative to a different peak white, changing its behavior under tone mapping and the result of calling `standardDynamicRangeColor`. The new color will have a `contentHeadroom` >= 1.0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/standarddynamicrange)*