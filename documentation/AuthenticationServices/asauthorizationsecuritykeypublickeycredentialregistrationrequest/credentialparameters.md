# credentialParameters

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

An array of parameters for the credential.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var credentialParameters: [ASAuthorizationPublicKeyCredentialParameters] { get set }
```

```objc
@property (nonatomic, copy) NSArray<ASAuthorizationPublicKeyCredentialParameters *> * credentialParameters;
```

## See Also

### Getting the properties
- [var excludedCredentials: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor]](./excludedcredentials.md)
  An array of excluded parameters for the credential.
- [var residentKeyPreference: ASAuthorizationPublicKeyCredentialResidentKeyPreference](./residentkeypreference.md)
  The preference that indicates where the resident key resides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialregistrationrequest/credentialparameters)*