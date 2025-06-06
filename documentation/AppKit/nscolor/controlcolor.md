# controlColor

**Framework**: AppKit  
**Kind**: property

The color to use for the flat surfaces of a control.

**Availability**:
- macOS ?+

## Declaration

```swift
class var controlColor: NSColor { get }
```

#### Return Value

The system color used for the flat surfaces of a control. By default, the control color is a pattern color that will draw the ruled lines for the window background, which is the same as returned by [`windowBackgroundColor`](nscolor/windowbackgroundcolor.md).

#### Discussion

If you use [`controlColor`](nscolor/controlcolor.md) assuming that it is a solid, you may have an incorrect appearance. You should use [`lightGray`](nscolor/lightgray.md) in its place.

## See Also

- [class var controlAccentColor: NSColor](nscolor/controlaccentcolor.md)
  The user’s current accent color preference.
- [class var controlBackgroundColor: NSColor](nscolor/controlbackgroundcolor.md)
  The color to use for the background of large controls, such as scroll views or table views.
- [class var controlTextColor: NSColor](nscolor/controltextcolor.md)
  The color to use for text on enabled controls.
- [class var disabledControlTextColor: NSColor](nscolor/disabledcontroltextcolor.md)
  The color to use for text on disabled controls.
- [class var currentControlTint: NSControlTint](nscolor/currentcontroltint.md)
  The current system control tint color.
- [class var selectedControlColor: NSColor](nscolor/selectedcontrolcolor.md)
  The color to use for the face of a selected control—that is, a control that has been clicked or is being dragged.
- [class var selectedControlTextColor: NSColor](nscolor/selectedcontroltextcolor.md)
  The color to use for text in a selected control—that is, a control being clicked or dragged.
- [class var alternateSelectedControlTextColor: NSColor](nscolor/alternateselectedcontroltextcolor.md)
  The color to use for text in a selected control.
- [class var scrubberTexturedBackground: NSColor](nscolor/scrubbertexturedbackground.md)
  The patterned color to use for the background of a scrubber control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/controlcolor)*