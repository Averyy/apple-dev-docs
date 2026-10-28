# interiorBackgroundStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cell’s interior background style.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var interiorBackgroundStyle: NSView.BackgroundStyle { get }
```

```objc
@property (readonly) NSBackgroundStyle interiorBackgroundStyle;
```

## Discussion

The interior background style describes the surface drawn onto in the [`drawInterior(withFrame:in:)`](./drawinterior%28withframe,in%29.md) method. This is often the same as the [`backgroundStyle`](./backgroundstyle.md), but a button that draws a bezel would use a different value for this property.

In a custom button with a custom bezel you can override this property and return a different value to describe that surface. A cell that has custom interior drawing might use the value of this property to pick an image that looks good on the cell.

## See Also

### Managing Display Attributes
- [var isBezeled: Bool](./isbezeled.md)
  A Boolean value indicating whether the cell has a bezeled border.
- [var isBordered: Bool](./isbordered.md)
  A Boolean value indicating whether the cell draws itself outlined with a plain border.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value indicating whether the cell is completely opaque.
- [var backgroundStyle: NSView.BackgroundStyle](./backgroundstyle.md)
  The cell’s background style.
- [NSView.BackgroundStyle](../nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/interiorbackgroundstyle)*