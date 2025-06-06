# init(strokes:)

**Framework**: PencilKit  
**Kind**: init

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

- `strokes`: A sequence of   elements.

## See Also

- [init(data: Data) throws](pkdrawing-swift.struct/init(data:).md)
  Creates a drawing object and populates it with previously drawn content.
- [init()](pkdrawing-swift.struct/init.md)
  Creates an empty drawing object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/init(strokes:))*