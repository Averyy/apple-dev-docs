# prepareForPresentation(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Performs any custom configuration of the document picker view controller.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For more information, see [`UIDocumentPickerExtensionViewController`](../uidocumentpickerextensionviewcontroller.md).

## Declaration

```swift
func prepareForPresentation(in mode: UIDocumentPickerMode)
```

```objc
- (void) prepareForPresentationInMode:(UIDocumentPickerMode) mode;
```

## Discussion

The system calls this method when a host app presents a document picker view controller for your Document Picker extension. Override this method to provide a custom user interface based on the provided mode.

Different modes may require different user interfaces. For example, the UIDocumentPickerModeImport and UIDocumentPickerModeOpen modes should let the user explore the available documents, whereas the UIDocumentPickerModeExportToService and UIDocumentPickerModeMoveToService modes let the user select the destination.

When overriding this method, examine the mode and present an appropriate user interface for the task at hand. If the differences between the modes are significant, consider creating separate child view controllers for each mode and then present the appropriate child in this method.

If your extension can manage multiple file types, check the [`validTypes`](./validtypes.md) property and make sure you are presenting only files that match one or more of the specified types.

## Parameters

- `mode`: The type of file-transfer operation that the document picker performs. For a list of valid modes, see `Document Picker Modes`.

## See Also

### Managing the user interface
- [func dismissGrantingAccess(to: URL?)](./dismissgrantingaccess%28to%29.md)
  Dismisses the document picker.
- [var documentPickerMode: UIDocumentPickerMode](./documentpickermode.md)
  The document picker’s file-transfer operation. (read-only)
- [var documentStorageURL: URL?](./documentstorageurl.md)
  The root URL for documents provided by the corresponding File Provider extension. (read-only)
- [var originalURL: URL?](./originalurl.md)
  The URL of the file to be exported. (read-only)
- [var providerIdentifier: String](./provideridentifier.md)
  An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only)
- [var validTypes: [String]?](./validtypes.md)
  An array of valid uniform type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/prepareforpresentation(in:))*