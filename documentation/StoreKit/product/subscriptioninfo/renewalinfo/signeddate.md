# signedDate

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The date that the App Store signed the JWS renewal information.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let signedDate: Date
```

#### Discussion

Use the [`signedDate`](./signeddate.md) to verify whether the certificate used to sign the transaction was valid when the App Store signed the transaction.

## See Also

### Verifying subscription renewal information
- [let deviceVerification: Data](./deviceverification.md)
  The device verification value to use to verify whether the renewal information belongs to the device.
- [let deviceVerificationNonce: UUID](./deviceverificationnonce.md)
  The UUID to use to compute the device verification value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/signeddate)*