# appendingStrokes(_:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (PKDrawing *) drawingByAppendingStrokes:(NSArray<PKStroke *> *) strokes;
```

## Return Value

A new drawing created by appending the provided strokes to the current drawing.

## Parameters

- `strokes`: An array of strokes to append to this drawing.

## See Also

### Modifying the drawing
- [func applying(CGAffineTransform) -> PKDrawing](./applying%28_%29.md)
  Returns a new drawing object by applying the specified transform to a copy of the current object’s contents.
- [func appending(PKDrawing) -> PKDrawing](./appending%28_%29.md)
  Returns a new drawing created by appending the current drawing with another drawing you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawingreference/appendingstrokes(_:))*