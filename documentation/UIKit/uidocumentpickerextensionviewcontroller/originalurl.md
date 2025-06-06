# originalURL

**Framework**: UIKit  
**Kind**: property

The URL of the file to be exported. (read-only)

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var originalURL: URL? { get }
```

#### Discussion

While in UIDocumentPickerModeExportToService mode, this property contains the original URL of the file to be copied. Otherwise it is `nil`.

## See Also

- [func dismissGrantingAccess(to: URL?)](uidocumentpickerextensionviewcontroller/dismissgrantingaccess(to:).md)
  Dismisses the document picker.
- [var documentPickerMode: UIDocumentPickerMode](uidocumentpickerextensionviewcontroller/documentpickermode.md)
  The document picker’s file-transfer operation. (read-only)
- [var documentStorageURL: URL?](uidocumentpickerextensionviewcontroller/documentstorageurl.md)
  The root URL for documents provided by the corresponding File Provider extension. (read-only)
- [func prepareForPresentation(in: UIDocumentPickerMode)](uidocumentpickerextensionviewcontroller/prepareforpresentation(in:).md)
  Performs any custom configuration of the document picker view controller.
- [var providerIdentifier: String](uidocumentpickerextensionviewcontroller/provideridentifier.md)
  An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only)
- [var validTypes: [String]?](uidocumentpickerextensionviewcontroller/validtypes.md)
  An array of valid uniform type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/originalurl)*