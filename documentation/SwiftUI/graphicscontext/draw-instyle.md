# draw(_:in:style:)

**Framework**: SwiftUI  
**Kind**: method

Draws a resolved image into the context, using the specified rectangle as a layout frame.

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
func draw(_ image: GraphicsContext.ResolvedImage, in rect: CGRect, style: FillStyle = FillStyle())
```

#### Discussion

The current context state defines the full drawing operation. For example, the current transformation and clip shapes affect how SwiftUI draws the image.

## Parameters

- `image`: The   to draw. Get a resolved image from an    by calling  . Alternatively, you can   call   with an  , and that method   performs the resolution automatically.
- `rect`: The rectangle in the current user space to draw the image in.
- `style`: A fill style to use when rasterizing the image.

## See Also

- [func draw(_:in:)](graphicscontext/draw(_:in:).md)
  Draws a resolved symbol into the context, using the specified rectangle as a layout frame.
- [func draw(_:at:anchor:)](graphicscontext/draw(_:at:anchor:).md)
  Draws a resolved image into the context, aligning an anchor within the image to a point in the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/draw(_:in:style:))*