# height(at:)

**Framework**: Accessibility  
**Kind**: method

Retrieves the height of an individual pin on the braille display.

**Availability**:
- iOS 15.2+
- iPadOS 15.2+
- Mac Catalyst 15.2+
- macOS 12.1+
- tvOS 15.2+
- visionOS 1.0+
- watchOS 8.2+

## Declaration

```swift
func height(at point: CGPoint) -> Float
```

#### Return Value

A floating-point number between `0.0` and `1.0` that specifies the height of the pin. A value of `0.0` indicates that the pin is completely lowered, and a value of `1.0` indicates that the pin is completely raised.

## Parameters

- `point`: The location of the pin to retrieve the height for. The bottom-left of the display   is at  , and the top-right of the display is at  .

## See Also

- [func setHeight(Float, at: CGPoint)](axbraillemap/setheight(_:at:).md)
  Sets the height of an individual pin on the braille display.
- [subscript(CGPoint) -> Float](axbraillemap/subscript(_:).md)
  Accesses the height of an individual pin on the braille display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axbraillemap/height(at:))*