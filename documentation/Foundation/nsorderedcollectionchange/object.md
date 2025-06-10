# object

**Framework**: Foundation  
**Kind**: property

An object the change inserts or removes.

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
var object: Any? { get }
```

## See Also

- [var changeType: NSCollectionChangeType](nsorderedcollectionchange/changetype.md)
  The type of change.
- [var index: Int](nsorderedcollectionchange/index.md)
  The index location of the change.
- [var associatedIndex: Int](nsorderedcollectionchange/associatedindex.md)
  When this property is set to a value other than [`NSNotFound`](nsnotfound-9t5v2.md), the receiver is one half of a move, and this value is the index of the change’s counterpart of the opposite type in the diff.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectionchange/object)*