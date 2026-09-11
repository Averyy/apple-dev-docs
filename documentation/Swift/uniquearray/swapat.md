# swapAt(_:_:)

**Framework**: Swift  
**Kind**: method

Exchanges the values at the specified indices of the array.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
mutating func swapAt(_ i: Int, _ j: Int)
```

#### Discussion

Both parameters must be valid indices of the array and not equal to endIndex. Passing the same index as both `i` and `j` has no effect.

> **Note**: O(1)

## Parameters

- `i`: The index of the first value to swap.
- `j`: The index of the second valud to swap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/swapat(_:_:))*