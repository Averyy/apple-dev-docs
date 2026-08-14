# canInsert

**Framework**: AppKit  
**Kind**: property

Returns a Boolean value that indicates whether an object can be inserted into the receiver’s content collection.

**Availability**:
- macOS ?+

## Declaration

```swift
var canInsert: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if an object can be inserted into the receiver’s content collection, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The result of this method can be used by a binding to enable user interface items.

This property is observable using key-value observing.

## See Also

- [func insert(Any?)](nsarraycontroller/insert(_:).md)
  Creates a new object and inserts it into the receiver’s content array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/caninsert)*