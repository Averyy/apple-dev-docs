# refresh()

**Framework**: EventKit  
**Kind**: method

Merges changes to this object with the latest saved values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func refresh() -> Bool
```

#### Return Value

If the operation is successful, [`true`](https://developer.apple.com/documentation/swift/true); if the object was deleted in the event store, [`false`](https://developer.apple.com/documentation/swift/false). If this method returns [`false`](https://developer.apple.com/documentation/swift/false), the object should be released.

#### Discussion

This method merges the local changes to properties of this object with the latest values in the event store. This method updates only properties that have not been modified locally, so you do not lose any changes by invoking this method. You can also use this method to see whether an object was deleted from the event store.

## See Also

- [var hasChanges: Bool](ekobject/haschanges.md)
  Returns whether this object or any of the objects it contains has uncommitted changes.
- [var isNew: Bool](ekobject/isnew.md)
  A Boolean value that indicates whether this object has ever been saved.
- [func reset()](ekobject/reset.md)
  Returns this object to its saved state.
- [func rollback()](ekobject/rollback.md)
  Rolls back the property values of this object to its original state when it was first fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekobject/refresh())*