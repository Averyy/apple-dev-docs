# setHeight(_:at:)

**Framework**: Accessibility  
**Kind**: method

Sets the height of an individual pin on the braille display.

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
func setHeight(_ status: Float, at point: CGPoint)
```

## Parameters

- `status`: A floating-point number between   and   that specifies the height of the   pin. A value of   lowers the pin completely, and a value of   raises the   pin completely.
- `point`: The location of the pin to adjust the height for. The bottom-left of the display   is at  , and the top-right of the display is at  .

## See Also

- [func height(at: CGPoint) -> Float](axbraillemap/height(at:).md)
  Retrieves the height of an individual pin on the braille display.
- [subscript(CGPoint) -> Float](axbraillemap/subscript(_:).md)
  Accesses the height of an individual pin on the braille display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axbraillemap/setheight(_:at:))*