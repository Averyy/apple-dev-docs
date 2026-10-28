# resolve(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Gets a version of a text view that’s fixed with the current values of the graphics context’s environment.

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
func resolve(_ text: Text) -> GraphicsContext.ResolvedText
```

**Other overloads**:

```swift
func resolve(_ image: Image) -> GraphicsContext.ResolvedImage
```

```swift
func resolve(_ shading: GraphicsContext.Shading) -> GraphicsContext.Shading
```

## Return Value

A text view that’s resolved into the current context’s environment, taking into account environment values like the display resolution and current color scheme.

## Discussion

You can measure the resolved text by calling its [`measure(in:)`](./resolvedtext/measure%28in%29.md) method. You can draw the resolved text with the context’s [`draw(_:in:)`](./draw%28_,in%29-69ad8.md) or [`draw(_:at:anchor:)`](./draw%28_,at,anchor%29-6xr87.md) method.

## Parameters

- `text`: The [`Text`](../text.md) view to resolve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/resolve(_:)-4dx65)*