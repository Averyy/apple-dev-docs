# ...(_:)

**Framework**: Swift  
**Kind**: op

Returns a partial range extending upward from a lower bound.

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
static func ... (minimum: Self) -> PartialRangeFrom<Self>
```

#### Discussion

Use the postfix range operator (postfix `...`) to create a partial range of any type that conforms to the `Comparable` protocol. This example creates a `PartialRangeFrom<Double>` instance that includes any value greater than or equal to `5.0`.

```swift
let atLeastFive = 5.0...

atLeastFive.contains(4.0)     // false
atLeastFive.contains(5.0)     // true
atLeastFive.contains(6.0)     // true
```

You can use this type of partial range of a collection’s indices to represent the range from the partial range’s lower bound up to the end of the collection.

```swift
let numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[3...])
// Prints "[40, 50, 60, 70]"
```

> **Note**: `minimum` must compare equal to itself (i.e. cannot be NaN).

## Parameters

- `minimum`: The lower bound for the range.

## See Also

- [static func ... (Self) -> PartialRangeThrough<Self>](unicode/scalar/'...(_:)-7lhvp.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self, Self) -> ClosedRange<Self>](unicode/scalar/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [static func ..< (Self) -> PartialRangeUpTo<Self>](unicode/scalar/'.._(_:).md)
  Returns a partial range up to, but not including, its upper bound.
- [static func ..< (Self, Self) -> Range<Self>](unicode/scalar/'.._(_:_:).md)
  Returns a half-open range that contains its lower bound but not its upper bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/'...(_:)-9u9rz)*