# processPendingChanges()

**Framework**: SwiftData  
**Kind**: method

Tells the undo manager to record any changes made to the context’s registered models.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
func processPendingChanges()
```

#### Discussion

In AppKit-based applications, the system invokes this method at the end of each event loop. The framework may call it more frequently if it needs to coalesce your changes before continuing. You can also invoke it manually to coalesce any pending changes.

## See Also

- [var undoManager: UndoManager?](modelcontext/undomanager.md)
  The object that provides undo support for the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/processpendingchanges())*