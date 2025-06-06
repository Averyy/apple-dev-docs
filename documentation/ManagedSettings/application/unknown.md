# !=(_:_:)

**Framework**: ManagedSettings  
**Kind**: op

Returns a Boolean value that indicates whether two values aren’t equal.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
static func != (lhs: Self, rhs: Self) -> Bool
```

#### Discussion

Inequality is the inverse of equality. For any values a and b, a != b implies that a == b is false.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [static func == (Application, Application) -> Bool](application/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [func hash(into: inout Hasher)](application/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](application/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/application/!=(_:_:))*