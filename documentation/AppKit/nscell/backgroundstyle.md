# backgroundStyle

**Framework**: AppKit  
**Kind**: property

The cell’s background style.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var backgroundStyle: NSView.BackgroundStyle { get set }
```

#### Discussion

The background describes the surface the cell is drawn onto in the [`draw(withFrame:in:)`](nscell/draw(withframe:in:).md) method. A control typically sets the value of this property before it asks the cell to draw. A cell may draw differently based on background characteristics. For example, a table view drawing a cell in a selected row might set the value to [`dark`](nsview/backgroundstyle/dark.md). A text cell might decide to render its text white as a result. A rating-style level indicator might draw its stars white instead of gray.

## See Also

- [var isBezeled: Bool](nscell/isbezeled.md)
  A Boolean value indicating whether the cell has a bezeled border.
- [var isBordered: Bool](nscell/isbordered.md)
  A Boolean value indicating whether the cell draws itself outlined with a plain border.
- [var isOpaque: Bool](nscell/isopaque.md)
  A Boolean value indicating whether the cell is completely opaque.
- [var controlTint: NSControlTint](nscell/controltint.md)
  The cell’s control tint.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](nscell/interiorbackgroundstyle.md)
  The cell’s interior background style.
- [NSView.BackgroundStyle](nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/backgroundstyle)*