# maxAcceleratorLevel

**Framework**: AppKit  
**Kind**: property

An integer value indicating the maximum pressure level for a button of type [`NSMultiLevelAcceleratorButton`](nsmultilevelacceleratorbutton.md).

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
@MainActor
var maxAcceleratorLevel: Int { get set }
```

#### Discussion

A multilevel accelerator button is a variation of a standard accelerator button that allows for a configurable number of stepped pressure levels in a system that supports pressure-sensitivity, such as the Force Touch trackpad. As each level is reached, the user receives light tactile feedback, and an action is sent.

You configure the number of pressure levels for a multilevel accelerator button by adjusting the value of [`maxAcceleratorLevel`](nsbutton/maxacceleratorlevel.md). For other types of buttons, this property value defaults to `1`. For multilevel accelerator buttons, this property value defaults to `2`, and may be set to a value between `1` and `5`.

The behavior of a multilevel accelerator button is reliant on a system that supports pressure sensitivity. On a system that doesn’t support pressure sensitivity, a multilevel accelerator button always has a value of `1` when the user clicks it.

## See Also

- [func setButtonType(NSButton.ButtonType)](nsbutton/setbuttontype(_:).md)
  Sets the button’s type, which affects its user interface and behavior when clicked.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](nsbutton/getperiodicdelay(_:interval:).md)
  Returns by reference the delay and interval periods for a continuous button.
- [func setPeriodicDelay(Float, interval: Float)](nsbutton/setperiodicdelay(_:interval:).md)
  Sets the message delay and interval periods for a continuous button.
- [var contentTintColor: NSColor?](nsbutton/contenttintcolor.md)
  A tint color to use for the template image and text content.
- [var hasDestructiveAction: Bool](nsbutton/hasdestructiveaction.md)
  A Boolean value that defines whether a button’s action has a destructive effect.
- [var alternateTitle: String](nsbutton/alternatetitle.md)
  The title that the button displays when the button is in an on state.
- [var attributedTitle: NSAttributedString](nsbutton/attributedtitle.md)
  The title that the button displays in an off state, as an attributed string.
- [var attributedAlternateTitle: NSAttributedString](nsbutton/attributedalternatetitle.md)
  The title that the button displays as an attributed string when the button is in an on state.
- [var title: String](nsbutton/title.md)
  The title displayed on the button when it’s in an off state.
- [var symbolConfiguration: NSImage.SymbolConfiguration?](nsbutton/symbolconfiguration.md)
  The combination of point size, weight, and scale to use when sizing and displaying symbol images.
- [var sound: NSSound?](nsbutton/sound.md)
  The sound that plays when the user clicks the button.
- [var isSpringLoaded: Bool](nsbutton/isspringloaded.md)
  A Boolean value that indicates whether spring loading is enabled for the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/maxacceleratorlevel)*