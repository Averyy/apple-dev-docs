# ...(_:)

**Framework**: Swift  
**Kind**: op

Returns a partial range up to, and including, its upper bound.

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
static func ... (maximum: Self) -> PartialRangeThrough<Self>
```

#### Discussion

Use the prefix closed range operator (prefix `...`) to create a partial range of any type that conforms to the `Comparable` protocol. This example creates a `PartialRangeThrough<Double>` instance that includes any value less than or equal to `5.0`.

```swift
let throughFive = ...5.0

throughFive.contains(4.0)     // true
throughFive.contains(5.0)     // true
throughFive.contains(6.0)     // false
```

You can use this type of partial range of a collection’s indices to represent the range from the start of the collection up to, and including, the partial range’s upper bound.

```swift
let numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[...3])
// Prints "[10, 20, 30, 40]"
```

> **Note**: `maximum` must compare equal to itself (i.e. cannot be NaN).

## Parameters

- `maximum`: The upper bound for the range.

## See Also

- [static func ... (Self, Self) -> ClosedRange<Self>](comparable/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [static func ... (Self) -> PartialRangeFrom<Self>](comparable/'...(_:)-6mvrh.md)
  Returns a partial range extending upward from a lower bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/comparable/'...(_:)-1quco)*