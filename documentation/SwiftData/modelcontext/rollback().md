# rollback()

**Framework**: SwiftData  
**Kind**: method  
**Role**: Instance Method

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

### Persisting unsaved changes
- [var autosaveEnabled: Bool](./autosaveenabled.md)
  A Boolean value that indicates whether the context should automatically save any pending changes when certain events occur.
- [func save() throws](./save%28%29.md)
  Writes any pending inserts, changes, and deletes to the persistent storage.
- [func transaction(block: () throws -> Void) throws](./transaction%28block%29.md)
  Runs the provided closure, and once it finishes, writes any pending inserts, changes, and deletes to the persistent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/rollback())*