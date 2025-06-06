# autosaveEnabled

**Framework**: SwiftData  
**Kind**: property

A Boolean value that indicates whether the context should automatically save any pending changes when certain events occur.

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
var autosaveEnabled: Bool { get set }
```

## Mentions

- [Preserving your app’s model data across launches](preserving-your-apps-model-data-across-launches.md)

#### Discussion

When `true`, the context calls [`save()`](modelcontext/save().md) after you make changes to any inserted or registered models. The context also calls `save()` at various times during the lifecycle of windows, scenes, views, and sheets.

The default value is `false`. SwiftData automatically sets this property to `true` for the model container’s [`mainContext`](modelcontainer/maincontext.md).

## See Also

- [func save() throws](modelcontext/save.md)
  Writes any pending inserts, changes, and deletes to the persistent storage.
- [func transaction(block: () throws -> Void) throws](modelcontext/transaction(block:).md)
  Runs the provided closure, and once it finishes, writes any pending inserts, changes, and deletes to the persistent storage.
- [func rollback()](modelcontext/rollback.md)
  Discards pending inserts and deletes, restores changed models to their most recent committed state, and empties the undo stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/autosaveenabled)*