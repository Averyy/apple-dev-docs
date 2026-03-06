# ==(_:_:)

**Framework**: Swift  
**Kind**: op  
**Required**: Yes

Returns a Boolean value indicating whether two values are equal.

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
static func == (lhs: Self, rhs: Self) -> Bool
```

#### Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b` implies that `a != b` is `false`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [static func != (Self, Self) -> Bool](equatable/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/equatable/==(_:_:))*