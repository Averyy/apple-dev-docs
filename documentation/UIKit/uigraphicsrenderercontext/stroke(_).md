# stroke(_:)

**Framework**: UIKit  
**Kind**: method

Paints a rectangular path using the currently selected stroke color.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func stroke(_ rect: CGRect)
```

#### Discussion

Before calling this method, select the stroke color with the [`setStroke()`](uicolor/setstroke().md) method on an instance of [`UIColor`](uicolor.md).

For an example of how to use this method, see [`Creating an image with an image renderer`](uigraphicsimagerenderer#Creating-an-image-with-an-image-renderer.md) in [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md).

## Parameters

- `rect`: A rectangle, specified in the Core Graphics coordinate space with values in points.

## See Also

- [func stroke(CGRect, blendMode: CGBlendMode)](uigraphicsrenderercontext/stroke(_:blendmode:).md)
  Paints a rectangular path using the currently selected stroke color and specified blend mode.
- [func fill(CGRect, blendMode: CGBlendMode)](uigraphicsrenderercontext/fill(_:blendmode:).md)
  Paints a rectangular area with the currently selected fill color using the supplied blend mode.
- [func fill(CGRect)](uigraphicsrenderercontext/fill(_:).md)
  Paints a rectangular area with the currently selected fill color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/stroke(_:))*