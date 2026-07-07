# JPKIPassContents.UserIdentity.AuthenticationType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

Defines valid authentication types associated with the user identity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum AuthenticationType
```

#### Overview

Use of the systemBiometric authentication requires you to set the [`NSFaceIDUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSFaceIDUsageDescription) usage description.

## Topics

### Types of authentication
- [JPKIPassContents.UserIdentity.AuthenticationType.pin(_:)](jpkipasscontents/useridentity-swift.struct/authenticationtype/pin(_:).md)
  The PIN associated with the user identity.
- [JPKIPassContents.UserIdentity.AuthenticationType.systemBiometric](jpkipasscontents/useridentity-swift.struct/authenticationtype/systembiometric.md)
  Authentication using biometric information.

## See Also

- [let userIdentity: JPKIPassContents.UserIdentity?](jpkipasscontents/useridentity-swift.property.md)
  Allows for access to the user identity, if present in the JPKI applet.
- [func changePIN(from: String, to: String) async throws](jpkipasscontents/useridentity-swift.struct/changepin(from:to:).md)
  A function that allows for the change of the PIN associated with the user identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/useridentity-swift.struct/authenticationtype)*