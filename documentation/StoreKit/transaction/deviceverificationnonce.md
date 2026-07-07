# deviceVerificationNonce

**Framework**: StoreKit  
**Kind**: property

The UUID for computing the device verification value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let deviceVerificationNonce: UUID
```

#### Discussion

Use the lowercased nonce when computing the [`deviceVerification`](transaction/deviceverification.md) value.

## See Also

- [let deviceVerification: Data](transaction/deviceverification.md)
  The device verification value you use to verify whether the transaction belongs to the device.
- [let signedDate: Date](transaction/signeddate.md)
  The date that the App Store signed the JWS transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/deviceverificationnonce)*