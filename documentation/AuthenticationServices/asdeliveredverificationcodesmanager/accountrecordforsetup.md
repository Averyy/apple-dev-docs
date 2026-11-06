# ASDeliveredVerificationCodesManager.AccountRecordForSetUp

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

An account that a client would like the user to be able to receive verification codes for.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct AccountRecordForSetUp
```

## Topics

### Initializers
- [init(contactMethod: ASDeliveredVerificationCodesManager.AccountRecordForSetUp.ContactMethod, user: String?, serviceIdentifier: ASCredentialServiceIdentifier)](./accountrecordforsetup/init%28contactmethod,user,serviceidentifier%29.md)
### Instance Properties
- [var contactMethod: ASDeliveredVerificationCodesManager.AccountRecordForSetUp.ContactMethod](./accountrecordforsetup/contactmethod-swift.property.md)
  How an account may receive verification codes.
- [var serviceIdentifier: ASCredentialServiceIdentifier](./accountrecordforsetup/serviceidentifier.md)
  The service the account signs in to.
- [var user: String?](./accountrecordforsetup/user.md)
  The user identifier at the service.
### Enumerations
- [ASDeliveredVerificationCodesManager.AccountRecordForSetUp.ContactMethod](./accountrecordforsetup/contactmethod-swift.enum.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asdeliveredverificationcodesmanager/accountrecordforsetup)*