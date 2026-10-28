# draw(_:in:style:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Draws an image into the context, using the specified rectangle as a layout frame.

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
func draw(_ image: Image, in rect: CGRect, style: FillStyle = FillStyle())
```

**Other overloads**:

```swift
func draw(_ image: GraphicsContext.ResolvedImage, in rect: CGRect, style: FillStyle = FillStyle())
```

## Discussion

The current context state defines the full drawing operation. For example, the current transformation and clip shapes affect how SwiftUI draws the image.

## Parameters

- `image`: The [`Image`](../image.md) to draw. Before drawing, the method converts the image to a [`GraphicsContext.ResolvedImage`](./resolvedimage.md) by calling [`resolve(_:)`](./resolve%28_%29-898z6.md).
- `rect`: The rectangle in the current user space to draw the image in.
- `style`: A fill style to use when rasterizing the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/draw(_:in:style:)-blhz)*