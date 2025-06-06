# !=(_:_:)

**Framework**: DeviceActivity  
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

Inequality is the inverse of equality. For any values a and b, a != b implies that a == b is false. This is the default implementation of the not-equal-to operator (!=) for any type that conforms to Equatable.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [var hashValue: Int](deviceactivityname/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](deviceactivityname/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityname/!=(_:_:))*