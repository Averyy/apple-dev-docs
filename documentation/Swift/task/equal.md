# ==(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether two values are equal.

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
static func == (lhs: Task<Success, Failure>, rhs: Task<Success, Failure>) -> Bool
```

#### Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b` implies that `a != b` is `false`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [static func != (borrowing Self, borrowing Self) -> Bool](task/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [var hashValue: Int](task/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](task/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/==(_:_:))*