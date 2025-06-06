# !=(_:_:)

**Framework**: Combine  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func != (lhs: Self, rhs: Self) -> Bool
```

#### Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b` implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any type that conforms to `Equatable`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [static func == (Publishers.CombineLatest3<A, B, C>, Publishers.CombineLatest3<A, B, C>) -> Bool](publishers/combinelatest3/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/combinelatest3/!=(_:_:))*