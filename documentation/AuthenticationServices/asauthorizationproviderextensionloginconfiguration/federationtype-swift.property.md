# federationType

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 13.3+

## Declaration

```swift
var federationType: ASAuthorizationProviderExtensionLoginConfiguration.FederationType { get set }
```

```objc
@property (nonatomic) ASAuthorizationProviderExtensionFederationType federationType;
```

## Mentions

- [Configuring authentication with the identity provider (IdP)](../configuring-authentication-with-the-identity-provider-idp.md)
- [Implementing web-based authentication with Platform Single Sign-on](../implementing-web-based-authentication.md)
- [Performing a WS-Trust metadata exchange data (MEX) request](../performing-a-ws-trust-metadata-exchange-data-mex-request.md)
- [Performing a preauthentication request](../performing-a-preauthentication-request.md)

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
- [var federationUserPreauthenticationURL: URL?](./federationuserpreauthenticationurl.md)
- [var groupRequestClaimName: String?](./grouprequestclaimname.md)
- [var groupResponseClaimName: String?](./groupresponseclaimname.md)
- [var jwksTrustedRootCertificates: [SecCertificate]](./jwkstrustedrootcertificates-5y2pc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/federationtype-swift.property)*