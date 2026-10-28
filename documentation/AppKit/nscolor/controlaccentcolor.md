# controlAccentColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The user’s current accent color preference.

**Availability**:
- macOS 10.14+

## Declaration

```swift
class var controlAccentColor: NSColor { get }
```

```objc
@property (class, strong, readonly) NSColor * controlAccentColor;
```

## Discussion

People set the accent color in the Appearance pane of System Settings. Don’t make assumptions about the color space associated with this color.

## See Also

### Control colors
- [class var controlColor: NSColor](./controlcolor.md)
  The color to use for the flat surfaces of a control.
- [class var controlBackgroundColor: NSColor](./controlbackgroundcolor.md)
  The color to use for the background of large controls, such as scroll views or table views.
- [class var controlTextColor: NSColor](./controltextcolor.md)
  The color to use for text on enabled controls.
- [class var disabledControlTextColor: NSColor](./disabledcontroltextcolor.md)
  The color to use for text on disabled controls.
- [class var currentControlTint: NSControlTint](./currentcontroltint.md)
  The current system control tint color.
- [class var selectedControlColor: NSColor](./selectedcontrolcolor.md)
  The color to use for the face of a selected control—that is, a control that has been clicked or is being dragged.
- [class var selectedControlTextColor: NSColor](./selectedcontroltextcolor.md)
  The color to use for text in a selected control—that is, a control being clicked or dragged.
- [class var alternateSelectedControlTextColor: NSColor](./alternateselectedcontroltextcolor.md)
  The color to use for text in a selected control.
- [class var scrubberTexturedBackground: NSColor](./scrubbertexturedbackground.md)
  The patterned color to use for the background of a scrubber control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/controlaccentcolor)*