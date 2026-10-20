# customLoginRequestValues

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

Provider-supplied values to add to the login POST request body.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var customLoginRequestValues: [URLQueryItem] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSURLQueryItem *> * customLoginRequestValues;
```

## Mentions

- [Creating and validating a login request](../creating-and-validating-a-login-request.md)

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
- [var kerberosTicketMappings: [ASAuthorizationProviderExtensionKerberosMapping]](./kerberosticketmappings.md)
  The set of ticket mappings the system uses to import Kerberos tickets from the single sign-on token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/customloginrequestvalues)*