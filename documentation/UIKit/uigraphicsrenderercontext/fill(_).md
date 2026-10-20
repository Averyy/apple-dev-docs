# fill(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Paints a rectangular area with the currently selected fill color.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func fill(_ rect: CGRect)
```

```objc
- (void) fillRect:(CGRect) rect;
```

#### Discussion

Before calling this method, select the fill color with the [`setFill()`](../uicolor/setfill%28%29.md) method on an instance of [`UIColor`](../uicolor.md).

For an example of how to use this method, see [Creating an image with an image renderer](../uigraphicsimagerenderer.md#Creating-an-image-with-an-image-renderer) in [`UIGraphicsImageRenderer`](../uigraphicsimagerenderer.md).

## Parameters

- `rect`: A rectangle, specified in the Core Graphics coordinate space with values in points.

## See Also

### Drawing content
- [func stroke(CGRect)](./stroke%28_%29.md)
  Paints a rectangular path using the currently selected stroke color.
- [func stroke(CGRect, blendMode: CGBlendMode)](./stroke%28_,blendmode%29.md)
  Paints a rectangular path using the currently selected stroke color and specified blend mode.
- [func fill(CGRect, blendMode: CGBlendMode)](./fill%28_,blendmode%29.md)
  Paints a rectangular area with the currently selected fill color using the supplied blend mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/fill(_:))*