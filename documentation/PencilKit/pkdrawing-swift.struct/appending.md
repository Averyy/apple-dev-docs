# appending(_:)

**Framework**: PencilKit  
**Kind**: method

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

- [func transform(using: CGAffineTransform)](pkdrawing-swift.struct/transform(using:).md)
  Applies the specified transform to the contents of this drawing.
- [func transformed(using: CGAffineTransform) -> PKDrawing](pkdrawing-swift.struct/transformed(using:).md)
  Applies the specified transform and returns a new drawing.
- [func append(PKDrawing)](pkdrawing-swift.struct/append(_:).md)
  Appends the contents of the specified drawing object to an existing drawing object that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/appending(_:))*