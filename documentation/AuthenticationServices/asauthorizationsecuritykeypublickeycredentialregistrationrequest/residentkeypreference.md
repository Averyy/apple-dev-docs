# residentKeyPreference

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The preference that indicates where the resident key resides.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var residentKeyPreference: ASAuthorizationPublicKeyCredentialResidentKeyPreference { get set }
```

```objc
@property (nonatomic) ASAuthorizationPublicKeyCredentialResidentKeyPreference residentKeyPreference;
```

## See Also

### Getting the properties
- [var credentialParameters: [ASAuthorizationPublicKeyCredentialParameters]](./credentialparameters.md)
  An array of parameters for the credential.
- [var excludedCredentials: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor]](./excludedcredentials.md)
  An array of excluded parameters for the credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialregistrationrequest/residentkeypreference)*