# swapAt(_:_:)

**Framework**: Swift  
**Kind**: method

Exchanges the values at the specified indices of the array.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
mutating func swapAt(_ i: InlineArray<count, Element>.Index, _ j: InlineArray<count, Element>.Index)
```

#### Discussion

Both parameters must be valid indices of the array and not equal to `endIndex`. Passing the same index as both `i` and `j` has no effect.

> **Note**: O(1)

## Parameters

- `i`: The index of the first value to swap.
- `j`: The index of the second value to swap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/inlinearray/swapat(_:_:))*