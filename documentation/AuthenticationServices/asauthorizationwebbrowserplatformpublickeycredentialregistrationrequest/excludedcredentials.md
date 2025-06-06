# excludedCredentials

**Framework**: Authentication Services  
**Kind**: property  
**Required**: Yes

A list of passkeys that the relying party doesn’t accept for resolving the challenge.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.6+
- macOS 13.5+

## Declaration

```swift
var excludedCredentials: [ASAuthorizationPlatformPublicKeyCredentialDescriptor]? { get set }
```

## See Also

- [var clientData: ASPublicKeyCredentialClientData?](asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest/clientdata-5dk66.md)
  The client data to supply to the relying party.
- [var shouldShowHybridTransport: Bool](asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest/shouldshowhybridtransport.md)
  Whether a remote authenticator that communicates with the operating system using Bluetooth can resolve the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest/excludedcredentials)*