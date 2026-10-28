# draw(_:at:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
func draw(_ image: Image, at point: CGPoint, anchor: UnitPoint = .center)
```

```swift
func draw(_ symbol: GraphicsContext.ResolvedSymbol, at point: CGPoint, anchor: UnitPoint = .center)
```

```swift
func draw(_ text: GraphicsContext.ResolvedText, at point: CGPoint, anchor: UnitPoint = .center)
```

```swift
func draw(_ text: Text, at point: CGPoint, anchor: UnitPoint = .center)
```

## Discussion

The current context state defines the full drawing operation. For example, the current transformation and clip shapes affect how SwiftUI draws the image.

## Parameters

- `image`: The [`GraphicsContext.ResolvedImage`](./resolvedimage.md) to draw. Get a resolved image from an [`Image`](../image.md) by calling [`resolve(_:)`](./resolve%28_%29-898z6.md). Alternatively, you can call [`draw(_:at:anchor:)`](./draw%28_,at,anchor%29-7l217.md) with an [`Image`](../image.md), and that method performs the resolution automatically.
- `point`: A point within the rectangle of the resolved image to anchor to a point in the context.
- `anchor`: A [`UnitPoint`](../unitpoint.md) within the context to align the image with. The default is [`center`](../unitpoint/center.md).

## See Also

### Drawing images, text, and views
- [func draw(_:in:)](./draw%28_,in%29.md)
  Draws a resolved symbol into the context, using the specified rectangle as a layout frame.
- [func draw(_:in:style:)](./draw%28_,in,style%29.md)
  Draws a resolved image into the context, using the specified rectangle as a layout frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/draw(_:at:anchor:))*