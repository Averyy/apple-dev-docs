# undoManager

**Framework**: AppKit  
**Kind**: property

The undo manager for this responder.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var undoManager: UndoManager? { get }
```

#### Discussion

The  `NSResponder` implementation simply invokes this property on the next responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/undomanager)*