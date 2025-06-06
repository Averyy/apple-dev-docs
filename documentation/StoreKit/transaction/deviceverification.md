# deviceVerification

**Framework**: StoreKit  
**Kind**: property

The device verification value you use to verify whether the transaction belongs to the device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let deviceVerification: Data
```

#### Discussion

Whenever StoreKit returns a verified transaction, the transaction is valid for the device. To perform your own verification, compute the device verification hash as follows:

1. Get the lowercase UUID string representation of [`deviceVerificationNonce`](transaction/deviceverificationnonce.md).
2. Append the lowercase UUID string representation of [`deviceVerificationID`](appstore/deviceverificationid.md).
3. Compute the SHA-384 hash of the ASCII representation of the combined string.

Compare the value you calculated to the transaction’s [`deviceVerification`](transaction/deviceverification.md) value. If the values match, the transaction is valid for the device. Otherwise, the verification fails and the transaction isn’t valid for the device. The following example illustrates validating a transaction.

```swift
guard let deviceVerificationUUID = AppStore.deviceVerificationID else {
    print("Device Verification ID isn't available.")
    return
}

// Assemble the values to hash.
let deviceVerificationIDString = deviceVerificationUUID.uuidString.lowercased()
let nonceString = transaction.deviceVerificationNonce.uuidString.lowercased()
let hashTargetString = nonceString.appending(deviceVerificationIDString)

// Compute the hash.
let hashTargetData = Data(hashTargetString.utf8)
let digest = SHA384.hash(data: hashTargetData)
let digestData = Data(digest)
if digestData == transaction.deviceVerification {
    print("Transaction is valid for this device.")
} else {
    print("Transaction isn't valid for this device.")
}
```

## See Also

- [let deviceVerificationNonce: UUID](transaction/deviceverificationnonce.md)
  The UUID for computing the device verification value.
- [let signedDate: Date](transaction/signeddate.md)
  The date that the App Store signed the JWS transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/deviceverification)*