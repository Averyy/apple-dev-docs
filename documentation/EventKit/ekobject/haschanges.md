# hasChanges

**Framework**: EventKit  
**Kind**: property

Returns whether this object or any of the objects it contains has uncommitted changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var hasChanges: Bool { get }
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if there are uncommitted changes; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isNew: Bool](ekobject/isnew.md)
  A Boolean value that indicates whether this object has ever been saved.
- [func refresh() -> Bool](ekobject/refresh.md)
  Merges changes to this object with the latest saved values.
- [func reset()](ekobject/reset.md)
  Returns this object to its saved state.
- [func rollback()](ekobject/rollback.md)
  Rolls back the property values of this object to its original state when it was first fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekobject/haschanges)*