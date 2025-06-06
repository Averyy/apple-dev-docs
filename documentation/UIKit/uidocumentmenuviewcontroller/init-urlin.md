# init(url:in:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns a document menu to export or move the given document.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
init(url: URL, in mode: UIDocumentPickerMode)
```

#### Return Value

Returns an initialized `UIDocumentMenuViewController` object, or `nil` if the object could not be successfully initialized.

#### Discussion

The resulting document menu displays all the document pickers appropriate for the given mode.

## Parameters

- `url`: The document to be exported or moved.
- `mode`: The type of file-transfer operation that the document picker performs. This argument accepts only the UIDocumentPickerModeExportToService or UIDocumentPickerModeMoveToService mode.

## See Also

- [init(documentTypes: [String], in: UIDocumentPickerMode)](uidocumentmenuviewcontroller/init(documenttypes:in:).md)
  Initializes and returns a document menu to import or open the given file types.
- [init?(coder: NSCoder)](uidocumentmenuviewcontroller/init(coder:).md)
  Creates a document menu from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/init(url:in:))*