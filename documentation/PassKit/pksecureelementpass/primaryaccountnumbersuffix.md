# primaryAccountNumberSuffix

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A display-ready version of the primary account number.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var primaryAccountNumberSuffix: String { get }
```

#### Discussion

This property’s value is generally the last four or five digits of the primary account number, but can vary by issuer. The value isn’t related to [`primaryAccountIdentifier`](pksecureelementpass/primaryaccountidentifier.md).

## See Also

- [var primaryAccountIdentifier: String](pksecureelementpass/primaryaccountidentifier.md)
  An opaque value that identifies the primary account number that funds the pass’s transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksecureelementpass/primaryaccountnumbersuffix)*