# canInsert

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value that indicates whether an object can be inserted into the receiver’s content collection.

**Availability**:
- macOS

## Declaration

```swift
var canInsert: Bool { get }
```

```objc
@property (readonly) BOOL canInsert;
```

#### Return Value

[`true`](../../Swift/true.md) if an object can be inserted into the receiver’s content collection, otherwise [`false`](../../Swift/false.md).

#### Discussion

The result of this method can be used by a binding to enable user interface items.

This property is observable using key-value observing.

## See Also

### Inserting
- [func insert(Any?)](./insert%28_%29.md)
  Creates a new object and inserts it into the receiver’s content array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/caninsert)*