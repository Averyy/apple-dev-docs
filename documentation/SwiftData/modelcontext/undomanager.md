# undoManager

**Framework**: SwiftData  
**Kind**: property

The object that provides undo support for the context.

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
var undoManager: UndoManager? { get set }
```

#### Discussion

Assign an instance of [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) to this property to enable undo support for the context. The undo manager can be exclusive to the context, or an existing manager should you want to integrate this context’s undo operations with those of the rest of your app.

If the context does use an undo manager, improve performance by temporarily setting this property to `nil` when performing expensive operations, such as importing large numbers of models.

The default value is `nil`.

## See Also

- [func processPendingChanges()](modelcontext/processpendingchanges.md)
  Tells the undo manager to record any changes made to the context’s registered models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/undomanager)*