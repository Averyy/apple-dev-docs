# !=(_:_:)

**Framework**: ManagedSettings  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

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

- [static func == (WebContentSettings.FilterPolicy, WebContentSettings.FilterPolicy) -> Bool](webcontentsettings/filterpolicy/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webcontentsettings/filterpolicy/!=(_:_:))*