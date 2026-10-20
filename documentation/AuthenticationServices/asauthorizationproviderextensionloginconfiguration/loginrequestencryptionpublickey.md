# loginRequestEncryptionPublicKey

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 14.0+

## Declaration

```swift
unowned(unsafe) var loginRequestEncryptionPublicKey: SecKey? { get set }
```

```objc
@property (nonatomic, assign, nullable) SecKeyRef loginRequestEncryptionPublicKey;
```

## Mentions

- [Creating an encrypted embedded assertion](../creating-an-encrypted-embedded-assertion.md)
- [Creating and validating a login request](../creating-and-validating-a-login-request.md)

## See Also

### Instance Properties
- [var additionalAuthorizationScopes: String?](./additionalauthorizationscopes.md)
- [var customFederationUserPreauthenticationRequestValues: [URLQueryItem]](./customfederationuserpreauthenticationrequestvalues.md)
- [var customKeyExchangeRequestValues: [URLQueryItem]](./customkeyexchangerequestvalues.md)
- [var customKeyRequestValues: [URLQueryItem]](./customkeyrequestvalues.md)
- [var customRefreshRequestValues: [URLQueryItem]](./customrefreshrequestvalues.md)
- [var customRequestJWTParameterName: String?](./customrequestjwtparametername.md)
- [var deviceContext: Data?](./devicecontext.md)
- [var federationMEXURL: URL?](./federationmexurl.md)
- [var federationMEXURLKeypath: String?](./federationmexurlkeypath.md)
- [var federationPredicate: String?](./federationpredicate.md)
- [var federationRequestURN: String?](./federationrequesturn.md)
- [var federationType: ASAuthorizationProviderExtensionLoginConfiguration.FederationType](./federationtype-swift.property.md)
- [var federationUserPreauthenticationURL: URL?](./federationuserpreauthenticationurl.md)
- [var groupRequestClaimName: String?](./grouprequestclaimname.md)
- [var groupResponseClaimName: String?](./groupresponseclaimname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/loginrequestencryptionpublickey)*