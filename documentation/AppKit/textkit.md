# TextKit

**Framework**: AppKit

Manage text storage and perform custom layout of text-based content in your app’s views.

#### Overview

TextKit is a powerful and versatile text layout and rendering engine available in AppKit and UIKit. It provides several classes to control the layout of text, including [`NSTextLayoutManager`](nstextlayoutmanager.md), [`NSTextContentStorage`](nstextcontentstorage.md), [`NSTextViewportLayoutController`](nstextviewportlayoutcontroller.md), and [`NSTextContainer`](nstextcontainer.md).

In AppKit, you can use [`NSTextView`](nstextview.md), which packages TextKit capabilities to provide a convenient text rendering and editing experience. [`NSTextView`](nstextview.md) uses [`NSTextContentStorage`](nstextcontentstorage.md) as the text backing store manager. [`NSTextContentStorage`](nstextcontentstorage.md) uses an instance of [`NSTextStorage`](nstextstorage.md) as the backing store, which is a subclass of [`NSMutableAttributedString`](https://developer.apple.com/documentation/Foundation/NSMutableAttributedString). For an example, see [`Enriching your text in text views`](https://developer.apple.com/documentation/UIKit/enriching-your-text-in-text-views).

Alternatively, you can build custom text views using your own [`NSView`](nsview.md) by rendering text provided by the TextKit text engine. Use [`NSTextContentStorage`](nstextcontentstorage.md) if you want an [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString)-related storage type, or subclass [`NSTextContentManager`](nstextcontentmanager.md) to use your own. For an example, see [`Using TextKit 2 to interact with text`](https://developer.apple.com/documentation/UIKit/using-textkit-2-to-interact-with-text).

When using [`NSTextView`](nstextview.md), access the TextKit engine through the view’s [`textLayoutManager`](nstextview/textlayoutmanager.md), [`textContainer`](nstextview/textcontainer.md), and [`textStorage`](nstextview/textstorage.md) properties. [`NSTextView`](nstextview.md) provides access to two layout engines: the modern [`textLayoutManager`](nstextview/textlayoutmanager.md), which uses [`NSTextLayoutManager`](nstextlayoutmanager.md), and the legacy [`layoutManager`](nstextview/layoutmanager.md), which uses [`NSLayoutManager`](nslayoutmanager.md). Use [`textLayoutManager`](nstextview/textlayoutmanager.md) for better performance, and support for international languages. Because TextKit classes are available in both AppKit and UIKit, the same techniques apply across macOS, iOS, iPadOS, tvOS, and visionOS.

## Topics

### Text management
- [class NSTextContentStorage](nstextcontentstorage.md)
  A concrete object for managing your view’s text content and generating the text elements necessary for layout.
- [class NSTextContentManager](nstextcontentmanager.md)
  An abstract class that defines the interface and a default implementation for managing the text document contents.
- [class NSAttributedString](../Foundation/NSAttributedString.md)
  A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.
- [class NSMutableAttributedString](../Foundation/NSMutableAttributedString.md)
  A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.
### Formatting and attributes
- [class NSParagraphStyle](nsparagraphstyle.md)
  The paragraph or ruler attributes for an attributed string.
- [class NSMutableParagraphStyle](nsmutableparagraphstyle.md)
  An object for changing the values of the subattributes in a paragraph style attribute.
- [class NSTextTab](nstexttab.md)
  A tab in a paragraph.
- [class NSTextList](nstextlist.md)
  A section of text that forms a single list.
### Tables
- [class NSTextTable](nstexttable.md)
  An object that represents a text table as a whole.
- [class NSTextTableBlock](nstexttableblock.md)
  A text block that appears as a cell in a text table.
- [class NSTextBlock](nstextblock.md)
  A block of text laid out in a subregion of the text container.
### Content elements
- [Enriching your text in text views](../UIKit/enriching-your-text-in-text-views.md)
  Support line numbering, section collapsing, inline attachment caching, exclusion paths, text attachments, and text lists in a text view.
- [class NSTextParagraph](nstextparagraph.md)
  A class that represents a single paragraph backed by an attributed string as the contents.
- [class NSTextListElement](nstextlistelement.md)
  A class that represents a text list node.
- [class NSTextElement](nstextelement.md)
  An abstract base class that represents the smallest units of text layout such as paragraphs or attachments.
- [protocol NSTextElementProvider](nstextelementprovider.md)
  A protocol the text content manager and its concrete subclasses conform to, which defines the interface for interacting with custom content types of a text document.
### Location and selection
- [class NSTextRange](nstextrange.md)
  A class that represents a contiguous range between two locations inside document contents.
- [class NSTextSelection](nstextselection.md)
  A class that represents a single logical selection context that corresponds to an insertion point.
- [class NSTextSelectionNavigation](nstextselectionnavigation.md)
  An interface you use to expose methods for obtaining results from actions performed on text selections.
- [class NSTextSelectionManager](nstextselectionmanager.md)
  An object that coordinates text selection behavior for custom text views.
- [protocol NSTextLocation](nstextlocation.md)
  An interface you implement that represents an abstract location inside your document’s content.
### Layout
- [Using TextKit 2 to interact with text](../UIKit/using-textkit-2-to-interact-with-text.md)
  Interact with text by managing text selection and inserting custom text elements.
- [Managing viewport layout and attachment reuse in text views](../UIKit/managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)
  Customize layout and preserve attachment views in your text view subclass.
- [class NSTextLayoutManager](nstextlayoutmanager.md)
  The primary class that you use to manage text layout and presentation for custom text displays.
- [class NSTextContainer](nstextcontainer.md)
  A region where text layout occurs.
- [class NSTextLayoutFragment](nstextlayoutfragment.md)
  A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.
- [class NSTextLineFragment](nstextlinefragment.md)
  A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.
- [class NSTextViewportLayoutController](nstextviewportlayoutcontroller.md)
  Manages the layout process inside the viewport interacting with its delegate.
- [protocol NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)
  A set of methods that define the orientation of text for an object.
- [protocol NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md)
  A protocol that identifies a view or layer as a drawable element for a text layout fragment.
- [protocol NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md)
  A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.
### Attachments
- [class NSTextAttachment](nstextattachment.md)
  The values for the attachment characteristics of attributed strings and related objects.
- [class NSTextAttachmentViewProvider](nstextattachmentviewprovider.md)
  A container object that associates a text attachment at a particular document location with a view object.
- [struct NSTextAttachmentViewProviderReusePolicy](nstextattachmentviewproviderreusepolicy.md)
- [class NSAdaptiveImageGlyph](nsadaptiveimageglyph.md)
  A data object for an emoji-like image that can appear in attributed text.
- [protocol NSTextAttachmentContainer](nstextattachmentcontainer.md)
  A set of methods that defines the interface to text attachment objects from a layout manager.
- [protocol NSTextAttachmentLayout](nstextattachmentlayout.md)
  A set of methods that defines the interface to attachment objects from a text layout manager.
- [class NSTextAttachmentCell](nstextattachmentcell-swift.class.md)
  An object that implements the functionality of the text attachment cell protocol.
- [protocol NSTextAttachmentCellProtocol](nstextattachmentcellprotocol.md)
  A set of methods that declares the interface for objects that draw text attachment icons and handle mouse events on their icons.
### Glyphs
- [typealias NSGlyph](nsglyph.md)
  The type used to specify glyphs.
- [protocol NSGlyphStorage](nsglyphstorage.md)
  A set of methods that a glyph storage object must implement to interact properly with [`NSGlyphGenerator`](nsglyphgenerator.md).
- [class NSGlyphGenerator](nsglyphgenerator.md)
  An object that performs the initial, nominal glyph generation phase in the layout process.
- [class NSGlyphInfo](nsglyphinfo.md)
  A glyph attribute in an attributed string.
- [Reserved Glyph Codes](reserved-glyph-codes.md)
  These constants define reserved glyph codes.
- [enum NSFontRenderingMode](nsfontrenderingmode.md)
  The font rendering mode.
### TextKit 1
- [class NSTextStorage](nstextstorage.md)
  The fundamental storage mechanism of TextKit that contains the text managed by the system.
- [class NSLayoutManager](nslayoutmanager.md)
  An object that coordinates the layout and display of text characters.
- [class NSATSTypesetter](nsatstypesetter.md)
  A concrete typesetter object that places glyphs during the text layout process.
- [class NSTypesetter](nstypesetter.md)
  An abstract class that performs various type layout tasks.

## See Also

- [Text Display](text-display.md)
  Display text and check spelling.
- [Fonts](fonts.md)
  Manage the fonts used to display text.
- [Writing Tools](writing-tools.md)
  Add support for Writing Tools to your app’s text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/textkit)*