# subscript(_:)

**Framework**: Accessibility  
**Kind**: subscript

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

Use this subscript to set or get the height of an individual pin. This subscript provides the same capabilities as using [`setHeight(_:at:)`](axbraillemap/setheight(_:at:).md) and [`height(at:)`](axbraillemap/height(at:).md).

## See Also

- [func setHeight(Float, at: CGPoint)](axbraillemap/setheight(_:at:).md)
  Sets the height of an individual pin on the braille display.
- [func height(at: CGPoint) -> Float](axbraillemap/height(at:).md)
  Retrieves the height of an individual pin on the braille display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axbraillemap/subscript(_:))*