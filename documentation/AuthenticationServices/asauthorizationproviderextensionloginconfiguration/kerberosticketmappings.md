# kerberosTicketMappings

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The set of ticket mappings the system uses to import Kerberos tickets from the single sign-on token.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var kerberosTicketMappings: [ASAuthorizationProviderExtensionKerberosMapping] { get set }
```

```objc
@property (nonatomic, copy) NSArray<ASAuthorizationProviderExtensionKerberosMapping *> * kerberosTicketMappings;
```

## Mentions

- [Creating a JSON Web Encryption (JWE) login response](../creating-a-json-web-encryption-jwe-login-response.md)

## See Also

### Customizing the authentication request
- [func setCustomAssertionRequestBodyClaims([String : Any]) throws](./setcustomassertionrequestbodyclaims%28_%29.md)
  Adds the custom claims to the embedded assertion request body.
- [func setCustomAssertionRequestHeaderClaims([String : Any]) throws](./setcustomassertionrequestheaderclaims%28_%29.md)
  Adds the custom claims to the embedded assertion request header.
- [func setCustomLoginRequestBodyClaims([String : Any]) throws](./setcustomloginrequestbodyclaims%28_%29.md)
  Adds the custom claims to the login request body.
- [func setCustomLoginRequestHeaderClaims([String : Any]) throws](./setcustomloginrequestheaderclaims%28_%29.md)
  Adds the custom claims to the login request header.
- [var additionalScopes: String](./additionalscopes.md)
  A set of extra scopes to add to the base for the authentication request.
- [var customLoginRequestValues: [URLQueryItem]](./customloginrequestvalues.md)
  Provider-supplied values to add to the login POST request body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/kerberosticketmappings)*