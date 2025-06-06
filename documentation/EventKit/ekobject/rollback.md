# rollback()

**Framework**: EventKit  
**Kind**: method

Rolls back the property values of this object to its original state when it was first fetched.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func rollback()
```

#### Discussion

Any local changes to this object are lost when invoking this method. This method does not re-fetch property values from the event store. This method does nothing if the object was never changed.

## See Also

- [var hasChanges: Bool](ekobject/haschanges.md)
  Returns whether this object or any of the objects it contains has uncommitted changes.
- [var isNew: Bool](ekobject/isnew.md)
  A Boolean value that indicates whether this object has ever been saved.
- [func refresh() -> Bool](ekobject/refresh.md)
  Merges changes to this object with the latest saved values.
- [func reset()](ekobject/reset.md)
  Returns this object to its saved state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekobject/rollback())*