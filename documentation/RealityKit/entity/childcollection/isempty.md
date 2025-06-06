# isEmpty

**Framework**: RealityKit  
**Kind**: property

A Boolean value indicating whether the collection is empty.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var isEmpty: Bool { get }
```

#### Discussion

When you need to check whether your collection is empty, use the `isEmpty` property instead of checking that the `count` property is equal to zero. For collections that don’t conform to `RandomAccessCollection`, accessing the `count` property iterates through the elements of the collection.

```None
let horseName = "Silver"
if horseName.isEmpty {
    print("My horse has no name.")
} else {
    print("Hi ho, \(horseName)!")
}
// Prints "Hi ho, Silver!")
```

> **Note**: O(1)

O(1)

## See Also

- [var count: Int](entity/childcollection/count.md)
  The number of elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/isempty)*