# palette(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a multilevel shading instance constructed from an array of shading instances.

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
static func palette(_ array: [GraphicsContext.Shading]) -> GraphicsContext.Shading
```

#### Return Value

A shading instance composed from the given instances.

## Parameters

- `array`: An array of shading instances. The array must   contain at least one element.

## See Also

- [static var backdrop: GraphicsContext.Shading](graphicscontext/shading/backdrop.md)
  A shading instance that draws a copy of the current background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shading/palette(_:))*