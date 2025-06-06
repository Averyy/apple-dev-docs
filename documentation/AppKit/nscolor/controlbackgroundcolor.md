# controlBackgroundColor

**Framework**: AppKit  
**Kind**: property

The color to use for the background of large controls, such as scroll views or table views.

**Availability**:
- macOS ?+

## Declaration

```swift
class var controlBackgroundColor: NSColor { get }
```

#### Return Value

Do not use this color for drawing. Instead, use an [`NSVisualEffectView`](nsvisualeffectview.md) with the appropriate background material.

#### Discussion

When applied to an [`NSBox`](nsbox.md) object, this color supports Desktop Tinting in Dark Mode. With Desktop Tinting, the system modifies this color dynamically by incorporating some of the color from the underlying desktop image. The system does not apply this dynamic tinting effect to other types of views.

## See Also

- [class var controlAccentColor: NSColor](nscolor/controlaccentcolor.md)
  The user’s current accent color preference.
- [class var controlColor: NSColor](nscolor/controlcolor.md)
  The color to use for the flat surfaces of a control.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/controlbackgroundcolor)*