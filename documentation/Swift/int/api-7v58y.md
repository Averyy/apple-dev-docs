# >=(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.

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
static func >= <Other>(lhs: Self, rhs: Other) -> Bool where Other : BinaryInteger
```

#### Discussion

You can compare instances of any `BinaryInteger` types using the greater-than-or-equal-to operator (`>=`), even if the two instances are of different types.

## Parameters

- `lhs`: An integer to compare.
- `rhs`: Another integer to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/_=(_:_:)-7v58y)*