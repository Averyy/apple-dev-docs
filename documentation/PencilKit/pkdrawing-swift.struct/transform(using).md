# transform(using:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Applies the specified transform to the contents of this drawing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
mutating func transform(using transform: CGAffineTransform)
```

## Parameters

- `transform`: The [`CGAffineTransform`](../../CoreFoundation/cgaffinetransform.md) to apply when transforming the contents of this drawing.

## See Also

### Modifying the drawing
- [func transformed(using: CGAffineTransform) -> PKDrawing](./transformed%28using%29.md)
  Applies the specified transform and returns a new drawing.
- [func append(PKDrawing)](./append%28_%29.md)
  Appends the contents of the specified drawing object to an existing drawing object that you provide.
- [func appending(PKDrawing) -> PKDrawing](./appending%28_%29.md)
  Returns a new drawing created by appending the current drawing with another drawing you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/transform(using:))*