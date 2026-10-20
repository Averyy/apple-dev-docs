# JPKIPassContents.UserIdentity.AuthenticationType.systemBiometric

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

Authentication using biometric information.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
case systemBiometric
```

#### Discussion

Use of the systemBiometric authentication requires you to set the [`NSFaceIDUsageDescription`](../../../../BundleResources/information-property-list/nsfaceidusagedescription.md) usage description.

## See Also

### Types of authentication
- [JPKIPassContents.UserIdentity.AuthenticationType.pin(_:)](./pin%28_%29.md)
  The PIN associated with the user identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/useridentity-swift.struct/authenticationtype/systembiometric)*