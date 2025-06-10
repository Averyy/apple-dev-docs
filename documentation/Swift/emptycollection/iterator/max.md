# max()

**Framework**: Swift  
**Kind**: method

Returns the maximum element in the sequence.

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
@warn_unqualified_access
func max() -> Self.Element?
```

#### Return Value

The sequence’s maximum element. If the sequence has no elements, returns `nil`.

#### Discussion

This example finds the largest value in an array of height measurements.

```swift
let heights = [67.5, 65.7, 64.3, 61.1, 58.5, 60.3, 64.9]
let greatestHeight = heights.max()
print(greatestHeight)
// Prints "Optional(67.5)"
```

> **Note**: O(), where  is the length of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/emptycollection/iterator/max())*