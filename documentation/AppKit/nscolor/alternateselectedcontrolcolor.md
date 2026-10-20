# alternateSelectedControlColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The system color used for the face of a selected control in a list or table.

**Availability**:
- macOS 10.2+ - Deprecated in 11.0

> **Deprecated**: Use [`selectedContentBackgroundColor`](./selectedcontentbackgroundcolor.md) instead.

## Declaration

```swift
class var alternateSelectedControlColor: NSColor { get }
```

```objc
@property (class, strong, readonly) NSColor * alternateSelectedControlColor;
```

#### Return Value

The system color used for the face of a selected control—a control being clicked or dragged. This color is used in lists and tables.

#### Discussion

This color is the table and list view equivalent to the [`selectedControlColor`](./selectedcontrolcolor.md) color, which is used for controls in other views.

For more information, see [`NSColor`](../nscolor.md).

## See Also

### Related Documentation
- [class var alternateSelectedControlTextColor: NSColor](./alternateselectedcontroltextcolor.md)
  The color to use for text in a selected control.
- [Color](https://developer.apple.com/design/human-interface-guidelines/color)
  Judicious use of color can enhance communication, evoke your brand, provide visual continuity, communicate status and feedback, and help people understand information.
- [class var selectedControlColor: NSColor](./selectedcontrolcolor.md)
  The color to use for the face of a selected control—that is, a control that has been clicked or is being dragged.
### Deprecated properties
- [static var quinaryLabel: NSColor](./quinarylabel.md)
- [class var controlAlternatingRowBackgroundColors: [NSColor]](./controlalternatingrowbackgroundcolors.md)
  An array containing the system specified background colors for alternating rows in tables and lists.
- [class var controlHighlightColor: NSColor](./controlhighlightcolor.md)
  The system color used for the highlighted bezels of controls.
- [class var controlLightHighlightColor: NSColor](./controllighthighlightcolor.md)
  The system color used for light highlights in controls.
- [class var controlShadowColor: NSColor](./controlshadowcolor.md)
  The system color used for the shadows dropped from controls.
- [class var controlDarkShadowColor: NSColor](./controldarkshadowcolor.md)
  The system color used for the dark edge of the shadow dropped from controls.
- [class var headerColor: NSColor](./headercolor.md)
  The system color used as the background color for header cells in table views and outline views.
- [class var knobColor: NSColor](./knobcolor.md)
  The system color used for the flat surface of a slider knob that hasn’t been selected.
- [class var selectedKnobColor: NSColor](./selectedknobcolor.md)
  The system color used for the slider knob when it is selected.
- [class var scrollBarColor: NSColor](./scrollbarcolor.md)
  The system color used for scroll “bars”—that is, for the groove in which a scroller’s knob moves
- [class var secondarySelectedControlColor: NSColor](./secondaryselectedcontrolcolor.md)
  The color used for selected controls in non-key views.
- [class var selectedMenuItemColor: NSColor](./selectedmenuitemcolor.md)
  The color to use for the face of selected menu items.
- [class var windowFrameColor: NSColor](./windowframecolor.md)
  The system color used for window frames, except for their text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/alternateselectedcontrolcolor)*