# init(credentialID:transports:)

**Framework**: Authentication Services  
**Kind**: init

Creates the object with the credential ID and the array of transports.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
init(credentialID: Data, transports allowedTransports: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport])
```

## Parameters

- `credentialID`: The credential identifier.
- `allowedTransports`: The array of allowed transports.

## See Also

- [var transports: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport]](asauthorizationsecuritykeypublickeycredentialdescriptor/transports.md)
  The array of transport types.
- [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport](asauthorizationsecuritykeypublickeycredentialdescriptor/transport.md)
  A structure that defines the security key credential transport type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialdescriptor/init(credentialid:transports:))*