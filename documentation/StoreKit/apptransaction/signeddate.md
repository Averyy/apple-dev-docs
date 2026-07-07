# signedDate

**Framework**: StoreKit  
**Kind**: property

The date that the App Store signed the JWS app transaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let signedDate: Date
```

#### Discussion

Use the [`signedDate`](apptransaction/signeddate.md) to verify whether the certificate used to sign the app transaction was valid when the App Store signed the transaction.

## See Also

- [let deviceVerification: Data](apptransaction/deviceverification.md)
  The device verification value to use to verify whether the app transaction belongs to the device.
- [let deviceVerificationNonce: UUID](apptransaction/deviceverificationnonce.md)
  The UUID used to compute the device verification value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/apptransaction/signeddate)*