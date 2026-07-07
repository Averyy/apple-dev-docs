# signedDate

**Framework**: StoreKit  
**Kind**: property

The date that the App Store signed the JWS transaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let signedDate: Date
```

#### Discussion

Use the [`signedDate`](transaction/signeddate.md) to verify whether the certificate used to sign the transaction was valid when the App Store signed the transaction.

## See Also

- [let deviceVerification: Data](transaction/deviceverification.md)
  The device verification value you use to verify whether the transaction belongs to the device.
- [let deviceVerificationNonce: UUID](transaction/deviceverificationnonce.md)
  The UUID for computing the device verification value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/signeddate)*