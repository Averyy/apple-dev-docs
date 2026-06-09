# updateDrawing(_:)

**Framework**: PencilKit  
**Kind**: method

Updates the drawing the recognizer analyzes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func updateDrawing(_ drawing: PKDrawing) async
```

## Mentions

- [Recognizing handwriting and converting it to text](recognizing-handwriting-and-converting-to-text.md)

#### Discussion

Recognition expects handwriting and strokes scaled as if written on standard paper sizes in points, such as US-letter or A4.

## Parameters

- `drawing`: The new drawing.

## See Also

- [var drawing: PKDrawing](pkstrokerecognizer/drawing.md)
  The drawing the recognizer analyzes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokerecognizer/updatedrawing(_:))*