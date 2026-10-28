# contrast(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Returns a filter that applies a contrast adjustment.

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
static func contrast(_ amount: Double) -> GraphicsContext.Filter
```

## Return Value

A filter that applies a contrast adjustment.

## Discussion

This filter is equivalent to the `contrast` filter primitive defined by the Scalable Vector Graphics (SVG) specification.

## Parameters

- `amount`: An amount to adjust the contrast. A value of zero leaves the result completely gray. A value of one leaves the result unchanged. You can use values greater than one.

## See Also

### Changing brightness and contrast
- [static func brightness(Double) -> GraphicsContext.Filter](./brightness%28_%29.md)
  Returns a filter that applies a brightness adjustment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter/contrast(_:))*