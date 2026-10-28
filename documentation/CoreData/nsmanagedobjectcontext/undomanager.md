# undoManager

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The object that provides undo support for the context.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var undoManager: UndoManager? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSUndoManager * undoManager;
```

## Discussion

Enable undo support for a context by setting this property to an instance of [`UndoManager`](../../Foundation/undomanager.md). This can be an undo manager that’s exclusive to the context, or an existing undo manager if you want to integrate the context’s undo operations with those of the rest of your app.

If your context uses an undo manager, you can realize a performance benefit by temporarily setting this property to `nil` when performing expensive operations on that context, such as importing a large number of objects.

The default value is `nil`.

## See Also

### Undoing changes
- [func undo()](./undo%28%29.md)
  Sends an undo message to the context’s undo manager, asking it to reverse the latest uncommitted changes applied to objects in the object graph.
- [func redo()](./redo%28%29.md)
  Sends a redo message to the context’s undo manager, asking it to reverse the latest undo operation applied to objects in the object graph.
- [func reset()](./reset%28%29.md)
  Returns the context to its base state.
- [func rollback()](./rollback%28%29.md)
  Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their last committed values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/undomanager)*