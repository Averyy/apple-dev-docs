# isOpaque

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell is completely opaque.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isOpaque: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the cell is completely opaque or [`false`](https://developer.apple.com/documentation/swift/false) if it contains some transparency.

## See Also

- [var isBezeled: Bool](nscell/isbezeled.md)
  A Boolean value indicating whether the cell has a bezeled border.
- [var isBordered: Bool](nscell/isbordered.md)
  A Boolean value indicating whether the cell draws itself outlined with a plain border.
- [var controlTint: NSControlTint](nscell/controltint.md)
  The cell’s control tint.
- [var backgroundStyle: NSView.BackgroundStyle](nscell/backgroundstyle.md)
  The cell’s background style.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](nscell/interiorbackgroundstyle.md)
  The cell’s interior background style.
- [NSView.BackgroundStyle](nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/isopaque)*