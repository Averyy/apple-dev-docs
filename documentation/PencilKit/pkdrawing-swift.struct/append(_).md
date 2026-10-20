# append(_:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Appends the contents of the specified drawing object to an existing drawing object that you provide.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
mutating func append(_ toAppend: PKDrawing)
```

## Parameters

- `toAppend`: A drawing object that contains additional content.

## See Also

### Modifying the drawing
- [func transform(using: CGAffineTransform)](./transform%28using%29.md)
  Applies the specified transform to the contents of this drawing.
- [func transformed(using: CGAffineTransform) -> PKDrawing](./transformed%28using%29.md)
  Applies the specified transform and returns a new drawing.
- [func appending(PKDrawing) -> PKDrawing](./appending%28_%29.md)
  Returns a new drawing created by appending the current drawing with another drawing you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/append(_:))*