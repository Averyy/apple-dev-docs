# TextKit

**Framework**: UIKit

Manage text storage and perform custom layout of text-based content in your app’s views.

#### Overview

TextKit provides several classes to control the layout of text, such as [`NSTextContentStorage`](nstextcontentstorage.md), [`NSTextLayoutManager`](nstextlayoutmanager.md), and [`NSTextContainer`](nstextcontainer.md).

Additionally, TextKit uses [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) objects extensively. The [`NSTextStorage`](nstextstorage.md) class is a subclass of [`NSMutableAttributedString`](https://developer.apple.com/documentation/Foundation/NSMutableAttributedString), and many of the TextKit classes focus on creating complex [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) instances. Use these classes to specify your text’s format.

Most of the time, you can use TextKit to fine tune the formatting and layout of a [`UITextView`](uitextview.md) by modifying the view’s [`textContainer`](uitextview/textcontainer.md), [`layoutManager`](uitextview/layoutmanager.md), or [`textStorage`](uitextview/textstorage.md) properties. If you need more control, you can also use TextKit to build custom text controls.

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
### Content elements
- [Enriching your text in text views](enriching-your-text-in-text-views.md)
  Add exclusion paths, text attachments, and text lists to your text, and render it with text views.
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
- [protocol NSTextLocation](nstextlocation.md)
  An interface you implement that represents an abstract location inside your document’s content.
### Layout
- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md)
  Interact with text by managing text selection and inserting custom text elements.
- [Display text with a custom layout](display-text-with-a-custom-layout.md)
  Lay out text in a custom-shaped container and apply glyph substitutions.
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
### Attachments
- [class NSTextAttachment](nstextattachment.md)
  The values for the attachment characteristics of attributed strings and related objects.
- [class NSTextAttachmentViewProvider](nstextattachmentviewprovider.md)
  A container object that associates a text attachment at a particular document location with a view object.
- [class NSAdaptiveImageGlyph](nsadaptiveimageglyph.md)
  A data object for an emoji-like image that can appear in attributed text.
- [protocol NSTextAttachmentContainer](nstextattachmentcontainer.md)
  A set of methods that defines the interface to text attachment objects from a layout manager.
- [protocol NSTextAttachmentLayout](nstextattachmentlayout.md)
  A set of methods that defines the interface to attachment objects from a text layout manager.
### TextKit 1
- [class NSTextStorage](nstextstorage.md)
  The fundamental storage mechanism of TextKit that contains the text managed by the system.
- [class NSLayoutManager](nslayoutmanager.md)
  An object that coordinates the layout and display of text characters.

## See Also

- [Text display and fonts](text-display-and-fonts.md)
  Display text, manage fonts, and check spelling.
- [Keyboards and input](keyboards-and-input.md)
  Configure the system keyboard, create your own keyboards to handle input, or detect key presses on a physical keyboard.
- [Writing Tools](writing-tools.md)
  Add support for Writing Tools to your app’s text views.
- [Handwriting recognition](handwriting-recognition.md)
  Configure text fields and custom views that accept text to handle input from Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/textkit)*