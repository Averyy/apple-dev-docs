# clientData

**Framework**: Authentication Services  
**Kind**: property

The client data to supply to the relying party.

**Availability**:
- Mac Catalyst 16.6+
- macOS 13.5+

## Declaration

```swift
var clientData: ASPublicKeyCredentialClientData? { get }
```

## See Also

- [var excludedCredentials: [ASAuthorizationPlatformPublicKeyCredentialDescriptor]?](asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest/excludedcredentials.md)
  A list of passkeys that the relying party doesn’t accept for resolving the challenge.
- [var shouldShowHybridTransport: Bool](asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest/shouldshowhybridtransport.md)
  Whether a remote authenticator that communicates with the operating system using Bluetooth can resolve the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest/clientdata-5dk66)*