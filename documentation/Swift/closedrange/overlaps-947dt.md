# overlaps(_:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether this range and the given range contain an element in common.

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
func overlaps(_ other: Range<Bound>) -> Bool
```

#### Return Value

`true` if this range and `other` have at least one element in common; otherwise, `false`.

#### Discussion

This example shows two overlapping ranges:

```swift
let x: Range = 0...20
print(x.overlaps(10..<1000))
// Prints "true"
```

Because a closed range includes its upper bound, the ranges in the following example overlap:

```swift
let y = 20..<30
print(x.overlaps(y))
// Prints "true"
```

## Parameters

- `other`: A range to check for elements in common.

## See Also

- [static func == (ClosedRange<Bound>, ClosedRange<Bound>) -> Bool](closedrange/==(_:_:).md)
  Returns a Boolean value indicating whether two ranges are equal.
- [static func != (Self, Self) -> Bool](closedrange/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func overlaps(ClosedRange<Bound>) -> Bool](closedrange/overlaps(_:)-7dfep.md)
  Returns a Boolean value indicating whether this range and the given closed range contain an element in common.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/closedrange/overlaps(_:)-947dt)*