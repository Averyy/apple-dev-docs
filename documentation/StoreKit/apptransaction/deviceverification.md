# deviceVerification

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The device verification value to use to verify whether the app transaction belongs to the device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let deviceVerification: Data
```

## Discussion

For more information, see [`deviceVerificationID`](../appstore/deviceverificationid.md).

## See Also

### Verifying the app transaction
- [let deviceVerificationNonce: UUID](./deviceverificationnonce.md)
  The UUID used to compute the device verification value.
- [let signedDate: Date](./signeddate.md)
  The date that the App Store signed the JWS app transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/apptransaction/deviceverification)*