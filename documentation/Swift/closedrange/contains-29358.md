# contains(_:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether the given range is contained within this closed range.

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

`true` if `other` is empty or wholly contained within this closed range; otherwise, `false`.

#### Discussion

The given range is contained within this closed range if the elements of the range are all contained within this closed range.

```swift
let range = 0...10
range.contains(5..<7)     // true
range.contains(5..<10)    // true
range.contains(5..<12)    // false

// Note that `5..<11` contains 5, 6, 7, 8, 9, and 10.
range.contains(5..<11)    // true
```

Additionally, passing any empty range as `other` results in the value `true`, even if the empty range’s bounds are outside the bounds of this closed range.

```swift
range.contains(3..<3)     // true
range.contains(20..<20)   // true
```

> **Note**: O(1)

O(1)

## Parameters

- `other`: A range to check for containment within this closed   range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/closedrange/contains(_:)-29358)*