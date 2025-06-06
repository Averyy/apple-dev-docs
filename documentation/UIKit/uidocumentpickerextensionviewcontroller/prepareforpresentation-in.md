# prepareForPresentation(in:)

**Framework**: UIKit  
**Kind**: method

Performs any custom configuration of the document picker view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func prepareForPresentation(in mode: UIDocumentPickerMode)
```

#### Discussion

The system calls this method when a host app presents a document picker view controller for your Document Picker extension. Override this method to provide a custom user interface based on the provided mode.

Different modes may require different user interfaces. For example, the UIDocumentPickerModeImport and UIDocumentPickerModeOpen modes should let the user explore the available documents, whereas the UIDocumentPickerModeExportToService and UIDocumentPickerModeMoveToService modes let the user select the destination.

When overriding this method, examine the mode and present an appropriate user interface for the task at hand. If the differences between the modes are significant, consider creating separate child view controllers for each mode and then present the appropriate child in this method.

If your extension can manage multiple file types, check the [`validTypes`](uidocumentpickerextensionviewcontroller/validtypes.md) property and make sure you are presenting only files that match one or more of the specified types.

## Parameters

- `mode`: The type of file-transfer operation that the document picker performs. For a list of valid modes, see  .

## See Also

- [func dismissGrantingAccess(to: URL?)](uidocumentpickerextensionviewcontroller/dismissgrantingaccess(to:).md)
  Dismisses the document picker.
- [var documentPickerMode: UIDocumentPickerMode](uidocumentpickerextensionviewcontroller/documentpickermode.md)
  The document picker’s file-transfer operation. (read-only)
- [var documentStorageURL: URL?](uidocumentpickerextensionviewcontroller/documentstorageurl.md)
  The root URL for documents provided by the corresponding File Provider extension. (read-only)
- [var originalURL: URL?](uidocumentpickerextensionviewcontroller/originalurl.md)
  The URL of the file to be exported. (read-only)
- [var providerIdentifier: String](uidocumentpickerextensionviewcontroller/provideridentifier.md)
  An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only)
- [var validTypes: [String]?](uidocumentpickerextensionviewcontroller/validtypes.md)
  An array of valid uniform type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/prepareforpresentation(in:))*