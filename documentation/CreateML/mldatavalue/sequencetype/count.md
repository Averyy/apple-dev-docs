# count

**Framework**: Create ML  
**Kind**: property

The number of elements in the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var count: Int { get }
```

#### Discussion

To check whether a collection is empty, use its `isEmpty` property instead of comparing `count` to zero. Unless the collection guarantees random-access performance, calculating `count` can be an O() operation.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/sequencetype/count)*