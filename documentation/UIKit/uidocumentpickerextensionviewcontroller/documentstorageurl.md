# documentStorageURL

**Framework**: UIKit  
**Kind**: property

The root URL for documents provided by the corresponding File Provider extension. (read-only)

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var documentStorageURL: URL? { get }
```

#### Discussion

This property returns a subdirectory of the app group container shared by the Document Picker extension and its corresponding File Provider extension. By default, this property holds the value returned by calling the File Provider extension’s [`documentStorageURL`](https://developer.apple.com/documentation/FileProvider/NSFileProviderExtension/documentStorageURL) method.

## See Also

- [func dismissGrantingAccess(to: URL?)](uidocumentpickerextensionviewcontroller/dismissgrantingaccess(to:).md)
  Dismisses the document picker.
- [var documentPickerMode: UIDocumentPickerMode](uidocumentpickerextensionviewcontroller/documentpickermode.md)
  The document picker’s file-transfer operation. (read-only)
- [var originalURL: URL?](uidocumentpickerextensionviewcontroller/originalurl.md)
  The URL of the file to be exported. (read-only)
- [func prepareForPresentation(in: UIDocumentPickerMode)](uidocumentpickerextensionviewcontroller/prepareforpresentation(in:).md)
  Performs any custom configuration of the document picker view controller.
- [var providerIdentifier: String](uidocumentpickerextensionviewcontroller/provideridentifier.md)
  An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only)
- [var validTypes: [String]?](uidocumentpickerextensionviewcontroller/validtypes.md)
  An array of valid uniform type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/documentstorageurl)*