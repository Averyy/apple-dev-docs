# isOpaque

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell is completely opaque.

**Availability**:
- macOS

## Declaration

```swift
var isOpaque: Bool { get }
```

```objc
@property (readonly, getter=isOpaque) BOOL opaque;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the cell is completely opaque or [`false`](../../Swift/false.md) if it contains some transparency.

## See Also

### Managing Display Attributes
- [var isBezeled: Bool](./isbezeled.md)
  A Boolean value indicating whether the cell has a bezeled border.
- [var isBordered: Bool](./isbordered.md)
  A Boolean value indicating whether the cell draws itself outlined with a plain border.
- [var backgroundStyle: NSView.BackgroundStyle](./backgroundstyle.md)
  The cell’s background style.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](./interiorbackgroundstyle.md)
  The cell’s interior background style.
- [NSView.BackgroundStyle](../nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/isopaque)*