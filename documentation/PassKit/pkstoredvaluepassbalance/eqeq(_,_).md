# ==(_:_:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: op  
**Role**: Operator

Returns a Boolean value that indicates whether two pass balance objects contain the same values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
static func == (lhs: PKStoredValuePassBalance, rhs: PKStoredValuePassBalance) -> Bool
```

## Return Value

[`true`](../../Swift/true.md) if the two stored-value pass balance objects are equal; otherwise, [`false`](../../Swift/false.md)

## Parameters

- `lhs`: A stored-value pass balance object to compare.
- `rhs`: Another stored-value pass balance object to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkstoredvaluepassbalance/==(_:_:))*