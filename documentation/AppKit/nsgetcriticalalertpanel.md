# NSGetCriticalAlertPanel

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Returns an alert panel to display a critical message.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`NSAlert`](./nsalert.md) instead.

## Declaration

```c
extern idNSGetCriticalAlertPanel(NSString *title, NSString *msgFormat, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);
```

## Discussion

Returns an [`NSPanel`](./nspanel.md) that can be used to set up a modal session. No button is displayed if `defaultButton` is `nil`. When you’re finished with the panel created by this function, you must dispose of it by passing it to [`NSReleaseAlertPanel(_:)`](./nsreleasealertpanel%28_%29.md).

The arguments for this function are the same as those for the [`NSGetAlertPanel`](./nsgetalertpanel.md). For more information on using a panel in a modal session, see [`NSGetAlertPanel`](./nsgetalertpanel.md).

The panel presented to the user is badged with a caution icon. For more information on using alerts, see Human Interface Guidelines > [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts).

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
- [NSGetInformationalAlertPanel](./nsgetinformationalalertpanel.md)
  Returns an alert panel to display an informational message.
- [func NSReleaseAlertPanel(Any!)](./nsreleasealertpanel%28_%29.md)
  Disposes of an alert panel.
- [NSRunAlertPanel](./nsrunalertpanel.md)
  Creates an alert panel.
- [NSRunCriticalAlertPanel](./nsruncriticalalertpanel.md)
  Creates and runs a critical alert panel.
- [NSRunInformationalAlertPanel](./nsruninformationalalertpanel.md)
  Creates and runs an informational alert panel.
- [NSRunAlertPanelRelativeToWindow](./nsrunalertpanelrelativetowindow.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgetcriticalalertpanel)*