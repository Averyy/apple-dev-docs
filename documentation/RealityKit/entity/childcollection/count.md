# count

**Framework**: RealityKit  
**Kind**: property

The number of elements in the collection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var count: Int { get }
```

#### Discussion

To check whether a collection is empty, use its `isEmpty` property instead of comparing `count` to zero. Unless the collection guarantees random-access performance, calculating `count` can be an O() operation.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

## See Also

- [var isEmpty: Bool](entity/childcollection/isempty.md)
  A Boolean value indicating whether the collection is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/count)*