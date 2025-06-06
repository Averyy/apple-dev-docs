# brightness(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a filter that applies a brightness adjustment.

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
static func brightness(_ amount: Double) -> GraphicsContext.Filter
```

#### Return Value

A filter that applies a brightness adjustment.

#### Discussion

This filter is different than `brightness` filter primitive defined by the Scalable Vector Graphics (SVG) specification. You can obtain an effect like that filter using a [`grayscale(_:)`](graphicscontext/filter/grayscale(_:).md) color multiply. However, this filter does match the [`CIColorControls`](https://developer.apple.com/documentation/coreimage/cicolorcontrols) filter’s brightness adjustment.

## Parameters

- `amount`: An amount to add to the pixel’s color components.

## See Also

- [static func contrast(Double) -> GraphicsContext.Filter](graphicscontext/filter/contrast(_:).md)
  Returns a filter that applies a contrast adjustment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter/brightness(_:))*