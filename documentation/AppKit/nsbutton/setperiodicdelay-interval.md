# setPeriodicDelay(_:interval:)

**Framework**: AppKit  
**Kind**: method

Sets the message delay and interval periods for a continuous button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setPeriodicDelay(_ delay: Float, interval: Float)
```

#### Discussion

The delay and interval values are used if the button is configured (by a [`isContinuous`](nscontrol/iscontinuous.md) message) to continuously send the action message to the target object while tracking the mouse.

## Parameters

- `delay`: The amount of time (in seconds) that a continuous button will pause before starting to periodically send action messages to the target object. The maximum allowed value is 60.0 seconds; if a larger value is supplied, it is ignored, and 60.0 seconds is used.
- `interval`: The amount of time (in seconds) the continuous button will pause between sending each action message. The maximum value is 60.0 seconds; if a larger value is supplied, it is ignored, and 60.0 seconds is used.

## See Also

- [var isContinuous: Bool](nscontrol/iscontinuous.md)
  A Boolean value indicating whether the receiver’s cell sends its action message continuously to its target during mouse tracking.
- [func setButtonType(NSButton.ButtonType)](nsbutton/setbuttontype(_:).md)
  Sets the button’s type, which affects its user interface and behavior when clicked.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](nsbutton/getperiodicdelay(_:interval:).md)
  Returns by reference the delay and interval periods for a continuous button.
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
- [var maxAcceleratorLevel: Int](nsbutton/maxacceleratorlevel.md)
  An integer value indicating the maximum pressure level for a button of type [`NSMultiLevelAcceleratorButton`](nsmultilevelacceleratorbutton.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/setperiodicdelay(_:interval:))*