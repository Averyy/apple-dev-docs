# interiorBackgroundStyle

**Framework**: AppKit  
**Kind**: property

The cell’s interior background style.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var interiorBackgroundStyle: NSView.BackgroundStyle { get }
```

#### Discussion

The interior background style describes the surface drawn onto in the [`drawInterior(withFrame:in:)`](nscell/drawinterior(withframe:in:).md) method. This is often the same as the [`backgroundStyle`](nscell/backgroundstyle.md), but a button that draws a bezel would use a different value for this property.

In a custom button with a custom bezel you can override this property and return a different value to describe that surface. A cell that has custom interior drawing might use the value of this property to pick an image that looks good on the cell.

## See Also

- [var isBezeled: Bool](nscell/isbezeled.md)
  A Boolean value indicating whether the cell has a bezeled border.
- [var isBordered: Bool](nscell/isbordered.md)
  A Boolean value indicating whether the cell draws itself outlined with a plain border.
- [var isOpaque: Bool](nscell/isopaque.md)
  A Boolean value indicating whether the cell is completely opaque.
- [var controlTint: NSControlTint](nscell/controltint.md)
  The cell’s control tint.
- [var backgroundStyle: NSView.BackgroundStyle](nscell/backgroundstyle.md)
  The cell’s background style.
- [NSView.BackgroundStyle](nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/interiorbackgroundstyle)*