# rollback()

**Framework**: SwiftData  
**Kind**: method

Discards pending inserts and deletes, restores changed models to their most recent committed state, and empties the undo stack.

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
func rollback()
```

## See Also

- [var autosaveEnabled: Bool](modelcontext/autosaveenabled.md)
  A Boolean value that indicates whether the context should automatically save any pending changes when certain events occur.
- [func save() throws](modelcontext/save.md)
  Writes any pending inserts, changes, and deletes to the persistent storage.
- [func transaction(block: () throws -> Void) throws](modelcontext/transaction(block:).md)
  Runs the provided closure, and once it finishes, writes any pending inserts, changes, and deletes to the persistent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/rollback())*