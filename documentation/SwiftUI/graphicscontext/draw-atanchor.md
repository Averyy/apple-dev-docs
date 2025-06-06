# draw(_:at:anchor:)

**Framework**: SwiftUI  
**Kind**: method

Draws a resolved image into the context, aligning an anchor within the image to a point in the context.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func draw(_ image: GraphicsContext.ResolvedImage, at point: CGPoint, anchor: UnitPoint = .center)
```

#### Discussion

The current context state defines the full drawing operation. For example, the current transformation and clip shapes affect how SwiftUI draws the image.

## Parameters

- `image`: The   to draw. Get a resolved image from an    by calling  . Alternatively, you can   call   with an  , and that method   performs the resolution automatically.
- `point`: A point within the rectangle of the resolved image to anchor   to a point in the context.
- `anchor`: A   within the context to align the image with.   The default is  .

## See Also

- [func draw(_:in:)](graphicscontext/draw(_:in:).md)
  Draws a resolved symbol into the context, using the specified rectangle as a layout frame.
- [func draw(_:in:style:)](graphicscontext/draw(_:in:style:).md)
  Draws a resolved image into the context, using the specified rectangle as a layout frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/draw(_:at:anchor:))*