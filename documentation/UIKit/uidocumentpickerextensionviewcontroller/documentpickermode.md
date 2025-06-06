# documentPickerMode

**Framework**: UIKit  
**Kind**: property

The document picker’s file-transfer operation. (read-only)

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var documentPickerMode: UIDocumentPickerMode { get }
```

#### Discussion

For a list of available modes, see `Document Picker Modes` in [`UIDocumentPickerViewController`](uidocumentpickerviewcontroller.md).

## See Also

- [func dismissGrantingAccess(to: URL?)](uidocumentpickerextensionviewcontroller/dismissgrantingaccess(to:).md)
  Dismisses the document picker.
- [var documentStorageURL: URL?](uidocumentpickerextensionviewcontroller/documentstorageurl.md)
  The root URL for documents provided by the corresponding File Provider extension. (read-only)
- [var originalURL: URL?](uidocumentpickerextensionviewcontroller/originalurl.md)
  The URL of the file to be exported. (read-only)
- [func prepareForPresentation(in: UIDocumentPickerMode)](uidocumentpickerextensionviewcontroller/prepareforpresentation(in:).md)
  Performs any custom configuration of the document picker view controller.
- [var providerIdentifier: String](uidocumentpickerextensionviewcontroller/provideridentifier.md)
  An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only)
- [var validTypes: [String]?](uidocumentpickerextensionviewcontroller/validtypes.md)
  An array of valid uniform type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/documentpickermode)*