# setCustomAssertionRequestBodyClaims(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Adds the custom claims to the embedded assertion request body.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func setCustomAssertionRequestBodyClaims(_ claims: [String : Any]) throws
```

```objc
- (BOOL) setCustomAssertionRequestBodyClaims:(NSDictionary<NSString *,id> *) claims returningError:(NSError **) error;
```

## Parameters

- `claims`: The claims to add. The request must serialize as valid JSON for the system to accept it.

## See Also

### Customizing the authentication request
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
- [var kerberosTicketMappings: [ASAuthorizationProviderExtensionKerberosMapping]](./kerberosticketmappings.md)
  The set of ticket mappings the system uses to import Kerberos tickets from the single sign-on token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/setcustomassertionrequestbodyclaims(_:))*