# isBezeled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell has a bezeled border.

**Availability**:
- macOS

## Declaration

```swift
var isBezeled: Bool { get set }
```

```objc
@property (getter=isBezeled) BOOL bezeled;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the cell has a bezeled border or [`false`](../../Swift/false.md) if it does not. This property is mutually exclusive with the [`isBordered`](./isbordered.md) property—that is, a cell’s border can be plain or bezeled but not both. Changing the value of this property automatically removes any border that has been set, regardless of the value you assign to the property.

## See Also

### Managing Display Attributes
- [var isBordered: Bool](./isbordered.md)
  A Boolean value indicating whether the cell draws itself outlined with a plain border.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value indicating whether the cell is completely opaque.
- [var backgroundStyle: NSView.BackgroundStyle](./backgroundstyle.md)
  The cell’s background style.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](./interiorbackgroundstyle.md)
  The cell’s interior background style.
- [NSView.BackgroundStyle](../nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/isbezeled)*