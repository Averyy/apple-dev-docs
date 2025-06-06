# setCustomLoginRequestBodyClaims(_:)

**Framework**: Authentication Services  
**Kind**: method

Adds the custom claims to the login request body.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func setCustomLoginRequestBodyClaims(_ claims: [String : Any]) throws
```

## Parameters

- `claims`: The claims to add. The request must serialize as valid JSON for the system to accept it.

## See Also

- [func setCustomAssertionRequestBodyClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomassertionrequestbodyclaims(_:).md)
  Adds the custom claims to the embedded assertion request body.
- [func setCustomAssertionRequestHeaderClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomassertionrequestheaderclaims(_:).md)
  Adds the custom claims to the embedded assertion request header.
- [func setCustomLoginRequestHeaderClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomloginrequestheaderclaims(_:).md)
  Adds the custom claims to the login request header.
- [var additionalScopes: String](asauthorizationproviderextensionloginconfiguration/additionalscopes.md)
  A set of extra scopes to add to the base for the authentication request.
- [var customLoginRequestValues: [URLQueryItem]](asauthorizationproviderextensionloginconfiguration/customloginrequestvalues.md)
  Provider-supplied values to add to the login POST request body.
- [var kerberosTicketMappings: [ASAuthorizationProviderExtensionKerberosMapping]](asauthorizationproviderextensionloginconfiguration/kerberosticketmappings.md)
  The set of ticket mappings the system uses to import Kerberos tickets from the single sign-on token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/setcustomloginrequestbodyclaims(_:))*