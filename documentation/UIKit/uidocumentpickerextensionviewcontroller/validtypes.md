# validTypes

**Framework**: UIKit  
**Kind**: property

An array of valid uniform type identifiers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var validTypes: [String]? { get }
```

#### Discussion

While in the `UIDocumentPickerModeImport` or `UIDocumentPickerModeOpen` modes, this property holds an array of valid UTIs; otherwise, it is `nil`.

Check the value of this property before your Document Picker extension displays any files to the user. You should let the user select only files that match at least one of the given UTIs.

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
- [var providerIdentifier: String](uidocumentpickerextensionviewcontroller/provideridentifier.md)
  An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/validtypes)*