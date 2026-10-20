# draw(_:in:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Draws a resolved symbol into the context, using the specified rectangle as a layout frame.

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
func draw(_ symbol: GraphicsContext.ResolvedSymbol, in rect: CGRect)
```

**Other overloads**:

```swift
func draw(_ text: GraphicsContext.ResolvedText, in rect: CGRect)
```

```swift
func draw(_ text: Text, in rect: CGRect)
```

#### Discussion

The current context state defines the full drawing operation. For example, the current transformation and clip shapes affect how SwiftUI draws the symbol.

## Parameters

- `symbol`: The [`GraphicsContext.ResolvedSymbol`](./resolvedsymbol.md) to draw. Get a resolved symbol by calling [`resolveSymbol(id:)`](./resolvesymbol%28id%29.md) with the identifier that you use to tag the corresponding child view during [`Canvas`](../canvas.md) initialization.
- `rect`: The rectangle in the current user space to draw the symbol in.

## See Also

### Drawing images, text, and views
- [func draw(_:in:style:)](./draw%28_,in,style%29.md)
  Draws a resolved image into the context, using the specified rectangle as a layout frame.
- [func draw(_:at:anchor:)](./draw%28_,at,anchor%29.md)
  Draws a resolved image into the context, aligning an anchor within the image to a point in the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/draw(_:in:))*