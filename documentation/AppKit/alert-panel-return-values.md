# Alert Panel Return Values

**Framework**: AppKit

These constants define values returned by the [`NSRunAlertPanel`](nsrunalertpanel.md) function and by the `NSApplication` method [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md) when the modal session is run with an `NSPanel` provided by the [`NSGetAlertPanel`](nsgetalertpanel.md) function.

## Topics

### Constants
- [var NSAlertDefaultReturn: Int](nsalertdefaultreturn.md)
  The user pressed the default button.
- [var NSAlertAlternateReturn: Int](nsalertalternatereturn.md)
  The user pressed the alternate button.
- [var NSAlertOtherReturn: Int](nsalertotherreturn.md)
  The user pressed a second alternate button.
- [var NSAlertErrorReturn: Int](nsalerterrorreturn.md)
  The alert cannot identify the reason it was closed; it may have been closed by an external source or by a button other than those listed above.

## See Also

- [Modal Panel Return Values](modal-panel-return-values.md)
  These constants define the possible return values for such methods as the `runModal...` methods of the [`NSOpenPanel`](nsopenpanel.md) class, which tell which button (OK or Cancel) the user has clicked on an open panel.
- [Style Masks](style-masks.md)
  Constants that specify panel styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/alert-panel-return-values)*