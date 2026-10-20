# undoManager

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The undo manager used to register a view’s undo operations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var undoManager: UndoManager? { get }
```

#### Discussion

This value is `nil` when the environment represents a context that doesn’t support undo and redo operations. You can skip registration of an undo operation when this value is `nil`.

## See Also

### Accessing document configuration
- [var documentConfiguration: DocumentConfiguration?](./documentconfiguration.md)
  The configuration of a document in a [`DocumentGroup`](../documentgroup.md).
- [struct DocumentConfiguration](../documentconfiguration.md)
  The configuration of a document in a [`DocumentGroup`](../documentgroup.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/undomanager)*