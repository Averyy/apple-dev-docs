# currentControlTint

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The current system control tint color.

**Availability**:
- macOS

## Declaration

```swift
class var currentControlTint: NSControlTint { get }
```

```objc
@property (class, readonly) NSControlTint currentControlTint;
```

## Return Value

The current system control tint.

## Discussion

An application can register for the [`currentControlTintDidChangeNotification`](./currentcontroltintdidchangenotification.md) notification to be notified of changes to the system control tint.

## See Also

### Related Documentation
- [init(for: NSControlTint)](./init%28for%29.md)
  Returns the color object specified by the given control tint.
### Control colors
- [class var controlAccentColor: NSColor](./controlaccentcolor.md)
  The user’s current accent color preference.
- [class var controlColor: NSColor](./controlcolor.md)
  The color to use for the flat surfaces of a control.
- [class var controlBackgroundColor: NSColor](./controlbackgroundcolor.md)
  The color to use for the background of large controls, such as scroll views or table views.
- [class var controlTextColor: NSColor](./controltextcolor.md)
  The color to use for text on enabled controls.
- [class var disabledControlTextColor: NSColor](./disabledcontroltextcolor.md)
  The color to use for text on disabled controls.
- [class var selectedControlColor: NSColor](./selectedcontrolcolor.md)
  The color to use for the face of a selected control—that is, a control that has been clicked or is being dragged.
- [class var selectedControlTextColor: NSColor](./selectedcontroltextcolor.md)
  The color to use for text in a selected control—that is, a control being clicked or dragged.
- [class var alternateSelectedControlTextColor: NSColor](./alternateselectedcontroltextcolor.md)
  The color to use for text in a selected control.
- [class var scrubberTexturedBackground: NSColor](./scrubbertexturedbackground.md)
  The patterned color to use for the background of a scrubber control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/currentcontroltint)*