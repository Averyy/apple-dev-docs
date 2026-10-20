# excludedCredentials

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

An array of excluded parameters for the credential.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var excludedCredentials: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor] { get set }
```

```objc
@property (nonatomic, copy) NSArray<ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor *> * excludedCredentials;
```

## See Also

### Getting the properties
- [var credentialParameters: [ASAuthorizationPublicKeyCredentialParameters]](./credentialparameters.md)
  An array of parameters for the credential.
- [var residentKeyPreference: ASAuthorizationPublicKeyCredentialResidentKeyPreference](./residentkeypreference.md)
  The preference that indicates where the resident key resides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialregistrationrequest/excludedcredentials)*