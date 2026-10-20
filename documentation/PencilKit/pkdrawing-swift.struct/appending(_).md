# appending(_:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Returns a new drawing created by appending the current drawing with another drawing you provide.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func appending(_ toAppend: PKDrawing) -> PKDrawing
```

#### Return Value

A new drawing created by merging the content from the current object with the content in the drawing parameter.

## Parameters

- `toAppend`: A drawing object that contains additional content.

## See Also

### Modifying the drawing
- [func transform(using: CGAffineTransform)](./transform%28using%29.md)
  Applies the specified transform to the contents of this drawing.
- [func transformed(using: CGAffineTransform) -> PKDrawing](./transformed%28using%29.md)
  Applies the specified transform and returns a new drawing.
- [func append(PKDrawing)](./append%28_%29.md)
  Appends the contents of the specified drawing object to an existing drawing object that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/appending(_:))*