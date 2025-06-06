# save()

**Framework**: SwiftData  
**Kind**: method

Writes any pending inserts, changes, and deletes to the persistent storage.

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
func save() throws
```

## Mentions

- [Preserving your app’s model data across launches](preserving-your-apps-model-data-across-launches.md)

#### Discussion

> ❗ **Important**: Use the [`hasChanges`](modelcontext/haschanges.md) property to determine whether the context has uncommitted changes before invoking this method. Otherwise, SwiftData may perform unnecessary work.

Use the [`hasChanges`](modelcontext/haschanges.md) property to determine whether the context has uncommitted changes before invoking this method. Otherwise, SwiftData may perform unnecessary work.

## See Also

- [var autosaveEnabled: Bool](modelcontext/autosaveenabled.md)
  A Boolean value that indicates whether the context should automatically save any pending changes when certain events occur.
- [func transaction(block: () throws -> Void) throws](modelcontext/transaction(block:).md)
  Runs the provided closure, and once it finishes, writes any pending inserts, changes, and deletes to the persistent storage.
- [func rollback()](modelcontext/rollback.md)
  Discards pending inserts and deletes, restores changed models to their most recent committed state, and empties the undo stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/save())*