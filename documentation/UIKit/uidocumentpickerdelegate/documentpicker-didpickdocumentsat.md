# documentPicker(_:didPickDocumentsAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user has selected one or more documents.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func documentPicker(_ controller: UIDocumentPickerViewController, didPickDocumentsAt urls: [URL])
```

## Mentions

- [Providing access to directories](providing-access-to-directories.md)

#### Discussion

The meaning of the provided URLs varies depending on the document picker’s mode:

- `UIDocumentPickerModeImport`

The URLs refer to a copy of the selected documents. These documents are temporary files. They remain available only until your application terminates. To keep a permanent copy, move these files to a permanent location inside your sandbox.

- `UIDocumentPickerModeOpen`

The URLs refer to the selected documents.

- `UIDocumentPickerModeExportToService`

The URLs refer to new copies of the exported documents at the selected destination.

- `UIDocumentPickerModeMoveToService`

The URLs refer to the documents’ new locations.

The provided URLs are security-scoped, referring to files outside your app’s sandbox. For more about working with external, security-scoped URLs, see [`Requirements`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentPickerProgrammingGuide/AccessingDocuments/AccessingDocuments.html#//apple_ref/doc/uid/TP40014451-CH2-SW3) in the [`Document Picker Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentPickerProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014451).

## Parameters

- `controller`: The document picker that called this method.
- `urls`: The URLs of the selected documents.

## See Also

- [func documentPickerWasCancelled(UIDocumentPickerViewController)](uidocumentpickerdelegate/documentpickerwascancelled(_:).md)
  Tells the delegate that the user canceled the document picker.
- [func documentPicker(UIDocumentPickerViewController, didPickDocumentAt: URL)](uidocumentpickerdelegate/documentpicker(_:didpickdocumentat:).md)
  Tells the delegate that the user has selected a document or a destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate/documentpicker(_:didpickdocumentsat:))*