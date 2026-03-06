# !=(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

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
static func != (lhs: Self, rhs: Self) -> Bool
```

#### Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b` implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any type that conforms to `Equatable`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [static func == (Task<Success, Failure>, Task<Success, Failure>) -> Bool](task/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [var hashValue: Int](task/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](task/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/!=(_:_:))*