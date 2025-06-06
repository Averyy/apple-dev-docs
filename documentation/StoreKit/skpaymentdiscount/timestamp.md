# timestamp

**Framework**: StoreKit  
**Kind**: property

The date and time of the signature’s creation in milliseconds, formatted in Unix epoch time.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
@NSCopying
var timestamp: NSNumber { get }
```

#### Discussion

The [`timestamp`](skpaymentdiscount/timestamp.md) keeps the payment discount active for 24 hours.

## See Also

- [var nonce: UUID](skpaymentdiscount/nonce.md)
  A universally unique ID (UUID) value that you define.
- [var signature: String](skpaymentdiscount/signature.md)
  A string representing the properties of a specific promotional offer, cryptographically signed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentdiscount/timestamp)*