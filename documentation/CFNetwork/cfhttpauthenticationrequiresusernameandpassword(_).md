# CFHTTPAuthenticationRequiresUserNameAndPassword(_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a CFHTTPAuthentication object uses an authentication method that requires a username and a password.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFHTTPAuthenticationRequiresUserNameAndPassword(_ auth: CFHTTPAuthentication) -> Bool
```

```c
extern Boolean CFHTTPAuthenticationRequiresUserNameAndPassword(CFHTTPAuthenticationRef auth);
```

## Return Value

`TRUE` if `auth` requires a username and password when it is applied to a request; otherwise, `FALSE`.

## Parameters

- `auth`: The CFHTTPAuthentication object to examine.

## See Also

### HTTP Authentication
- [class CFHTTPAuthentication](./cfhttpauthentication.md)
  An opaque reference representing HTTP authentication information.
- [func CFHTTPAuthenticationAppliesToRequest(CFHTTPAuthentication, CFHTTPMessage) -> Bool](./cfhttpauthenticationappliestorequest%28_,_%29.md)
  Returns a Boolean value that indicates whether a CFHTTPAuthentication object is associated with a CFHTTPMessage object.
- [func CFHTTPAuthenticationCopyDomains(CFHTTPAuthentication) -> Unmanaged<CFArray>](./cfhttpauthenticationcopydomains%28_%29.md)
  Returns an array of domain URLs to which a given CFHTTPAuthentication object can be applied.
- [func CFHTTPAuthenticationCopyMethod(CFHTTPAuthentication) -> Unmanaged<CFString>](./cfhttpauthenticationcopymethod%28_%29.md)
  Gets the strongest authentication method that will be used when a CFHTTPAuthentication object is applied to a request.
- [func CFHTTPAuthenticationCopyRealm(CFHTTPAuthentication) -> Unmanaged<CFString>](./cfhttpauthenticationcopyrealm%28_%29.md)
  Gets an authentication information’s namespace.
- [func CFHTTPAuthenticationCreateFromResponse(CFAllocator?, CFHTTPMessage) -> Unmanaged<CFHTTPAuthentication>](./cfhttpauthenticationcreatefromresponse%28_,_%29.md)
  Uses an authentication failure response to create a CFHTTPAuthentication object.
- [func CFHTTPAuthenticationGetTypeID() -> CFTypeID](./cfhttpauthenticationgettypeid%28%29.md)
  Gets the Core Foundation type identifier for the CFHTTPAuthentication opaque type.
- [func CFHTTPAuthenticationIsValid(CFHTTPAuthentication, UnsafeMutablePointer<CFStreamError>?) -> Bool](./cfhttpauthenticationisvalid%28_,_%29.md)
  Returns a Boolean value that indicates whether a CFHTTPAuthentication object is valid.
- [func CFHTTPAuthenticationRequiresAccountDomain(CFHTTPAuthentication) -> Bool](./cfhttpauthenticationrequiresaccountdomain%28_%29.md)
  Returns a Boolean value that indicates whether a CFHTTPAuthentication object uses an authentication method that requires an account domain.
- [func CFHTTPAuthenticationRequiresOrderedRequests(CFHTTPAuthentication) -> Bool](./cfhttpauthenticationrequiresorderedrequests%28_%29.md)
  Returns a Boolean value that indicates whether authentication requests should be made one at a time.
- [let kCFHTTPAuthenticationAccountDomain: CFString](./kcfhttpauthenticationaccountdomain.md)
  Account domain to use for authentication.
- [let kCFHTTPAuthenticationPassword: CFString](./kcfhttpauthenticationpassword.md)
  Password to use for authentication.
- [let kCFHTTPAuthenticationSchemeBasic: CFString](./kcfhttpauthenticationschemebasic.md)
  Request the HTTP basic authentication scheme.
- [let kCFHTTPAuthenticationSchemeDigest: CFString](./kcfhttpauthenticationschemedigest.md)
  Request the HTTP digest authentication scheme.
- [let kCFHTTPAuthenticationSchemeKerberos: CFString](./kcfhttpauthenticationschemekerberos.md)
  Request the HTTP Kerberos authentication scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhttpauthenticationrequiresusernameandpassword(_:))*