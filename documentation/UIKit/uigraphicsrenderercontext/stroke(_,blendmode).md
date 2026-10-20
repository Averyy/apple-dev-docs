# stroke(_:blendMode:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Paints a rectangular path using the currently selected stroke color and specified blend mode.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func stroke(_ rect: CGRect, blendMode: CGBlendMode)
```

```objc
- (void) strokeRect:(CGRect) rect blendMode:(CGBlendMode) blendMode;
```

#### Discussion

Before calling this method, select the stroke color with the [`setStroke()`](../uicolor/setstroke%28%29.md) method on an instance of [`UIColor`](../uicolor.md).

The blend mode specifies how the new value for a given pixel is calculated, given the existing pixel value and the currently selected fill color. For more information on the blend modes available, see [`CGBlendMode`](../../CoreGraphics/cgblendmode.md).

## Parameters

- `rect`: A rectangle, specified in the Core Graphics coordinate space with values in points.
- `blendMode`: The blend mode applied to the stroke operation.

## See Also

### Drawing content
- [func stroke(CGRect)](./stroke%28_%29.md)
  Paints a rectangular path using the currently selected stroke color.
- [func fill(CGRect, blendMode: CGBlendMode)](./fill%28_,blendmode%29.md)
  Paints a rectangular area with the currently selected fill color using the supplied blend mode.
- [func fill(CGRect)](./fill%28_%29.md)
  Paints a rectangular area with the currently selected fill color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/stroke(_:blendmode:))*