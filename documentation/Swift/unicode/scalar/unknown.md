# <(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.

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
static func < (lhs: Unicode.Scalar, rhs: Unicode.Scalar) -> Bool
```

#### Discussion

This function is the only requirement of the `Comparable` protocol. The remainder of the relational operator functions are implemented by the standard library for any type that conforms to `Comparable`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [static func == (Unicode.Scalar, Unicode.Scalar) -> Bool](unicode/scalar/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](unicode/scalar/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func <= (Self, Self) -> Bool](unicode/scalar/_=(_:_:)-13yar.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func > (Self, Self) -> Bool](unicode/scalar/_(_:_:)-1xeim.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func >= (Self, Self) -> Bool](unicode/scalar/_=(_:_:)-7oywq.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/_(_:_:))*