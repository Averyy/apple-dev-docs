# isNew

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isNew) BOOL new;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the object hasn’t been saved; otherwise, [`false`](../../Swift/false.md).

## See Also

### Saving and Restoring State
- [var hasChanges: Bool](./haschanges.md)
  Returns whether this object or any of the objects it contains has uncommitted changes.
- [func refresh() -> Bool](./refresh%28%29.md)
  Merges changes to this object with the latest saved values.
- [func reset()](./reset%28%29.md)
  Returns this object to its saved state.
- [func rollback()](./rollback%28%29.md)
  Rolls back the property values of this object to its original state when it was first fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekobject/isnew)*