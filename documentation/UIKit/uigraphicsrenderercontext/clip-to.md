# clip(to:)

**Framework**: UIKit  
**Kind**: method

Sets the clipping mask for the drawing context to the specified rectangle.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func clip(to rect: CGRect)
```

#### Discussion

To restrict the active drawing area to the specified rectangle, call this method before executing drawing commands.

To use a more complex shape as a clipping mask, use the [`clip(to:mask:)`](https://developer.apple.com/documentation/CoreGraphics/CGContext/clip(to:mask:)) method on the underlying Core Graphics context, accessed through the [`cgContext`](uigraphicsrenderercontext/cgcontext.md) property.

## Parameters

- `rect`: The rectangle to which the drawing context is clipped, specified in the Core Graphics coordinate space with values in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/clip(to:))*