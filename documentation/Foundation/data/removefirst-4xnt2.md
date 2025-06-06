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

Attempting to remove more elements than exist in the collection triggers a runtime error.

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the specified number of elements.

## Parameters

- `k`: The number of elements to remove from the collection.    must be greater than or equal to zero and must not exceed the   number of elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/removefirst(_:)-4xnt2)*