# alternateTitle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The title that the button displays when the button is in an on state.

**Availability**:
- macOS

## Declaration

```swift
var alternateTitle: String { get set }
```

```objc
@property (copy) NSString * alternateTitle;
```

#### Discussion

This property contains the string that appears on the button when the button is in an on state, or the empty string if the button doesn’t display an alternate title. By default, a button’s alternate title is Button.

## See Also

### Configuring buttons
- [func setButtonType(NSButton.ButtonType)](./setbuttontype%28_%29.md)
  Sets the button’s type, which affects its user interface and behavior when clicked.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](./getperiodicdelay%28_,interval%29.md)
  Returns by reference the delay and interval periods for a continuous button.
- [func setPeriodicDelay(Float, interval: Float)](./setperiodicdelay%28_,interval%29.md)
  Sets the message delay and interval periods for a continuous button.
- [var contentTintColor: NSColor?](./contenttintcolor.md)
  A tint color to use for the template image and text content.
- [var hasDestructiveAction: Bool](./hasdestructiveaction.md)
  A Boolean value that defines whether a button’s action has a destructive effect.
- [var attributedTitle: NSAttributedString](./attributedtitle.md)
  The title that the button displays in an off state, as an attributed string.
- [var attributedAlternateTitle: NSAttributedString](./attributedalternatetitle.md)
  The title that the button displays as an attributed string when the button is in an on state.
- [var title: String](./title.md)
  The title displayed on the button when it’s in an off state.
- [var symbolConfiguration: NSImage.SymbolConfiguration?](./symbolconfiguration.md)
  The combination of point size, weight, and scale to use when sizing and displaying symbol images.
- [var sound: NSSound?](./sound.md)
  The sound that plays when the user clicks the button.
- [var isSpringLoaded: Bool](./isspringloaded.md)
  A Boolean value that indicates whether spring loading is enabled for the button.
- [var maxAcceleratorLevel: Int](./maxacceleratorlevel.md)
  An integer value indicating the maximum pressure level for a button of type [`NSMultiLevelAcceleratorButton`](../nsmultilevelacceleratorbutton.md).
- [var tintProminence: NSTintProminence](./tintprominence.md)
  The tint prominence of the button. Use tint prominence to gently suggest a hierarchy when multiple buttons perform similar actions. A button with primary tint prominence suggests the most preferred option, while secondary prominence indicates a reasonable alternative. See [`NSTintProminence`](../nstintprominence.md) for a list of possible values.
- [enum NSTintProminence](../nstintprominence.md)
  Controls how strongly the tint color applies in a view.
- [var borderShape: NSControl.BorderShape](./bordershape.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/alternatetitle)*