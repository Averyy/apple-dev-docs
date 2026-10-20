# init(url:in:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a document menu to export or move the given document.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIDocumentMenuViewController`](../uidocumentmenuviewcontroller.md).

## Declaration

```swift
init(url: URL, in mode: UIDocumentPickerMode)
```

```objc
- (instancetype) initWithURL:(NSURL *) url inMode:(UIDocumentPickerMode) mode;
```

#### Return Value

Returns an initialized `UIDocumentMenuViewController` object, or `nil` if the object could not be successfully initialized.

#### Discussion

The resulting document menu displays all the document pickers appropriate for the given mode.

## Parameters

- `url`: The document to be exported or moved.
- `mode`: The type of file-transfer operation that the document picker performs. This argument accepts only the UIDocumentPickerModeExportToService or UIDocumentPickerModeMoveToService mode.

## See Also

### Creating a document menu
- [init(documentTypes: [String], in: UIDocumentPickerMode)](./init%28documenttypes,in%29.md)
  Initializes and returns a document menu to import or open the given file types.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a document menu from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/init(url:in:))*