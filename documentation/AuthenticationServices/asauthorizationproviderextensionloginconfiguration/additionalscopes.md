# additionalScopes

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

A set of extra scopes to add to the base for the authentication request.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var additionalScopes: String { get set }
```

```objc
@property (nonatomic, copy) NSString * additionalScopes;
```

## Mentions

- [Creating a refresh request](../creating-a-refresh-request.md)
- [Creating an embedded assertion](../creating-an-embedded-assertion.md)
- [Creating an encrypted embedded assertion](../creating-an-encrypted-embedded-assertion.md)
- [Creating and validating a login request](../creating-and-validating-a-login-request.md)

#### Discussion

The base value is `openid offline_access`. The system appends any additional values. The default additional scope is `urn:apple:platformsso`.

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
- [var customLoginRequestValues: [URLQueryItem]](./customloginrequestvalues.md)
  Provider-supplied values to add to the login POST request body.
- [var kerberosTicketMappings: [ASAuthorizationProviderExtensionKerberosMapping]](./kerberosticketmappings.md)
  The set of ticket mappings the system uses to import Kerberos tickets from the single sign-on token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/additionalscopes)*