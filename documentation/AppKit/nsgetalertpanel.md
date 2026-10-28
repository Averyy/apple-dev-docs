# NSGetAlertPanel

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Returns an alert panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`NSAlert`](./nsalert.md) instead.

## Declaration

```c
extern idNSGetAlertPanel(NSString *title, NSString *msgFormat, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, ...);
```

## Discussion

Returns an [`NSPanel`](./nspanel.md) that can be used to set up a modal session. A modal session is useful for allowing the user to interrupt the program. During a modal session, you can perform activities while the panel is displayed and check at various points in your program whether the user has clicked one of the panel’s buttons. The arguments for this function are the same as those for [`NSRunAlertPanel`](./nsrunalertpanel.md), but unlike that function, no button is displayed if `defaultButton` is `nil`.

To set up a modal session, send the Application object [`beginModalSession(for:)`](./nsapplication/beginmodalsession%28for%29.md) with the panel returned by [`NSGetAlertPanel`](./nsgetalertpanel.md) as its argument. When you want to check if the user has clicked one of the panel’s buttons, use [`runModalSession(_:)`](./nsapplication/runmodalsession%28_%29.md). To end the modal session, use [`endModalSession(_:)`](./nsapplication/endmodalsession%28_%29.md). When you’re finished with the panel created by [`NSGetAlertPanel`](./nsgetalertpanel.md), you must dispose of it by passing it to [`NSReleaseAlertPanel(_:)`](./nsreleasealertpanel%28_%29.md).

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
- [NSGetCriticalAlertPanel](./nsgetcriticalalertpanel.md)
  Returns an alert panel to display a critical message.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgetalertpanel)*