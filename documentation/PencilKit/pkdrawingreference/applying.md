# applying(_:)

**Framework**: PencilKit  
**Kind**: method

Returns a new drawing object by applying the specified transform to a copy of the current object’s contents.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func applying(_ transform: CGAffineTransform) -> PKDrawing
```

#### Return Value

A new drawing created by applying the specified `transform` to the current object.

## Parameters

- `transform`: The transform to apply to the drawing.

## See Also

- [func appendingStrokes([PKStroke]) -> PKDrawing](pkdrawingreference/appendingstrokes(_:).md)
  Returns a copy of the current drawing with the strokes you provide appended.
- [func appending(PKDrawing) -> PKDrawing](pkdrawingreference/appending(_:).md)
  Returns a new drawing created by appending the current drawing with another drawing you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawingreference/applying(_:))*