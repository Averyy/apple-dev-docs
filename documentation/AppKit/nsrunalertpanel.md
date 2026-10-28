# NSRunAlertPanel

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Creates an alert panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`NSAlert`](./nsalert.md) instead.

## Declaration

```c
extern NSInteger NSRunAlertPanel(NSString *title, NSString *msgFormat, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);
```

## Discussion

Creates and runs an alert panel (or dialog) with the title of `title` and buttons with titles of `defaultButton`, `alternateButton`, and `otherButton`. The optional alert message specified by `msgFormat` should be a static value that can consist of variable values using a format string (list any necessary arguments for this formatted string at the end of the function’s argument list), an unformatted string, or an empty string (`@""`), but not `nil`. Note that passing an untrusted string in `msgFormat` can lead to security issues. See the description of [`NSBeginAlertSheet`](./nsbeginalertsheet.md) for information on layout of buttons, default parameters, and possible return values. `NSRunAlertPanel` runs the panel in a modal event loop.

A Command-D key equivalent for the “Don’t Save” button is provided, if one is found. The button titles are searched for the localized value for “Don’t Save.” If a match is found, that button is assigned a Command-D key equivalent, provided it is not the default button.

If you create a modal panel using [`runModal(for:)`](./nsapplication/runmodal%28for%29.md) or [`beginSheet(_:modalFor:modalDelegate:didEnd:contextInfo:)`](./nsapplication/beginsheet%28_,modalfor,modaldelegate,didend,contextinfo%29.md), you can assign the key equivalent yourself, using [`keyEquivalent`](./nsbutton/keyequivalent.md) and [`keyEquivalentModifierMask`](./nsbutton/keyequivalentmodifiermask.md).

This function not only creates the panel; it also puts the panel onscreen and runs it using the [`runModal(for:)`](./nsapplication/runmodal%28for%29.md) method defined in the [`NSApplication`](./nsapplication.md) class. This method sets up a modal event loop that causes the panel to remain onscreen until the user clicks one of its buttons. This function then removes the panel from the screen list and returns a value that indicates which of the three buttons the user clicked. For efficiency, this function creates the panel the first time it’s called and reuses it on subsequent calls, reconfiguring it if necessary.

## See Also

### Deprecated functions
- [func NSConvertGlyphsToPackedGlyphs(UnsafeMutablePointer<NSGlyph>, Int, NSMultibyteGlyphPacking, UnsafeMutablePointer<CChar>) -> Int](./nsconvertglyphstopackedglyphs%28_,_,_,_%29.md)
  Prepares a set of glyphs for processing by character-based routines.
- [NSOpenGLGetOption](./nsopenglgetoption.md)
  Returns global OpenGL options.
- [NSOpenGLGetVersion](./nsopenglgetversion.md)
  Returns the NSOpenGL version numbers.
- [NSOpenGLSetOption](./nsopenglsetoption.md)
  Sets global OpenGL options.
- [static func raiseBadArgumentException(Any!, NSAccessibility.Attribute!, Any!)](./nsaccessibility-swift.struct/raisebadargumentexception%28_,_,_%29.md)
  Raises an error if the parameter is the wrong type or has an illegal value
- [NSBeginAlertSheet](./nsbeginalertsheet.md)
  Creates and runs an alert sheet.
- [NSBeginCriticalAlertSheet](./nsbegincriticalalertsheet.md)
  Creates and runs a critical alert sheet.
- [NSBeginInformationalAlertSheet](./nsbegininformationalalertsheet.md)
  Creates and runs an informational alert sheet.
- [NSGetAlertPanel](./nsgetalertpanel.md)
  Returns an alert panel.
- [NSGetCriticalAlertPanel](./nsgetcriticalalertpanel.md)
  Returns an alert panel to display a critical message.
- [NSGetInformationalAlertPanel](./nsgetinformationalalertpanel.md)
  Returns an alert panel to display an informational message.
- [func NSReleaseAlertPanel(Any!)](./nsreleasealertpanel%28_%29.md)
  Disposes of an alert panel.
- [NSRunCriticalAlertPanel](./nsruncriticalalertpanel.md)
  Creates and runs a critical alert panel.
- [NSRunInformationalAlertPanel](./nsruninformationalalertpanel.md)
  Creates and runs an informational alert panel.
- [NSRunAlertPanelRelativeToWindow](./nsrunalertpanelrelativetowindow.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunalertpanel)*