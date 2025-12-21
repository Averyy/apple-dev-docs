# isSpringLoaded

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether spring loading is enabled for the button.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
@MainActor
var isSpringLoaded: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if spring loading is enabled for the button, and [`false`](https://developer.apple.com/documentation/Swift/false) if it is not. The default is [`false`](https://developer.apple.com/documentation/Swift/false).

On pressure-sensitive systems, such as systems with the Force Touch trackpad, spring loading is a feature that allows a user to activate a button by dragging selected items over it and force clicking—pressing harder—without dropping the selected items. The user can then continue dragging the items, possibly to perform additional actions.

A practical example of this feature can be found in the Calendar app. A selected calendar event can be dragged over the Calendars button in the toolbar. Force clicking on the button displays the calendar list without releasing the selected event. The event can then be dropped onto a calendar in the list, which assigns it to that calendar.

If spring loading is enabled on a button and a user drags items over it, the button highlights to indicate that it responds to force clicking. If the user presses harder, additional highlighting occurs to indicate that the button was fully activated.

On systems that don’t support pressure sensitivity, simply hovering over the button for a short period of time is sufficient to activate the button.

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
- [var maxAcceleratorLevel: Int](nsbutton/maxacceleratorlevel.md)
  An integer value indicating the maximum pressure level for a button of type [`NSMultiLevelAcceleratorButton`](nsmultilevelacceleratorbutton.md).
- [var tintProminence: NSTintProminence](nsbutton/tintprominence.md)
  The tint prominence of the button. Use tint prominence to gently suggest a hierarchy when multiple buttons perform similar actions. A button with primary tint prominence suggests the most preferred option, while secondary prominence indicates a reasonable alternative. See [`NSTintProminence`](nstintprominence.md) for a list of possible values.
- [enum NSTintProminence](nstintprominence.md)
  Controls how strongly the tint color applies in a view.
- [var borderShape: NSControl.BorderShape](nsbutton/bordershape.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/isspringloaded)*