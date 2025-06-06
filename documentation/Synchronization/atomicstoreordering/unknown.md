# ==(_:_:)

**Framework**: Synchronization  
**Kind**: op

Returns a Boolean value indicating whether two values are equal.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func == (left: AtomicStoreOrdering, right: AtomicStoreOrdering) -> Bool
```

#### Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b` implies that `a != b` is `false`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomicstoreordering/==(_:_:))*