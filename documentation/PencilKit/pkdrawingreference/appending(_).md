# appending(_:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Returns a new drawing created by appending the current drawing with another drawing you provide.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func appending(_ drawing: PKDrawing) -> PKDrawing
```

```objc
- (PKDrawing *) drawingByAppendingDrawing:(PKDrawing *) drawing;
```

#### Return Value

A new drawing created by merging the content from the current object with the content in the `drawing` parameter.

## Parameters

- `drawing`: A drawing object that contains additional content.

## See Also

### Modifying the drawing
- [func applying(CGAffineTransform) -> PKDrawing](./applying%28_%29.md)
  Returns a new drawing object by applying the specified transform to a copy of the current object’s contents.
- [func appendingStrokes([PKStroke]) -> PKDrawing](./appendingstrokes%28_%29.md)
  Returns a copy of the current drawing with the strokes you provide appended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawingreference/appending(_:))*