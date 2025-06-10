# Additional Writing Directions

**Framework**: AppKit

Additional values to be added to [`NSWritingDirection.leftToRight`](nswritingdirection/lefttoright.md) or [`NSWritingDirection.rightToLeft`](nswritingdirection/righttoleft.md), when used with `NSAttributedString/Key/writingDirection`.

#### Overview

You can use the logical `OR` operator to combine these constants with [`NSWritingDirection.leftToRight`](nswritingdirection/lefttoright.md) or [`NSWritingDirection.rightToLeft`](nswritingdirection/righttoleft.md) when used with `NSAttributedString/Key/writingDirection` to specify formatting controls defined by the Unicode Bidirectional Algorithm in Unicode Standard Annex #9.

## Topics

### Constants
- [var NSTextWritingDirectionEmbedding: Int](nstextwritingdirectionembedding.md)
  Text is embedded in text with another writing direction.
- [var NSTextWritingDirectionOverride: Int](nstextwritingdirectionoverride.md)

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
- [Return values for modal operations](return-values-for-modal-operations.md)
  Historical return values for [`runModal(for:)`](nsapplication/runmodal(for:).md) and [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md).
- [Tags of Views in the FontPanel](tags-of-views-in-the-fontpanel.md)
  These constants are obsolete and should not be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/additional-writing-directions)*