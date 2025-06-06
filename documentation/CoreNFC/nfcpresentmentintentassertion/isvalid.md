# isValid

**Framework**: Core NFC  
**Kind**: property

A Boolean property that indicates whether the presentment intent assertion instance is still valid.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
final var isValid: Bool { get }
```

#### Discussion

This value is `true` when you first acquire a presentment intent assertion. It becomes `false` when any of the following occur:

- Your app goes into the background.
- The maximum presentment intention assertion duration expires.

## See Also

- [NFCPresentmentIntentAssertion.Error](nfcpresentmentintentassertion/error.md)
  An error type that indicates problems with the presentment intent assertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcpresentmentintentassertion/isvalid)*