# ..<(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a half-open range that contains its lower bound but not its upper bound.

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
static func ..< (minimum: Self, maximum: Self) -> Range<Self>
```

#### Discussion

Use the half-open range operator (`..<`) to create a range of any type that conforms to the `Comparable` protocol. This example creates a `Range<Double>` from zero up to, but not including, 5.0.

```swift
let lessThanFive = 0.0..<5.0
print(lessThanFive.contains(3.14))  // Prints "true"
print(lessThanFive.contains(5.0))   // Prints "false"
```

> **Note**: `minimum <= maximum`.

## Parameters

- `minimum`: The lower bound for the range.
- `maximum`: The upper bound for the range.

## See Also

- [struct Range](range.md)
  A half-open interval from a lower bound up to, but not including, an upper bound.
- [struct RangeSet](rangeset.md)
  A set of values of any comparable type, represented by ranges.
- [static func ... (Self, Self) -> ClosedRange<Self>](comparable/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [struct ClosedRange](closedrange.md)
  An interval from a lower bound up to, and including, an upper bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/comparable/'.._(_:_:))*