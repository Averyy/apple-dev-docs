# controlAccentColor

**Framework**: AppKit  
**Kind**: property

The user’s current accent color preference.

**Availability**:
- macOS 10.14+

## Declaration

```swift
class var controlAccentColor: NSColor { get }
```

#### Discussion

Users set the accent color in the General pane of system preferences. Do not make assumptions about the color space associated with this color.

## See Also

- [class var controlColor: NSColor](nscolor/controlcolor.md)
  The color to use for the flat surfaces of a control.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/controlaccentcolor)*