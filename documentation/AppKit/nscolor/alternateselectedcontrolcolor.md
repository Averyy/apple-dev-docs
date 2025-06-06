# alternateSelectedControlColor

**Framework**: AppKit  
**Kind**: property

The system color used for the face of a selected control in a list or table.

**Availability**:
- macOS 10.2+

## Declaration

```swift
class var alternateSelectedControlColor: NSColor { get }
```

#### Return Value

The system color used for the face of a selected control—a control being clicked or dragged. This color is used in lists and tables. For general information about system colors, see [`Accessing System Colors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/Tasks/SystemColors.html#//apple_ref/doc/uid/20000790).

#### Discussion

This color is the table and list view equivalent to the [`selectedControlColor`](nscolor/selectedcontrolcolor.md) color, which is used for controls in other views.

For general information about system colors, see [`Accessing System Colors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/Tasks/SystemColors.html#//apple_ref/doc/uid/20000790).

## See Also

- [class var alternateSelectedControlTextColor: NSColor](nscolor/alternateselectedcontroltextcolor.md)
  The color to use for text in a selected control.
- [Color Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/DrawColor.html#//apple_ref/doc/uid/10000082i)
- [class var selectedControlColor: NSColor](nscolor/selectedcontrolcolor.md)
  The color to use for the face of a selected control—that is, a control that has been clicked or is being dragged.
- [class var controlAlternatingRowBackgroundColors: [NSColor]](nscolor/controlalternatingrowbackgroundcolors.md)
  An array containing the system specified background colors for alternating rows in tables and lists.
- [class var controlHighlightColor: NSColor](nscolor/controlhighlightcolor.md)
  The system color used for the highlighted bezels of controls.
- [class var controlLightHighlightColor: NSColor](nscolor/controllighthighlightcolor.md)
  The system color used for light highlights in controls.
- [class var controlShadowColor: NSColor](nscolor/controlshadowcolor.md)
  The system color used for the shadows dropped from controls.
- [class var controlDarkShadowColor: NSColor](nscolor/controldarkshadowcolor.md)
  The system color used for the dark edge of the shadow dropped from controls.
- [class var headerColor: NSColor](nscolor/headercolor.md)
  The system color used as the background color for header cells in table views and outline views.
- [class var knobColor: NSColor](nscolor/knobcolor.md)
  The system color used for the flat surface of a slider knob that hasn’t been selected.
- [class var selectedKnobColor: NSColor](nscolor/selectedknobcolor.md)
  The system color used for the slider knob when it is selected.
- [class var scrollBarColor: NSColor](nscolor/scrollbarcolor.md)
  The system color used for scroll “bars”—that is, for the groove in which a scroller’s knob moves
- [class var secondarySelectedControlColor: NSColor](nscolor/secondaryselectedcontrolcolor.md)
  The color used for selected controls in non-key views.
- [class var selectedMenuItemColor: NSColor](nscolor/selectedmenuitemcolor.md)
  The color to use for the face of selected menu items.
- [class var windowFrameColor: NSColor](nscolor/windowframecolor.md)
  The system color used for window frames, except for their text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/alternateselectedcontrolcolor)*