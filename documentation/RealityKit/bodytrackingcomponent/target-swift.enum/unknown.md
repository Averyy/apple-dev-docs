# !=(_:_:)

**Framework**: RealityKit  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+

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

- [static func == (BodyTrackingComponent.Target, BodyTrackingComponent.Target) -> Bool](bodytrackingcomponent/target-swift.enum/==(_:_:).md)
  Indicates whether two targets are equal.
- [func hash(into: inout Hasher)](bodytrackingcomponent/target-swift.enum/hash(into:).md)
  Hashes the essential components of the target by feeding them into the given hash function.
- [var hashValue: Int](bodytrackingcomponent/target-swift.enum/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bodytrackingcomponent/target-swift.enum/!=(_:_:))*