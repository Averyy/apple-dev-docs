# deviceVerification

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The device verification value to use to verify whether the renewal information belongs to the device.

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
let deviceVerification: Data
```

#### Discussion

For more information, see [`deviceVerificationID`](../../../appstore/deviceverificationid.md).

## See Also

### Verifying subscription renewal information
- [let deviceVerificationNonce: UUID](./deviceverificationnonce.md)
  The UUID to use to compute the device verification value.
- [let signedDate: Date](./signeddate.md)
  The date that the App Store signed the JWS renewal information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/deviceverification)*