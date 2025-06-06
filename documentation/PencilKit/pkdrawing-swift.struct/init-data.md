# init(data:)

**Framework**: PencilKit  
**Kind**: init

Creates a drawing object and populates it with previously drawn content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(data: Data) throws
```

#### Discussion

This initializer creates a new canvas object initialized with the specified data.

## Parameters

- `data`: The initial data to add to the canvas. Only specify data you previously obtained from a canvas view.

## See Also

- [init<S>(strokes: S)](pkdrawing-swift.struct/init(strokes:).md)
  Creates a drawing object and populates it with a sequence of strokes the user provides.
- [init()](pkdrawing-swift.struct/init.md)
  Creates an empty drawing object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/init(data:))*