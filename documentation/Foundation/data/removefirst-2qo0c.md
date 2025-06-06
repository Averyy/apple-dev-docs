# removeFirst(_:)

**Framework**: Foundation  
**Kind**: method

Removes the specified number of elements from the beginning of the collection.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func removeFirst(_ k: Int)
```

#### Discussion

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the specified number of elements.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the specified number of elements.

## Parameters

- `k`: The number of elements to remove.   must be greater than   or equal to zero, and must be less than or equal to the number of   elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/removefirst(_:)-2qo0c)*