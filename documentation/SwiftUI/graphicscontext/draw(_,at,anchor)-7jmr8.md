# draw(_:at:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Draws a resolved symbol into the context, aligning an anchor within the symbol to a point in the context.

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
func draw(_ symbol: GraphicsContext.ResolvedSymbol, at point: CGPoint, anchor: UnitPoint = .center)
```

**Other overloads**:

```swift
func draw(_ image: GraphicsContext.ResolvedImage, at point: CGPoint, anchor: UnitPoint = .center)
```

```swift
func draw(_ image: Image, at point: CGPoint, anchor: UnitPoint = .center)
```

```swift
func draw(_ text: GraphicsContext.ResolvedText, at point: CGPoint, anchor: UnitPoint = .center)
```

```swift
func draw(_ text: Text, at point: CGPoint, anchor: UnitPoint = .center)
```

## Discussion

The current context state defines the full drawing operation. For example, the current transformation and clip shapes affect how SwiftUI draws the symbol.

## Parameters

- `symbol`: The [`GraphicsContext.ResolvedSymbol`](./resolvedsymbol.md) view to draw. Get a resolved symbol by calling [`resolveSymbol(id:)`](./resolvesymbol%28id%29.md) with the identifier that you use to tag the corresponding child view during [`Canvas`](../canvas.md) initialization.
- `point`: A point within the rectangle of the resolved symbol to anchor to a point in the context.
- `anchor`: A [`UnitPoint`](../unitpoint.md) within the context to align the symbol with. The default is [`center`](../unitpoint/center.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/draw(_:at:anchor:)-7jmr8)*