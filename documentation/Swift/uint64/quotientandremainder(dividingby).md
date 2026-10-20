# quotientAndRemainder(dividingBy:)

**Framework**: Swift  
**Kind**: method

Returns the quotient and remainder of this value divided by the given value.

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
func quotientAndRemainder(dividingBy rhs: Self) -> (quotient: Self, remainder: Self)
```

#### Return Value

A tuple containing the quotient and remainder of this value divided by `rhs`. The remainder has the same sign as `lhs`.

#### Discussion

Use this method to calculate the quotient and remainder of a division at the same time.

```swift
let x = 1_000_000
let (q, r) = x.quotientAndRemainder(dividingBy: 933)
// q == 1071
// r == 757
```

## Parameters

- `rhs`: The value to divide this value by.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint64/quotientandremainder(dividingby:))*