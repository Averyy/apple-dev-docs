# refresh()

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) refresh;
```

## Return Value

If the operation is successful, [`true`](../../Swift/true.md); if the object was deleted in the event store, [`false`](../../Swift/false.md). If this method returns [`false`](../../Swift/false.md), the object should be released.

## Discussion

This method merges the local changes to properties of this object with the latest values in the event store. This method updates only properties that have not been modified locally, so you do not lose any changes by invoking this method. You can also use this method to see whether an object was deleted from the event store.

## See Also

### Saving and Restoring State
- [var hasChanges: Bool](./haschanges.md)
  Returns whether this object or any of the objects it contains has uncommitted changes.
- [var isNew: Bool](./isnew.md)
  A Boolean value that indicates whether this object has ever been saved.
- [func reset()](./reset%28%29.md)
  Returns this object to its saved state.
- [func rollback()](./rollback%28%29.md)
  Rolls back the property values of this object to its original state when it was first fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekobject/refresh())*