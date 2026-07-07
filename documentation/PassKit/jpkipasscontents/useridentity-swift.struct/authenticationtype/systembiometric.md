# JPKIPassContents.UserIdentity.AuthenticationType.systemBiometric

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

Authentication using biometric information.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
case systemBiometric
```

#### Discussion

Use of the systemBiometric authentication requires you to set the [`NSFaceIDUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSFaceIDUsageDescription) usage description.

## See Also

- [JPKIPassContents.UserIdentity.AuthenticationType.pin(_:)](jpkipasscontents/useridentity-swift.struct/authenticationtype/pin(_:).md)
  The PIN associated with the user identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/useridentity-swift.struct/authenticationtype/systembiometric)*