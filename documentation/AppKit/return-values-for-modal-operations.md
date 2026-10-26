# Return values for modal operations

**Framework**: AppKit  
**Role**: API Collection

Historical return values for [`runModal(for:)`](./nsapplication/runmodal%28for%29.md) and [`runModalSession(_:)`](./nsapplication/runmodalsession%28_%29.md).

#### Overview

The system also reserves all values below these.

## Topics

### Constants
- [var NSRunAbortedResponse: Int](./nsrunabortedresponse.md)
  Modal session was broken with [`abortModal()`](./nsapplication/abortmodal%28%29.md).
- [var NSRunContinuesResponse: Int](./nsruncontinuesresponse.md)
  Modal session is continuing (returned by [`runModalSession(_:)`](./nsapplication/runmodalsession%28_%29.md) only).
- [var NSRunStoppedResponse: Int](./nsrunstoppedresponse.md)
  Modal session was broken with [`stopModal()`](./nsapplication/stopmodal%28%29.md).

## See Also

### Deprecated enumerations
- [enum NSMultibyteGlyphPacking](./nsmultibyteglyphpacking.md)
  A constant for glyph packing.
- [Glyph Attributes](./glyph-attributes.md)
  Attributes that are used only inside the glyph generation machinery, but must also be shared between components.
- [enum NSOpenGLGlobalOption](./nsopenglglobaloption.md)
  Constants that specify OpenGL options.
- [Data Entry Types](./data-entry-types.md)
  These constants specify how a cell formats numeric data.
- [Anonymous](./nsbuttontypes-anonymous.md)
- [Additional Writing Directions](./additional-writing-directions.md)
  Constants that specify additional options when setting the writing direction of attributed strings.
- [Tags of Views in the FontPanel](./tags-of-views-in-the-fontpanel.md)
  These constants are obsolete and should not be used.
- [NSInterfaceStyle](./nsinterfacestyle.md)
  These constants are used in `NSResponder`’s [`interfaceStyle`](./nsresponder/interfacestyle.md) method.
- [NSNoUnderlineStyle](./nsnounderlinestyle.md)
- [NSSingleUnderlineStyle](./nssingleunderlinestyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/return-values-for-modal-operations)*