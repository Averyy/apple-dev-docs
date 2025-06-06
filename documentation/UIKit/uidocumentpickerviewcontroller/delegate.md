# delegate

**Framework**: UIKit  
**Kind**: property

An object that acts as the delegate of the view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIDocumentPickerDelegate)? { get set }
```

#### Discussion

The delegate must adopt the [`UIDocumentPickerDelegate`](uidocumentpickerdelegate.md) protocol.

## See Also

- [protocol UIDocumentPickerDelegate](uidocumentpickerdelegate.md)
  A set of methods for tracking when the user selects a document or destination, or cancels the operation.
- [var allowsMultipleSelection: Bool](uidocumentpickerviewcontroller/allowsmultipleselection.md)
  A Boolean value that determines whether the user can select more than one document at a time.
- [var directoryURL: URL?](uidocumentpickerviewcontroller/directoryurl.md)
  The initial directory that the document picker displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/delegate)*