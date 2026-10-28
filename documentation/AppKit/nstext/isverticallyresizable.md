# isVerticallyResizable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that controls whether the receiver changes its height to fit the height of its text.

**Availability**:
- macOS

## Declaration

```swift
var isVerticallyResizable: Bool { get set }
```

```objc
@property (getter=isVerticallyResizable) BOOL verticallyResizable;
```

## Discussion

If `flag` is [`true`](../../Swift/true.md) it does; if `flag` is [`false`](../../Swift/false.md) it doesn’t.

## See Also

### Constraining size
- [var maxSize: NSSize](./maxsize.md)
  The receiver’s maximum size.
- [var minSize: NSSize](./minsize.md)
  The receiver’s minimum size.
- [var isHorizontallyResizable: Bool](./ishorizontallyresizable.md)
  A Boolean that controls whether the receiver changes its width to fit the width of its text.
- [func sizeToFit()](./sizetofit%28%29.md)
  Resizes the receiver to fit its text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/isverticallyresizable)*