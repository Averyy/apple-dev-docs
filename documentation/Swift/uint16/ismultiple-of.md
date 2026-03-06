# isMultiple(of:)

**Framework**: Swift  
**Kind**: method

Returns `true` if this value is a multiple of the given value, and `false` otherwise.

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
func isMultiple(of other: Self) -> Bool
```

#### Discussion

For two integers *a* and *b*, *a* is a multiple of *b* if there exists a third integer *q* such that *a = q*b*. For example, *6* is a multiple of *3* because *6 = 2*3*. Zero is a multiple of everything because *0 = 0*x* for any integer *x*.

Two edge cases are worth particular attention:

- `x.isMultiple(of: 0)` is `true` if `x` is zero and `false` otherwise.
- `T.min.isMultiple(of: -1)` is `true` for signed integer `T`, even though the quotient `T.min / -1` isn’t representable in type `T`.

## Parameters

- `other`: The value to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint16/ismultiple(of:))*