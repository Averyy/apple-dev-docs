# subscript(_:)

**Framework**: Accessibility  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the height of an individual pin on the braille display.

**Availability**:
- iOS 15.2+
- iPadOS 15.2+
- Mac Catalyst 15.2+
- macOS 12.2+
- tvOS 15.2+
- visionOS 1.0+
- watchOS 8.2+

## Declaration

```swift
subscript(point: CGPoint) -> Float { get set }
```

#### Overview

Use this subscript to set or get the height of an individual pin. This subscript provides the same capabilities as using [`setHeight(_:at:)`](./setheight%28_,at%29.md) and [`height(at:)`](./height%28at%29.md).

## See Also

### Accessing dots
- [func setHeight(Float, at: CGPoint)](./setheight%28_,at%29.md)
  Sets the height of an individual pin on the braille display.
- [func height(at: CGPoint) -> Float](./height%28at%29.md)
  Retrieves the height of an individual pin on the braille display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axbraillemap/subscript(_:))*