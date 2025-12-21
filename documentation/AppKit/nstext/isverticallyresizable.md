# isVerticallyResizable

**Framework**: AppKit  
**Kind**: property

A Boolean that controls whether the receiver changes its height to fit the height of its text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isVerticallyResizable: Bool { get set }
```

#### Discussion

If `flag` is [`true`](https://developer.apple.com/documentation/Swift/true) it does; if `flag` is [`false`](https://developer.apple.com/documentation/Swift/false) it doesn’t.

## See Also

- [var maxSize: NSSize](nstext/maxsize.md)
  The receiver’s maximum size.
- [var minSize: NSSize](nstext/minsize.md)
  The receiver’s minimum size.
- [var isHorizontallyResizable: Bool](nstext/ishorizontallyresizable.md)
  A Boolean that controls whether the receiver changes its width to fit the width of its text.
- [func sizeToFit()](nstext/sizetofit.md)
  Resizes the receiver to fit its text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/isverticallyresizable)*