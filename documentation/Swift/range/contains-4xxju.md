# contains(_:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether the given range is contained within this range.

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
func contains(_ other: Range<Bound>) -> Bool
```

#### Return Value

`true` if `other` is empty or wholly contained within this range; otherwise, `false`.

#### Discussion

The given range is contained within this range if its bounds are equal to or within the bounds of this range.

```swift
let range = 0..<10
range.contains(2..<5)        // true
range.contains(2..<10)       // true
range.contains(2..<12)       // false
```

Additionally, passing any empty range as `other` results in the value `true`, even if the empty range’s bounds are outside the bounds of this range.

```swift
let emptyRange = 3..<3
emptyRange.contains(3..<3)   // true
emptyRange.contains(5..<5)   // true
```

> **Note**: O(1)

## Parameters

- `other`: A range to check for containment within this range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/contains(_:)-4xxju)*