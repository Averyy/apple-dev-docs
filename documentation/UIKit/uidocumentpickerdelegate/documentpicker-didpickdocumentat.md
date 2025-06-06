# documentPicker(_:didPickDocumentAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user has selected a document or a destination.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func documentPicker(_ controller: UIDocumentPickerViewController, didPickDocumentAt url: URL)
```

#### Discussion

The meaning of the provided URL varies depending on the document picker’s mode:

- `UIDocumentPickerModeImport`

The URL refers to a copy of the selected document. This document is a temporary file. It remains available only until your application terminates. To keep a permanent copy, you must move this file to a permanent location inside your sandbox.

- `UIDocumentPickerModeOpen`

The URL refers to the selected document. The provided URL is a security-scoped URL referring to a file outside your app’s sandbox. For more information on working with external, security-scoped URLs, see [`Requirements`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentPickerProgrammingGuide/AccessingDocuments/AccessingDocuments.html#//apple_ref/doc/uid/TP40014451-CH2-SW3).

- `UIDocumentPickerModeExportToService`

The URL refers to the new copy of the exported document at the selected destination. This URL refers to a file outside your app’s sandbox. You cannot access this copy; the URL is passed only to indicate success.

- `UIDocumentPickerModeMoveToService`

The URL refers to the document’s new location. The provided URL is a security-scoped URL referring to a file outside your app’s sandbox. For more information on working with external, security-scoped URLs, see [`Requirements`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentPickerProgrammingGuide/AccessingDocuments/AccessingDocuments.html#//apple_ref/doc/uid/TP40014451-CH2-SW3).

## Parameters

- `controller`: The document picker that called this method.
- `url`: The URL of the selected document or destination.

## See Also

- [func documentPicker(UIDocumentPickerViewController, didPickDocumentsAt: [URL])](uidocumentpickerdelegate/documentpicker(_:didpickdocumentsat:).md)
  Tells the delegate that the user has selected one or more documents.
- [func documentPickerWasCancelled(UIDocumentPickerViewController)](uidocumentpickerdelegate/documentpickerwascancelled(_:).md)
  Tells the delegate that the user canceled the document picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate/documentpicker(_:didpickdocumentat:))*