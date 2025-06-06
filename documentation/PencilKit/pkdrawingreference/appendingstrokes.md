# appendingStrokes(_:)

**Framework**: PencilKit  
**Kind**: method

Returns a copy of the current drawing with the strokes you provide appended.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func appendingStrokes(_ strokes: [PKStroke]) -> PKDrawing
```

#### Return Value

A new drawing created by appending the provided strokes to the current drawing.

## Parameters

- `strokes`: An array of strokes to append to this drawing.

## See Also

- [func applying(CGAffineTransform) -> PKDrawing](pkdrawingreference/applying(_:).md)
  Returns a new drawing object by applying the specified transform to a copy of the current object’s contents.
- [func appending(PKDrawing) -> PKDrawing](pkdrawingreference/appending(_:).md)
  Returns a new drawing created by appending the current drawing with another drawing you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawingreference/appendingstrokes(_:))*