# init(documentTypes:in:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns a document menu to import or open the given file types.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(documentTypes allowedUTIs: [String], in mode: UIDocumentPickerMode)
```

#### Return Value

Returns an initialized `UIDocumentMenuViewController` object, or `nil` if the object could not be successfully initialized.

#### Discussion

The UTI array defines the type of documents that can be imported or opened. The resulting document menu displays all the document pickers appropriate for the given document types and mode.

## Parameters

- `allowedUTIs`: An array of uniform type identifiers. UTIs are strings that uniquely identify a file’s type. For more information, see [`Uniform Type Identifiers Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319).
- `mode`: The type of file transfer operation the document picker performs. This argument accepts only the [`UIDocumentPickerMode.import`](uidocumentpickermode/import.md) or [`UIDocumentPickerMode.open`](uidocumentpickermode/open.md) mode.

## See Also

- [init(url: URL, in: UIDocumentPickerMode)](uidocumentmenuviewcontroller/init(url:in:).md)
  Initializes and returns a document menu to export or move the given document.
- [init?(coder: NSCoder)](uidocumentmenuviewcontroller/init(coder:).md)
  Creates a document menu from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/init(documenttypes:in:))*