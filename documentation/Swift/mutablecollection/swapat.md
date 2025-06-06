# swapAt(_:_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Exchanges the values at the specified indices of the collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func swapAt(_ i: Self.Index, _ j: Self.Index)
```

#### Discussion

Both parameters must be valid indices of the collection and not equal to `endIndex`. Passing the same index as both `i` and `j` has no effect.

> **Note**: O(1)

O(1)

## Parameters

- `i`: The index of the first value to swap.
- `j`: The index of the second value to swap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablecollection/swapat(_:_:))*