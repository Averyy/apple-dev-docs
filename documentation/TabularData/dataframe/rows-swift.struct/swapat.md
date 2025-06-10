# swapAt(_:_:)

**Framework**: TabularData  
**Kind**: method

Exchanges the values at the specified indices of the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
mutating func swapAt(_ i: Self.Index, _ j: Self.Index)
```

#### Discussion

Both parameters must be valid indices of the collection that are not equal to `endIndex`. Calling `swapAt(_:_:)` with the same index as both `i` and `j` has no effect.

> **Note**: O(1)

## Parameters

- `i`: The index of the first value to swap.
- `j`: The index of the second value to swap.

## See Also

- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](dataframe/rows-swift.struct/partition(by:)-jit0.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/rows-swift.struct/swapat(_:_:))*