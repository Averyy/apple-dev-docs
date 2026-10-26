# customFederationUserPreauthenticationRequestValues

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 13.3+

## Declaration

```swift
var customFederationUserPreauthenticationRequestValues: [URLQueryItem] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSURLQueryItem *> * customFederationUserPreauthenticationRequestValues;
```

## Mentions

- [Performing a preauthentication request](../performing-a-preauthentication-request.md)

## See Also

### Instance Properties
- [var additionalAuthorizationScopes: String?](./additionalauthorizationscopes.md)
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
- [var jwksTrustedRootCertificates: [SecCertificate]](./jwkstrustedrootcertificates-5y2pc.md)
- [keyEndpointURL](./keyendpointurl.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/customfederationuserpreauthenticationrequestvalues)*