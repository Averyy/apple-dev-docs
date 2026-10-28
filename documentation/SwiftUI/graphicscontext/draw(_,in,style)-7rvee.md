# draw(_:in:style:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
func draw(_ image: Image, in rect: CGRect, style: FillStyle = FillStyle())
```

## Discussion

The current context state defines the full drawing operation. For example, the current transformation and clip shapes affect how SwiftUI draws the image.

## Parameters

- `image`: The [`GraphicsContext.ResolvedImage`](./resolvedimage.md) to draw. Get a resolved image from an [`Image`](../image.md) by calling [`resolve(_:)`](./resolve%28_%29-898z6.md). Alternatively, you can call [`draw(_:in:style:)`](./draw%28_,in,style%29-blhz.md) with an [`Image`](../image.md), and that method performs the resolution automatically.
- `rect`: The rectangle in the current user space to draw the image in.
- `style`: A fill style to use when rasterizing the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/draw(_:in:style:)-7rvee)*