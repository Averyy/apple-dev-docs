# UIDocumentPickerMode

**Framework**: UIKit  
**Kind**: enum

Modes that define the type of file transfer operation that the document picker uses.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum UIDocumentPickerMode
```

## Topics

### Constants
- [UIDocumentPickerMode.import](uidocumentpickermode/import.md)
  The document picker imports a file from outside the app’s sandbox.
- [UIDocumentPickerMode.open](uidocumentpickermode/open.md)
  The document picker opens an external file outside the app’s sandbox.
- [UIDocumentPickerMode.exportToService](uidocumentpickermode/exporttoservice.md)
  The document picker exports a local file to a destination outside the app’s sandbox.
- [UIDocumentPickerMode.moveToService](uidocumentpickermode/movetoservice.md)
  The document picker moves a local file outside the app’s sandbox and provides access to it as an external file.
### Initializers
- [init?(rawValue: UInt)](uidocumentpickermode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var shouldShowFileExtensions: Bool](uidocumentpickerviewcontroller/shouldshowfileextensions.md)
  A Boolean value that determines whether the browser always shows file extensions.
- [var documentPickerMode: UIDocumentPickerMode](uidocumentpickerviewcontroller/documentpickermode.md)
  The type of file transfer operation that the document picker uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickermode)*