# contains(_:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether the given closed range is contained within this range.

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
func contains(_ other: ClosedRange<Bound>) -> Bool
```

#### Return Value

`true` if `other` is wholly contained within this range; otherwise, `false`.

#### Discussion

The given closed range is contained within this range if its bounds are contained within this range. If this range is empty, it cannot contain a closed range, since closed ranges by definition contain their boundaries.

```swift
let range = 0..<10
range.contains(2...5)        // true
range.contains(2...10)       // false
range.contains(2...12)       // false

let emptyRange = 3..<3
emptyRange.contains(3...3)   // false
```

> **Note**: O(1)

## Parameters

- `other`: A closed range to check for containment within this   range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/contains(_:)-680jp)*