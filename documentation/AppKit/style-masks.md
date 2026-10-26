# Style Masks

**Framework**: AppKit  
**Role**: API Collection

Constants that specify panel styles.

## Topics

### Deprecated
- [NSDocModalWindowMask](./nsdocmodalwindowmask.md)
  The panel is created as a modal sheet.
- [NSUtilityWindowMask](./nsutilitywindowmask.md)
  The panel is created as a floating window.
- [NSNonactivatingPanelMask](./nsnonactivatingpanelmask.md)
  The panel can receive keyboard input without activating the owning app.
- [NSHUDWindowMask](./nshudwindowmask.md)
  The panel is created as a transparent panel (sometimes called a “heads-up display”).

## See Also

### Constants
- [Alert Panel Return Values](./alert-panel-return-values.md)
  These constants define values returned by the [`NSRunAlertPanel`](./nsrunalertpanel.md) function and by the `NSApplication` method [`runModalSession(_:)`](./nsapplication/runmodalsession%28_%29.md) when the modal session is run with an `NSPanel` provided by the [`NSGetAlertPanel`](./nsgetalertpanel.md) function.
- [Modal Panel Return Values](./modal-panel-return-values.md)
  These constants define the possible return values for such methods as the `runModal...` methods of the [`NSOpenPanel`](./nsopenpanel.md) class, which tell which button (OK or Cancel) the user has clicked on an open panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/style-masks)*