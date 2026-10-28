# draw(_:in:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Draws resolved text into the context using the specified rectangle as a layout frame.

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
func draw(_ text: GraphicsContext.ResolvedText, in rect: CGRect)
```

**Other overloads**:

```swift
func draw(_ symbol: GraphicsContext.ResolvedSymbol, in rect: CGRect)
```

```swift
func draw(_ text: Text, in rect: CGRect)
```

## Discussion

The current context state defines the full drawing operation. For example, the current transformation and clip shapes affect how SwiftUI draws the text.

## Parameters

- `text`: The [`GraphicsContext.ResolvedText`](./resolvedtext.md) to draw. Get resolved text from a [`Text`](../text.md) view by calling [`resolve(_:)`](./resolve%28_%29-4dx65.md). Alternatively, you can call [`draw(_:in:)`](./draw%28_,in%29-5opqf.md) with a [`Text`](../text.md) view, and that method performs the resolution automatically.
- `rect`: The rectangle in the current user space to draw the text in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/draw(_:in:)-69ad8)*