# deviceVerificationNonce

**Framework**: StoreKit  
**Kind**: property

The UUID used to compute the device verification value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let deviceVerificationNonce: UUID
```

#### Discussion

For more information, see [`deviceVerificationID`](appstore/deviceverificationid.md).

## See Also

- [let deviceVerification: Data](apptransaction/deviceverification.md)
  The device verification value to use to verify whether the app transaction belongs to the device.
- [let signedDate: Date](apptransaction/signeddate.md)
  The date that the App Store signed the JWS app transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/apptransaction/deviceverificationnonce)*