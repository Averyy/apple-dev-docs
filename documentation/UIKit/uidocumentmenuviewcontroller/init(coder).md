# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a document menu from data in an unarchiver.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIDocumentMenuViewController`](../uidocumentmenuviewcontroller.md).

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## See Also

### Creating a document menu
- [init(documentTypes: [String], in: UIDocumentPickerMode)](./init%28documenttypes,in%29.md)
  Initializes and returns a document menu to import or open the given file types.
- [init(url: URL, in: UIDocumentPickerMode)](./init%28url,in%29.md)
  Initializes and returns a document menu to export or move the given document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/init(coder:))*