# UIDocumentPickerMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Modes that define the type of file transfer operation that the document picker uses.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`UIDocumentPickerViewController`](./uidocumentpickerviewcontroller.md) initializers instead.

## Declaration

```swift
enum UIDocumentPickerMode
```

```c
enum UIDocumentPickerMode : NSUInteger;
```

## Topics

### Constants
- [UIDocumentPickerMode.import](./uidocumentpickermode/import.md)
  The document picker imports a file from outside the app’s sandbox.
- [UIDocumentPickerMode.open](./uidocumentpickermode/open.md)
  The document picker opens an external file outside the app’s sandbox.
- [UIDocumentPickerMode.exportToService](./uidocumentpickermode/exporttoservice.md)
  The document picker exports a local file to a destination outside the app’s sandbox.
- [UIDocumentPickerMode.moveToService](./uidocumentpickermode/movetoservice.md)
  The document picker moves a local file outside the app’s sandbox and provides access to it as an external file.
### Initializers
- [init?(rawValue: UInt)](./uidocumentpickermode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickermode)*