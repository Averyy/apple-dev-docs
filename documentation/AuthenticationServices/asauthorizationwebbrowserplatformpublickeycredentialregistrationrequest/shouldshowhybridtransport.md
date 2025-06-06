# shouldShowHybridTransport

**Framework**: Authentication Services  
**Kind**: property  
**Required**: Yes

Whether a remote authenticator that communicates with the operating system using Bluetooth can resolve the challenge.

**Availability**:
- Mac Catalyst 16.6+
- macOS 13.5+

## Declaration

```swift
var shouldShowHybridTransport: Bool { get set }
```

## See Also

- [var clientData: ASPublicKeyCredentialClientData?](asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest/clientdata-5dk66.md)
  The client data to supply to the relying party.
- [var excludedCredentials: [ASAuthorizationPlatformPublicKeyCredentialDescriptor]?](asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest/excludedcredentials.md)
  A list of passkeys that the relying party doesn’t accept for resolving the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest/shouldshowhybridtransport)*