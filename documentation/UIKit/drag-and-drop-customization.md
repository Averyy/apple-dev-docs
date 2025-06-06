# Drag and drop customization

**Framework**: UIKit

Extend the standard drag and drop support for text views to include custom types of content.

#### Overview

The [`UITextField`](uitextfield.md) and [`UITextView`](uitextview.md) classes provide built-in support for dragging and dropping text and images. You can extend this support to your own custom data types by adding a text drag delegate or text drop delegate to your views. Your text drag delegate adopts the [`UITextDragDelegate`](uitextdragdelegate.md) protocol and is responsible for providing the items to be dragged. Your text drop delegate adopts the [`UITextDropDelegate`](uitextdropdelegate.md) protocol and handles drops containing items with your custom data types.

## Topics

### Text view additions
- [protocol UITextDragDelegate](uitextdragdelegate.md)
  The interface for customizing the behavior of a drag activity for a text view.
- [protocol UITextDropDelegate](uitextdropdelegate.md)
  The interface for configuring a text view’s drop behavior.
- [protocol UITextDraggable](uitextdraggable.md)
  The interface that determines if a text view is a drag source.
- [struct UITextDragOptions](uitextdragoptions.md)
  A set of options that determine the behavior of a draggable text view.
- [protocol UITextDroppable](uitextdroppable.md)
  The interface that determines if a text view is a drop destination.
- [enum UITextDropEditability](uitextdropeditability.md)
  The text-drop editability styles for noneditable text views.
### Drag content
- [protocol UITextDragRequest](uitextdragrequest.md)
  The interface for describing the attributes of a drag activity originating in a text view.
- [class UITextDragPreviewRenderer](uitextdragpreviewrenderer.md)
  Renders previews of text dragged by the user.
### Drop management
- [protocol UITextDropRequest](uitextdroprequest.md)
  The interface for specifying the attributes of a drop request for a text view.
- [class UITextDropProposal](uitextdropproposal.md)
  A proposed configuration for the behavior of a text drop interaction.
- [UITextDropProposal.Action](uitextdropproposal/action.md)
  The text drop action styles for text views.
- [UITextDropProposal.Performer](uitextdropproposal/performer.md)
  The performers that are responsible for handling the drop operation.
- [UITextDropProposal.ProgressMode](uitextdropproposal/progressmode.md)
  The text drop progress styles for user-visible progress indication.
### Pasteboard support
- [protocol UITextPasteItem](uitextpasteitem.md)
  The interface for obtaining information about, and interacting with, a text item for pasting or dropping.
- [protocol UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md)
  A protocol that supports pasting tokens.
- [protocol UITextPasteDelegate](uitextpastedelegate.md)
  The interface for handling pasting and dropping of text, using item providers.
- [protocol UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md)
  The interface for text-oriented responder objects to participate in the unified paste and drop system in iOS.

## See Also

- [class UILabel](uilabel.md)
  A view that displays one or more lines of informational text.
- [class UITextField](uitextfield.md)
  An object that displays an editable text area in your interface.
- [class UITextView](uitextview.md)
  A scrollable, multiline text region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/drag-and-drop-customization)*