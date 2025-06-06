# kerberosTicketMappings

**Framework**: Authentication Services  
**Kind**: property

The set of ticket mappings the system uses to import Kerberos tickets from the single sign-on token.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var kerberosTicketMappings: [ASAuthorizationProviderExtensionKerberosMapping] { get set }
```

## Mentions

- [Creating a JSON Web Encryption (JWE) login response](creating-a-json-web-encryption-jwe-login-response.md)

## See Also

- [func setCustomAssertionRequestBodyClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomassertionrequestbodyclaims(_:).md)
  Adds the custom claims to the embedded assertion request body.
- [func setCustomAssertionRequestHeaderClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomassertionrequestheaderclaims(_:).md)
  Adds the custom claims to the embedded assertion request header.
- [func setCustomLoginRequestBodyClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomloginrequestbodyclaims(_:).md)
  Adds the custom claims to the login request body.
- [func setCustomLoginRequestHeaderClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomloginrequestheaderclaims(_:).md)
  Adds the custom claims to the login request header.
- [var additionalScopes: String](asauthorizationproviderextensionloginconfiguration/additionalscopes.md)
  A set of extra scopes to add to the base for the authentication request.
- [var customLoginRequestValues: [URLQueryItem]](asauthorizationproviderextensionloginconfiguration/customloginrequestvalues.md)
  Provider-supplied values to add to the login POST request body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/kerberosticketmappings)*