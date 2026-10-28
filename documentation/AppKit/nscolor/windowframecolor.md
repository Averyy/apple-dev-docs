# windowFrameColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The system color used for window frames, except for their text.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: Use an [`NSVisualEffectView`](../nsvisualeffectview.md) with the [`NSVisualEffectView.Material.titlebar`](../nsvisualeffectview/material-swift.enum/titlebar.md) material instead.

## Declaration

```swift
class var windowFrameColor: NSColor { get }
```

```objc
@property (class, strong, readonly) NSColor * windowFrameColor;
```

## Return Value

The color used for window frames. For more information, see [`NSColor`](../nscolor.md).

## See Also

### Related Documentation
- [class var windowFrameTextColor: NSColor](./windowframetextcolor.md)
  The color to use for text in a window’s frame.
### Deprecated properties
- [static var quinaryLabel: NSColor](./quinarylabel.md)
- [class var alternateSelectedControlColor: NSColor](./alternateselectedcontrolcolor.md)
  The system color used for the face of a selected control in a list or table.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/windowframecolor)*