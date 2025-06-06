# Return values for modal operations

**Framework**: AppKit

Historical return values for [`runModal(for:)`](nsapplication/runmodal(for:).md) and [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md).

#### Overview

The system also reserves all values below these.

## Topics

### Constants
- [var NSRunAbortedResponse: Int](nsrunabortedresponse.md)
  Modal session was broken with [`abortModal()`](nsapplication/abortmodal().md).
- [var NSRunContinuesResponse: Int](nsruncontinuesresponse.md)
  Modal session is continuing (returned by [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md) only).
- [var NSRunStoppedResponse: Int](nsrunstoppedresponse.md)
  Modal session was broken with [`stopModal()`](nsapplication/stopmodal().md).

## See Also

- [enum NSMultibyteGlyphPacking](nsmultibyteglyphpacking.md)
  A constant for glyph packing.
- [Glyph Attributes](glyph-attributes.md)
  Attributes that are used only inside the glyph generation machinery, but must also be shared between components.
- [enum NSOpenGLGlobalOption](nsopenglglobaloption.md)
  Constants that specify OpenGL options.
- [Data Entry Types](data-entry-types.md)
  These constants specify how a cell formats numeric data.
- [Anonymous](nsbuttontypes-anonymous.md)
- [Additional Writing Directions](additional-writing-directions.md)
  Additional values to be added to [`NSWritingDirection.leftToRight`](nswritingdirection/lefttoright.md) or [`NSWritingDirection.rightToLeft`](nswritingdirection/righttoleft.md), when used with [`writingDirection`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1524497-writingdirection).
- [Tags of Views in the FontPanel](tags-of-views-in-the-fontpanel.md)
  These constants are obsolete and should not be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/return-values-for-modal-operations)*