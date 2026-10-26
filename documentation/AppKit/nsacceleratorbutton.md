# NSAcceleratorButton

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

A button that sends an action when the user first clicks the button and continues sending actions until the user releases pressure entirely.

**Availability**:
- macOS 10.10.3+ - Deprecated in 10.14

> **Deprecated**: Use [`NSButton.ButtonType.accelerator`](./nsbutton/buttontype/accelerator.md) instead.

## Declaration

```c
static const NSButtonType NSAcceleratorButton;
```

#### Discussion

On pressure-sensitive systems, such as systems with the Force Touch trackpad, an accelerator button sends repeating actions as pressure changes occur. It stops sending actions when the user releases pressure entirely. A media player app, for example, might implement an accelerator button in order to allow a user to adjust the speed of fast forward or rewind with variable pressure. In this case, the button sends actions to the app to indicate when the user changes pressure on the button. The app then determines the amount of pressure the user is currently applying and adjusts playback speed accordingly.

For continuous accelerator buttons (see [`isContinuous`](./nscontrol/iscontinuous.md)), the interval between repeating actions (a rate typically specified with [`setPeriodicDelay(_:interval:)`](./nsbutton/setperiodicdelay%28_,interval%29.md)) automatically adjusts to match the applied pressure. As the user force clicks (presses harder), the button sends actions more rapidly. As the user reduces pressure on the button, actions slow down. As such, the user has direct control over how fast the button sends actions. Continuous accelerator buttons are intended for continuously advancing through a series of discrete objects, such as photos in an album or pages in a book.

For noncontinuous accelerator buttons, they send actions whenever a change in force occurs. Noncontinuous accelerator buttons are for adjusting the speed of navigation, such as playback speed in a media player, based on pressure. After the user releases the button, the button sends a final action.

For buttons that aren’t accelerator buttons, the value of the button matches its state. For accelerator buttons, the value of the button is distinct from its state and indicates pressure level. While the user force clicks the button, [`doubleValue`](./nscontrol/doublevalue.md) is a measurement of pressure between `1.0` and approaching `2.0`. When the user releases the button, `doubleValue` is `0.0`.

An accelerator button appears like any other button and doesn’t provide any visual indication that it supports variable pressure. To provide this type of visual indication, you can apply a custom [`image`](./nsbutton/image.md) to the button.

On a system that doesn’t support pressure sensitivity, an accelerator button behaves like a button of type [`NSMomentaryLightButton`](./nsmomentarylightbutton.md).

## See Also

### Deprecated constants
- [NSMomentaryLightButton](./nsmomentarylightbutton.md)
  When the button is clicked (on state), it appears illuminated. If the button has borders, it may also appear recessed. When the button is released, it returns to its normal (off) state.
- [NSPushOnPushOffButton](./nspushonpushoffbutton.md)
  When the button is clicked (on state), it appears illuminated. If the button has borders, it may also appear recessed. A second click returns it to its normal (off) state.
- [NSToggleButton](./nstogglebutton.md)
  After the first click, the button displays its alternate image or title (on state); a second click returns the button to its normal (off) state.
- [NSSwitchButton](./nsswitchbutton.md)
  This style is a variant of `NSToggleButton` that has no border and is typically used to represent a checkbox.
- [NSRadioButton](./nsradiobutton.md)
  This style is similar to `NSSwitchButton`, but it is used to constrain a selection to a single element from several elements.
- [NSMomentaryChangeButton](./nsmomentarychangebutton.md)
  When the button is clicked, the alternate (on state) image and alternate title are displayed.
- [NSOnOffButton](./nsonoffbutton.md)
  The first click highlights the button; a second click returns it to the normal (unhighlighted) state.
- [NSMultiLevelAcceleratorButton](./nsmultilevelacceleratorbutton.md)
  A multilevel accelerator button is a variation of a normal accelerator button that allows for a configurable number of stepped pressure levels. As each one is reached, the user receives light tactile feedback and an action is sent.
- [NSMomentaryPushInButton](./nsmomentarypushinbutton.md)
  When the user clicks the button (on state), the button appears illuminated.
- [NSMomentaryPushButton](./nsmomentarypushbutton.md)
  When the button is clicked (on state), it appears illuminated. If the button has a bordered, it may also appear recessed. When the button is released, it returns to its normal (off) state.
- [NSMomentaryLight](./nsmomentarylight.md)
  When the button is clicked (on state), it appears illuminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsacceleratorbutton)*