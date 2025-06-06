# fill(_:blendMode:)

**Framework**: UIKit  
**Kind**: method

Paints a rectangular area with the currently selected fill color using the supplied blend mode.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func fill(_ rect: CGRect, blendMode: CGBlendMode)
```

#### Discussion

Before calling this method, select the fill color with the [`setFill()`](uicolor/setfill().md) method on an instance of [`UIColor`](uicolor.md).

The blend mode specifies how the new value for a given pixel is calculated, given the existing pixel value and the currently selected fill color. For more information on the blend modes available, see [`CGBlendMode`](https://developer.apple.com/documentation/CoreGraphics/CGBlendMode).

For an example of how to use this method, see [`Using blend mode`](uigraphicsimagerenderer#Using-blend-mode.md) in [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md).

## Parameters

- `rect`: A rectangle, specified in the Core Graphics coordinate space with values in points.
- `blendMode`: The blend mode applied to the fill operation.

## See Also

- [func stroke(CGRect)](uigraphicsrenderercontext/stroke(_:).md)
  Paints a rectangular path using the currently selected stroke color.
- [func stroke(CGRect, blendMode: CGBlendMode)](uigraphicsrenderercontext/stroke(_:blendmode:).md)
  Paints a rectangular path using the currently selected stroke color and specified blend mode.
- [func fill(CGRect)](uigraphicsrenderercontext/fill(_:).md)
  Paints a rectangular area with the currently selected fill color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/fill(_:blendmode:))*