# isEqualToBalance:

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether two pass balance objects contain the same values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
- (BOOL) isEqualToBalance:(PKStoredValuePassBalance *) balance;
```

## Return Value

True when the two balance objects contain the same settings, false otherwise.

## Parameters

- `balance`: A pass balance object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkstoredvaluepassbalance/isequaltobalance:)*