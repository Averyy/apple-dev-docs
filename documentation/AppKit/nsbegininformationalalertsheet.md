# NSBeginInformationalAlertSheet

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Creates and runs an informational alert sheet.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`NSAlert`](./nsalert.md) instead.

## Declaration

```c
extern void NSBeginInformationalAlertSheet(NSString *title, NSString *defaultButton, NSString *alternateButton, NSString *otherButton, NSWindow *docWindow, id modalDelegate, SEL didEndSelector, SEL didDismissSelector, void *contextInfo, NSString *msgFormat, ...);
```

#### Discussion

Creates and runs an informational alert sheet on `docWindow`, with the title of `title`, the text of `msg`, and buttons with titles of `defaultButton`, `alternateButton`, and `otherButton`.

See the description of [`NSBeginAlertSheet`](./nsbeginalertsheet.md) for information on layout, default parameters, and the selectors.

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
- [NSGetAlertPanel](./nsgetalertpanel.md)
  Returns an alert panel.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbegininformationalalertsheet)*