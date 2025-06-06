# transformed(using:)

**Framework**: PencilKit  
**Kind**: method

Applies the specified transform and returns a new drawing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func transformed(using transform: CGAffineTransform) -> PKDrawing
```

#### Return Value

A new drawing with the provided `transform` applied.

## Parameters

- `transform`: The   to apply to the contents of this drawing.

## See Also

- [func transform(using: CGAffineTransform)](pkdrawing-swift.struct/transform(using:).md)
  Applies the specified transform to the contents of this drawing.
- [func append(PKDrawing)](pkdrawing-swift.struct/append(_:).md)
  Appends the contents of the specified drawing object to an existing drawing object that you provide.
- [func appending(PKDrawing) -> PKDrawing](pkdrawing-swift.struct/appending(_:).md)
  Returns a new drawing created by appending the current drawing with another drawing you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/transformed(using:))*