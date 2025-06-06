# UIDocumentPickerDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods for tracking when the user selects a document or destination, or cancels the operation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIDocumentPickerDelegate : NSObjectProtocol
```

## Topics

### Responding to user actions
- [func documentPicker(UIDocumentPickerViewController, didPickDocumentsAt: [URL])](uidocumentpickerdelegate/documentpicker(_:didpickdocumentsat:).md)
  Tells the delegate that the user has selected one or more documents.
- [func documentPickerWasCancelled(UIDocumentPickerViewController)](uidocumentpickerdelegate/documentpickerwascancelled(_:).md)
  Tells the delegate that the user canceled the document picker.
- [func documentPicker(UIDocumentPickerViewController, didPickDocumentAt: URL)](uidocumentpickerdelegate/documentpicker(_:didpickdocumentat:).md)
  Tells the delegate that the user has selected a document or a destination.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UIDocumentPickerDelegate)?](uidocumentpickerviewcontroller/delegate.md)
  An object that acts as the delegate of the view controller.
- [var allowsMultipleSelection: Bool](uidocumentpickerviewcontroller/allowsmultipleselection.md)
  A Boolean value that determines whether the user can select more than one document at a time.
- [var directoryURL: URL?](uidocumentpickerviewcontroller/directoryurl.md)
  The initial directory that the document picker displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate)*