# draw(_:in:)

**Framework**: Core Graphics  
**Kind**: method

Draws the contents of a layer object into the specified rectangle.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst ?+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func draw(_ layer: CGLayer, in rect: CGRect)
```

#### Discussion

The contents are scaled, if necessary, to fit into the rectangle.

## Parameters

- `layer`: The layer whose contents you want to draw.
- `rect`: The rectangle, in current user space coordinates, to draw in.

## See Also

- [func draw(CGLayer, at: CGPoint)](cgcontext/draw(_:at:).md)
  Draws the contents of a layer object at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/draw(_:in:))*