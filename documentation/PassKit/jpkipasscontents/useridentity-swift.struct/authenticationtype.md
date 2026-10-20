# JPKIPassContents.UserIdentity.AuthenticationType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

Defines valid authentication types associated with the user identity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum AuthenticationType
```

#### Overview

Use of the systemBiometric authentication requires you to set the [`NSFaceIDUsageDescription`](../../../BundleResources/information-property-list/nsfaceidusagedescription.md) usage description.

## Topics

### Types of authentication
- [JPKIPassContents.UserIdentity.AuthenticationType.pin(_:)](./authenticationtype/pin%28_%29.md)
  The PIN associated with the user identity.
- [JPKIPassContents.UserIdentity.AuthenticationType.systemBiometric](./authenticationtype/systembiometric.md)
  Authentication using biometric information.

## See Also

### Identifying the pass user
- [let userIdentity: JPKIPassContents.UserIdentity?](../useridentity-swift.property.md)
  Allows for access to the user identity, if present in the JPKI applet.
- [func changePIN(from: String, to: String) async throws](./changepin%28from,to%29.md)
  A function that allows for the change of the PIN associated with the user identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/useridentity-swift.struct/authenticationtype)*