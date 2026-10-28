# NSColorWell.Style.minimal

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

A style that adds minimal adornments to the color well.

**Availability**:
- macOS 13.0+

## Declaration

```swift
case minimal
```

```c
NSColorWellStyleMinimal
```

## Discussion

This style displays a rectangular area with the selected color. Clicks in the color area display a popover with a color picker. If you specified a custom action using the [`pulldownAction`](../pulldownaction.md) and [`pulldownTarget`](../pulldowntarget.md) properties, clicks in the color area execute your action method instead.

## See Also

### Getting the Style Option
- [NSColorWell.Style.default](./default.md)
  The default style for color wells.
- [NSColorWell.Style.expanded](./expanded.md)
  A style that supports a color picker popover for fast interactions, and adds a dedicated button to display the color panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/style/minimal)*