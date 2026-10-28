# ..<(_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Returns a partial range up to, but not including, its upper bound.

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
static func ..< (maximum: Self) -> PartialRangeUpTo<Self>
```

## Discussion

Use the prefix half-open range operator (prefix `..<`) to create a partial range of any type that conforms to the `Comparable` protocol. This example creates a `PartialRangeUpTo<Double>` instance that includes any value less than `5.0`.

```swift
let upToFive = ..<5.0

upToFive.contains(3.14)       // true
upToFive.contains(6.28)       // false
upToFive.contains(5.0)        // false
```

You can use this type of partial range of a collection’s indices to represent the range from the start of the collection up to, but not including, the partial range’s upper bound.

```swift
let numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[..<3])
// Prints "[10, 20, 30]"
```

> **Precondition**: `maximum` must compare equal to itself (i.e. cannot be NaN).

## Parameters

- `maximum`: The upper bound for the range.

## See Also

### Creating Ranges of Scalars
- [static func ... (Self) -> PartialRangeFrom<Self>](./dotdotdot%28_%29-9u9rz.md)
  Returns a partial range extending upward from a lower bound.
- [static func ... (Self) -> PartialRangeThrough<Self>](./dotdotdot%28_%29-7lhvp.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self, Self) -> ClosedRange<Self>](./dotdotdot%28_,_%29.md)
  Returns a closed range that contains both of its bounds.
- [static func ..< (Self, Self) -> Range<Self>](./dotdotop%28_,_%29.md)
  Returns a half-open range that contains its lower bound but not its upper bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/'.._(_:))*