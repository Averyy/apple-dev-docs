# draw(_:at:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Draws an image into the context, aligning an anchor within the image to a point in the context.

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
func draw(_ image: Image, at point: CGPoint, anchor: UnitPoint = .center)
```

**Other overloads**:

```swift
func draw(_ image: GraphicsContext.ResolvedImage, at point: CGPoint, anchor: UnitPoint = .center)
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

- `image`: The [`Image`](../image.md) to draw. Before drawing, the method converts the image to a [`GraphicsContext.ResolvedImage`](./resolvedimage.md) by calling [`resolve(_:)`](./resolve%28_%29-898z6.md).
- `point`: A point within the rectangle of the resolved image to anchor to a point in the context.
- `anchor`: A [`UnitPoint`](../unitpoint.md) within the context to align the image with. The default is [`center`](../unitpoint/center.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/draw(_:at:anchor:)-7l217)*