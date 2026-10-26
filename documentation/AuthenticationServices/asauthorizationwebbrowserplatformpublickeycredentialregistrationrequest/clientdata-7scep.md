# clientData

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The client data to supply to the relying party.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.6+
- macOS 13.5+

## Declaration

```objc
@property (nonatomic, readonly, nullable) ASPublicKeyCredentialClientData * clientData;
```

## See Also

### Information about the assertion
- [var excludedCredentials: [ASAuthorizationPlatformPublicKeyCredentialDescriptor]?](./excludedcredentials.md)
  A list of passkeys that the relying party doesn’t accept for resolving the challenge.
- [var shouldShowHybridTransport: Bool](./shouldshowhybridtransport.md)
  Whether a remote authenticator that communicates with the operating system using Bluetooth can resolve the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest/clientdata-7scep)*