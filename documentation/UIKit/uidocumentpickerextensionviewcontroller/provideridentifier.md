# providerIdentifier

**Framework**: UIKit  
**Kind**: property

An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only)

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var providerIdentifier: String { get }
```

#### Discussion

Both the Document Picker View Controller extension and the File Provider extension should pass this identifier to their file coordinator’s `setPurposeIdentifier:` method. This approach helps coordinate the read and write operations between the two extensions, preventing possible deadlocks.

This property holds the value returned by calling the File Provider extension’s [`providerIdentifier`](https://developer.apple.com/documentation/FileProvider/NSFileProviderExtension/providerIdentifier) method.

## See Also

- [func dismissGrantingAccess(to: URL?)](uidocumentpickerextensionviewcontroller/dismissgrantingaccess(to:).md)
  Dismisses the document picker.
- [var documentPickerMode: UIDocumentPickerMode](uidocumentpickerextensionviewcontroller/documentpickermode.md)
  The document picker’s file-transfer operation. (read-only)
- [var documentStorageURL: URL?](uidocumentpickerextensionviewcontroller/documentstorageurl.md)
  The root URL for documents provided by the corresponding File Provider extension. (read-only)
- [var originalURL: URL?](uidocumentpickerextensionviewcontroller/originalurl.md)
  The URL of the file to be exported. (read-only)
- [func prepareForPresentation(in: UIDocumentPickerMode)](uidocumentpickerextensionviewcontroller/prepareforpresentation(in:).md)
  Performs any custom configuration of the document picker view controller.
- [var validTypes: [String]?](uidocumentpickerextensionviewcontroller/validtypes.md)
  An array of valid uniform type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/provideridentifier)*