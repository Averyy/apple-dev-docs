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
static func == (lhs: ClosedRange<Bound>, rhs: ClosedRange<Bound>) -> Bool
```

#### Discussion

Two ranges are equal when they have the same lower and upper bounds.

```swift
let x = 5...15
print(x == 5...15)
// Prints "true"
print(x == 10...20)
// Prints "false"
```

## Parameters

- `lhs`: A range to compare.
- `rhs`: Another range to compare.

## See Also

- [static func != (Self, Self) -> Bool](closedrange/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func overlaps(Range<Bound>) -> Bool](closedrange/overlaps(_:)-947dt.md)
  Returns a Boolean value indicating whether this range and the given range contain an element in common.
- [func overlaps(ClosedRange<Bound>) -> Bool](closedrange/overlaps(_:)-7dfep.md)
  Returns a Boolean value indicating whether this range and the given closed range contain an element in common.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/closedrange/==(_:_:))*