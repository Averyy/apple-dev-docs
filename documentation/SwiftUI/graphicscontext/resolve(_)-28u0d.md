# resolve(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a version of a shading resolved with the current values of the graphics context’s environment.

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
func resolve(_ shading: GraphicsContext.Shading) -> GraphicsContext.Shading
```

**Other overloads**:

```swift
func resolve(_ image: Image) -> GraphicsContext.ResolvedImage
```

```swift
func resolve(_ text: Text) -> GraphicsContext.ResolvedText
```

## Discussion

Calling this function once and then drawing multiple times with the result will often have less overhead than drawing with the original shading multiple times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/resolve(_:)-28u0d)*