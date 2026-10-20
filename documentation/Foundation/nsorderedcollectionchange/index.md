# index

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The index location of the change.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var index: Int { get }
```

```objc
@property (readonly) NSUInteger index;
```

## See Also

### Accessing the Change
- [var changeType: NSCollectionChangeType](./changetype.md)
  The type of change.
- [var object: Any?](./object.md)
  An object the change inserts or removes.
- [var associatedIndex: Int](./associatedindex.md)
  When this property is set to a value other than [`NSNotFound`](../nsnotfound-9t5v2.md), the receiver is one half of a move, and this value is the index of the change’s counterpart of the opposite type in the diff.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectionchange/index)*