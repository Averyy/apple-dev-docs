# reset()

**Framework**: EventKit  
**Kind**: method

Returns this object to its saved state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func reset()
```

#### Discussion

This method updates all the properties of this object with the corresponding values in the event store. Any local changes that were not saved before invoking this method are lost. This method does nothing if the object was never saved.

## See Also

- [var hasChanges: Bool](ekobject/haschanges.md)
  Returns whether this object or any of the objects it contains has uncommitted changes.
- [var isNew: Bool](ekobject/isnew.md)
  A Boolean value that indicates whether this object has ever been saved.
- [func refresh() -> Bool](ekobject/refresh.md)
  Merges changes to this object with the latest saved values.
- [func rollback()](ekobject/rollback.md)
  Rolls back the property values of this object to its original state when it was first fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekobject/reset())*