# makeSmartCard()

**Framework**: CryptoTokenKit  
**Kind**: method

Creates a new [`TKSmartCard`](tksmartcard.md) object representing the currently inserted Smart Card.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func makeSmartCard() -> TKSmartCard?
```

#### Return Value

A new [`TKSmartCard`](tksmartcard.md) object, or `nil` if no Smart Card is currently inserted.

#### Discussion

You can create multiple instances of `TKSmartCard` that represent the same Smart Card. Exclusivity of data transfer is handled by sessions on the individual `TKSmartCard` objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/makesmartcard())*