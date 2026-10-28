# NSMomentaryChangeButton

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

When the button is clicked, the alternate (on state) image and alternate title are displayed.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use [`NSButton.ButtonType.momentaryChange`](./nsbutton/buttontype/momentarychange.md) instead.

## Declaration

```c
static const NSButtonType NSMomentaryChangeButton;
```

## Discussion

Otherwise, the normal (off state) image and title are displayed. This option is called Momentary Change in Interface Builder’s Button inspector.

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
- [NSOnOffButton](./nsonoffbutton.md)
  The first click highlights the button; a second click returns it to the normal (unhighlighted) state.
- [NSAcceleratorButton](./nsacceleratorbutton.md)
  A button that sends an action when the user first clicks the button and continues sending actions until the user releases pressure entirely.
- [NSMultiLevelAcceleratorButton](./nsmultilevelacceleratorbutton.md)
  A multilevel accelerator button is a variation of a normal accelerator button that allows for a configurable number of stepped pressure levels. As each one is reached, the user receives light tactile feedback and an action is sent.
- [NSMomentaryPushInButton](./nsmomentarypushinbutton.md)
  When the user clicks the button (on state), the button appears illuminated.
- [NSMomentaryPushButton](./nsmomentarypushbutton.md)
  When the button is clicked (on state), it appears illuminated. If the button has a bordered, it may also appear recessed. When the button is released, it returns to its normal (off) state.
- [NSMomentaryLight](./nsmomentarylight.md)
  When the button is clicked (on state), it appears illuminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmomentarychangebutton)*