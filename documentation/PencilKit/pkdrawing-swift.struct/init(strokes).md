# init(strokes:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates a drawing object and populates it with a sequence of strokes the user provides.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init<S>(strokes: S) where S : Sequence, S.Element == PKStroke
```

## Parameters

- `strokes`: A sequence of [`PKStroke`](../pkstroke-swift.struct.md) elements.

## See Also

### Creating a drawing object
- [init(data: Data) throws](./init%28data%29.md)
  Creates a drawing object and populates it with previously drawn content.
- [init()](./init%28%29.md)
  Creates an empty drawing object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/init(strokes:))*