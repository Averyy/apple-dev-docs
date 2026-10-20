# payment

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

A pass that represents a credit or debit card

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.12+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: Use [`PKPassType.secureElement`](./secureelement.md) instead.

## Declaration

```swift
static var payment: PKPassType { get }
```

```c
PKPassTypePayment
```

## See Also

### Pass types
- [PKPassType.any](./any.md)
  A nonspecific pass type.
- [PKPassType.barcode](./barcode.md)
  A pass that represents a barcode.
- [PKPassType.secureElement](./secureelement.md)
  A pass that represents a credential that the device stores in the Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasstype/payment)*