# fill(with:alpha:)

**Framework**: UIKit  
**Kind**: method

Uses the specified blend mode and transparency values to paint the region that the path encloses.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func fill(with blendMode: CGBlendMode, alpha: CGFloat)
```

#### Discussion

This method fills the path using the current fill color and drawing properties (plus the specified blend mode and transparency value). If the path contains any open subpaths, this method implicitly closes them before painting the fill region.

The painted region includes the pixels right up to, but not including, the path line itself. For paths with large line widths, this can result in overlap between the fill region and the stroked path (which is itself centered on the path line).

This method automatically saves the current graphics state prior to drawing and restores that state when it is done, so you do not have to save the graphics state yourself.

## Parameters

- `blendMode`: The blend mode determines how the filled path is composited with any existing rendered content.
- `alpha`: The amount of transparency to apply to the filled path. Values can range between   (transparent) and   (opaque). Values outside this range are clamped to   or  .

## See Also

- [func fill()](uibezierpath/fill.md)
  Uses the current drawing properties to paint the region that the path encloses.
- [func stroke()](uibezierpath/stroke.md)
  Draws a line along the path using the current drawing properties.
- [func stroke(with: CGBlendMode, alpha: CGFloat)](uibezierpath/stroke(with:alpha:).md)
  Draws a line along the path using the specified blend mode and transparency values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/fill(with:alpha:))*