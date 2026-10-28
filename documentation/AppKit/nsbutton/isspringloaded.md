# isSpringLoaded

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether spring loading is enabled for the button.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
var isSpringLoaded: Bool { get set }
```

```objc
@property (getter=isSpringLoaded) BOOL springLoaded;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if spring loading is enabled for the button, and [`false`](../../Swift/false.md) if it is not. The default is [`false`](../../Swift/false.md).

On pressure-sensitive systems, such as systems with the Force Touch trackpad, spring loading is a feature that allows a user to activate a button by dragging selected items over it and force clicking—pressing harder—without dropping the selected items. The user can then continue dragging the items, possibly to perform additional actions.

A practical example of this feature can be found in the Calendar app. A selected calendar event can be dragged over the Calendars button in the toolbar. Force clicking on the button displays the calendar list without releasing the selected event. The event can then be dropped onto a calendar in the list, which assigns it to that calendar.

If spring loading is enabled on a button and a user drags items over it, the button highlights to indicate that it responds to force clicking. If the user presses harder, additional highlighting occurs to indicate that the button was fully activated.

On systems that don’t support pressure sensitivity, simply hovering over the button for a short period of time is sufficient to activate the button.

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
- [var alternateTitle: String](./alternatetitle.md)
  The title that the button displays when the button is in an on state.
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
- [var maxAcceleratorLevel: Int](./maxacceleratorlevel.md)
  An integer value indicating the maximum pressure level for a button of type [`NSMultiLevelAcceleratorButton`](../nsmultilevelacceleratorbutton.md).
- [var tintProminence: NSTintProminence](./tintprominence.md)
  The tint prominence of the button. Use tint prominence to gently suggest a hierarchy when multiple buttons perform similar actions. A button with primary tint prominence suggests the most preferred option, while secondary prominence indicates a reasonable alternative. See [`NSTintProminence`](../nstintprominence.md) for a list of possible values.
- [enum NSTintProminence](../nstintprominence.md)
  Controls how strongly the tint color applies in a view.
- [var borderShape: NSControl.BorderShape](./bordershape.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/isspringloaded)*