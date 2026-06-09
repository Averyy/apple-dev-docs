# ==(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether two ranges are equal.

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
static func == (lhs: Range<Bound>, rhs: Range<Bound>) -> Bool
```

#### Discussion

Two ranges are equal when they have the same lower and upper bounds. That requirement holds even for empty ranges.

```swift
let x = 5..<15
print(x == 5..<15)
// Prints "true"

let y = 5..<5
print(y == 15..<15)
// Prints "false"
```

## Parameters

- `lhs`: A range to compare.
- `rhs`: Another range to compare.

## See Also

- [static func != (borrowing Self, borrowing Self) -> Bool](range/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func overlaps(Range<Bound>) -> Bool](range/overlaps(_:)-7osha.md)
  Returns a Boolean value indicating whether this range and the given range contain an element in common.
- [func overlaps(ClosedRange<Bound>) -> Bool](range/overlaps(_:)-9fkb2.md)
  Returns a Boolean value indicating whether this range and the given closed range contain an element in common.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/==(_:_:))*