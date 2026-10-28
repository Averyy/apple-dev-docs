# reset()

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) reset;
```

## Discussion

This method updates all the properties of this object with the corresponding values in the event store. Any local changes that were not saved before invoking this method are lost. This method does nothing if the object was never saved.

## See Also

### Saving and Restoring State
- [var hasChanges: Bool](./haschanges.md)
  Returns whether this object or any of the objects it contains has uncommitted changes.
- [var isNew: Bool](./isnew.md)
  A Boolean value that indicates whether this object has ever been saved.
- [func refresh() -> Bool](./refresh%28%29.md)
  Merges changes to this object with the latest saved values.
- [func rollback()](./rollback%28%29.md)
  Rolls back the property values of this object to its original state when it was first fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekobject/reset())*