# knobColor

**Framework**: AppKit  
**Kind**: property

The system color used for the flat surface of a slider knob that hasn’t been selected.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class var knobColor: NSColor { get }
```

#### Return Value

The system color used for an unselected slider knob.

#### Discussion

The knob’s beveled edges, which set it in relief, are drawn in highlighted and shadowed versions of the face color. When a knob is selected, its color changes to [`selectedKnobColor`](nscolor/selectedknobcolor.md). For general information about system colors, see [`Accessing System Colors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/Tasks/SystemColors.html#//apple_ref/doc/uid/20000790).

## See Also

- [class var alternateSelectedControlColor: NSColor](nscolor/alternateselectedcontrolcolor.md)
  The system color used for the face of a selected control in a list or table.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/knobcolor)*