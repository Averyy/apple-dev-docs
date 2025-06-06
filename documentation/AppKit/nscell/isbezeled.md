# isBezeled

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell has a bezeled border.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isBezeled: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the cell has a bezeled border or [`false`](https://developer.apple.com/documentation/swift/false) if it does not. This property is mutually exclusive with the [`isBordered`](nscell/isbordered.md) property—that is, a cell’s border can be plain or bezeled but not both. Changing the value of this property automatically removes any border that has been set, regardless of the value you assign to the property.

## See Also

- [var isBordered: Bool](nscell/isbordered.md)
  A Boolean value indicating whether the cell draws itself outlined with a plain border.
- [var isOpaque: Bool](nscell/isopaque.md)
  A Boolean value indicating whether the cell is completely opaque.
- [var controlTint: NSControlTint](nscell/controltint.md)
  The cell’s control tint.
- [var backgroundStyle: NSView.BackgroundStyle](nscell/backgroundstyle.md)
  The cell’s background style.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](nscell/interiorbackgroundstyle.md)
  The cell’s interior background style.
- [NSView.BackgroundStyle](nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/isbezeled)*