# isNew

**Framework**: EventKit  
**Kind**: property

A Boolean value that indicates whether this object has ever been saved.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var isNew: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the object hasn’t been saved; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var hasChanges: Bool](ekobject/haschanges.md)
  Returns whether this object or any of the objects it contains has uncommitted changes.
- [func refresh() -> Bool](ekobject/refresh.md)
  Merges changes to this object with the latest saved values.
- [func reset()](ekobject/reset.md)
  Returns this object to its saved state.
- [func rollback()](ekobject/rollback.md)
  Rolls back the property values of this object to its original state when it was first fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekobject/isnew)*