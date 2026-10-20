# isBordered

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell draws itself outlined with a plain border.

**Availability**:
- macOS

## Declaration

```swift
var isBordered: Bool { get set }
```

```objc
@property (getter=isBordered) BOOL bordered;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the cell has a plain border or [`false`](../../Swift/false.md) if it does not. This property is mutually exclusive with the [`isBezeled`](./isbezeled.md) property—that is, a cell’s border can be plain or bezeled but not both. Changing the value of this property automatically removes any bezel that has been set, regardless of the value you assign to the property.

## See Also

### Managing Display Attributes
- [var isBezeled: Bool](./isbezeled.md)
  A Boolean value indicating whether the cell has a bezeled border.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value indicating whether the cell is completely opaque.
- [var backgroundStyle: NSView.BackgroundStyle](./backgroundstyle.md)
  The cell’s background style.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](./interiorbackgroundstyle.md)
  The cell’s interior background style.
- [NSView.BackgroundStyle](../nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/isbordered)*