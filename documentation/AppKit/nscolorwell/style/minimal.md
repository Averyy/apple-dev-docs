# NSColorWell.Style.minimal

**Framework**: AppKit  
**Kind**: case

A style that adds minimal adornments to the color well.

**Availability**:
- macOS 13.0+

## Declaration

```swift
case minimal
```

#### Discussion

This style displays a rectangular area with the selected color. Clicks in the color area display a popover with a color picker. If you specified a custom action using the [`pulldownAction`](nscolorwell/pulldownaction.md) and [`pulldownTarget`](nscolorwell/pulldowntarget.md) properties, clicks in the color area execute your action method instead.

## See Also

- [NSColorWell.Style.default](nscolorwell/style/default.md)
  The default style for color wells.
- [NSColorWell.Style.expanded](nscolorwell/style/expanded.md)
  A style that supports a color picker popover for fast interactions, and adds a dedicated button to display the color panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/style/minimal)*