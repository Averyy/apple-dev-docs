# setCustomAssertionRequestHeaderClaims(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Adds the custom claims to the embedded assertion request header.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func setCustomAssertionRequestHeaderClaims(_ claims: [String : Any]) throws
```

```objc
- (BOOL) setCustomAssertionRequestHeaderClaims:(NSDictionary<NSString *,id> *) claims returningError:(NSError **) error;
```

## Parameters

- `claims`: The claims to add. The request must serialize as valid JSON for the system to accept it.

## See Also

### Customizing the authentication request
- [func setCustomAssertionRequestBodyClaims([String : Any]) throws](./setcustomassertionrequestbodyclaims%28_%29.md)
  Adds the custom claims to the embedded assertion request body.
- [func setCustomLoginRequestBodyClaims([String : Any]) throws](./setcustomloginrequestbodyclaims%28_%29.md)
  Adds the custom claims to the login request body.
- [func setCustomLoginRequestHeaderClaims([String : Any]) throws](./setcustomloginrequestheaderclaims%28_%29.md)
  Adds the custom claims to the login request header.
- [var additionalScopes: String](./additionalscopes.md)
  A set of extra scopes to add to the base for the authentication request.
- [var customLoginRequestValues: [URLQueryItem]](./customloginrequestvalues.md)
  Provider-supplied values to add to the login POST request body.
- [var kerberosTicketMappings: [ASAuthorizationProviderExtensionKerberosMapping]](./kerberosticketmappings.md)
  The set of ticket mappings the system uses to import Kerberos tickets from the single sign-on token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/setcustomassertionrequestheaderclaims(_:))*