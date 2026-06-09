# DocumentConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The configuration of a document in a [`DocumentGroup`](documentgroup.md).

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct DocumentConfiguration
```

## Topics

### Getting configuration values
- [var fileURL: URL?](documentconfiguration/fileurl.md)
  A URL of an open document.
- [var isEditable: Bool](documentconfiguration/iseditable.md)
  A Boolean value that indicates whether you can edit the document.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var documentConfiguration: DocumentConfiguration?](environmentvalues/documentconfiguration.md)
  The configuration of a document in a [`DocumentGroup`](documentgroup.md).
- [var undoManager: UndoManager?](environmentvalues/undomanager.md)
  The undo manager used to register a view’s undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentconfiguration)*