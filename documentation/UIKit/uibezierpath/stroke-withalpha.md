# stroke(with:alpha:)

**Framework**: UIKit  
**Kind**: method

Draws a line along the path using the specified blend mode and transparency values.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func stroke(with blendMode: CGBlendMode, alpha: CGFloat)
```

#### Discussion

The drawn line is centered on the path with its sides parallel to the path segment. This method applies the current stroke color and drawing properties (plus the specified blend mode and transparency value) to the rendered path.

This method automatically saves the current graphics state prior to drawing and restores that state when it is done, so you do not have to save the graphics state yourself.

## Parameters

- `blendMode`: The blend mode determines how the stroked path is composited with any existing rendered content.
- `alpha`: The amount of transparency to apply to the stroked path. Values can range between   (transparent) and   (opaque). Values outside this range are clamped to   or  .

## See Also

- [func fill()](uibezierpath/fill.md)
  Uses the current drawing properties to paint the region that the path encloses.
- [func fill(with: CGBlendMode, alpha: CGFloat)](uibezierpath/fill(with:alpha:).md)
  Uses the specified blend mode and transparency values to paint the region that the path encloses.
- [func stroke()](uibezierpath/stroke.md)
  Draws a line along the path using the current drawing properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/stroke(with:alpha:))*