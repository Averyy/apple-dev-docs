# overlaps(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether this range and the given closed range contain an element in common.

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
func overlaps(_ other: ClosedRange<Bound>) -> Bool
```

Available when `Bound` conforms to `Comparable`.

## Return Value

`true` if this range and `other` have at least one element in common; otherwise, `false`.

## Discussion

This example shows two overlapping ranges:

```swift
let x: Range = 0...20
print(x.overlaps(10...1000))
// Prints "true"
```

## Parameters

- `other`: A range to check for elements in common.

## See Also

### Comparing Ranges
- [static func == (ClosedRange<Bound>, ClosedRange<Bound>) -> Bool](./eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two ranges are equal.
- [static func != (borrowing Self, borrowing Self) -> Bool](./noteq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are not equal.
- [func overlaps(Range<Bound>) -> Bool](./overlaps%28_%29-947dt.md)
  Returns a Boolean value indicating whether this range and the given range contain an element in common.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/closedrange/overlaps(_:)-7dfep)*