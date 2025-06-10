# removeLast(_:)

**Framework**: Foundation  
**Kind**: method

Removes the given number of elements from the end of the collection.

**Availability**:
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func removeLast(_ k: Int)
```

#### Discussion

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the number of elements to remove.

## Parameters

- `k`: The number of elements to remove.   must be greater   than or equal to zero, and must be less than or equal to the number of   elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/removelast(_:)-vle5)*