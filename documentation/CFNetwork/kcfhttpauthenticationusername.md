# kCFHTTPAuthenticationUsername

**Framework**: CFNetwork  
**Kind**: var

Username to use for authentication.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let kCFHTTPAuthenticationUsername: CFString
```

## See Also

- [class CFHTTPAuthentication](cfhttpauthentication.md)
  An opaque reference representing HTTP authentication information.
- [func CFHTTPAuthenticationAppliesToRequest(CFHTTPAuthentication, CFHTTPMessage) -> Bool](cfhttpauthenticationappliestorequest(_:_:).md)
  Returns a Boolean value that indicates whether a CFHTTPAuthentication object is associated with a CFHTTPMessage object.
- [func CFHTTPAuthenticationCopyDomains(CFHTTPAuthentication) -> Unmanaged<CFArray>](cfhttpauthenticationcopydomains(_:).md)
  Returns an array of domain URLs to which a given CFHTTPAuthentication object can be applied.
- [func CFHTTPAuthenticationCopyMethod(CFHTTPAuthentication) -> Unmanaged<CFString>](cfhttpauthenticationcopymethod(_:).md)
  Gets the strongest authentication method that will be used when a CFHTTPAuthentication object is applied to a request.
- [func CFHTTPAuthenticationCopyRealm(CFHTTPAuthentication) -> Unmanaged<CFString>](cfhttpauthenticationcopyrealm(_:).md)
  Gets an authentication information’s namespace.
- [func CFHTTPAuthenticationCreateFromResponse(CFAllocator?, CFHTTPMessage) -> Unmanaged<CFHTTPAuthentication>](cfhttpauthenticationcreatefromresponse(_:_:).md)
  Uses an authentication failure response to create a CFHTTPAuthentication object.
- [func CFHTTPAuthenticationGetTypeID() -> CFTypeID](cfhttpauthenticationgettypeid().md)
  Gets the Core Foundation type identifier for the CFHTTPAuthentication opaque type.
- [func CFHTTPAuthenticationIsValid(CFHTTPAuthentication, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfhttpauthenticationisvalid(_:_:).md)
  Returns a Boolean value that indicates whether a CFHTTPAuthentication object is valid.
- [func CFHTTPAuthenticationRequiresAccountDomain(CFHTTPAuthentication) -> Bool](cfhttpauthenticationrequiresaccountdomain(_:).md)
  Returns a Boolean value that indicates whether a CFHTTPAuthentication object uses an authentication method that requires an account domain.
- [func CFHTTPAuthenticationRequiresOrderedRequests(CFHTTPAuthentication) -> Bool](cfhttpauthenticationrequiresorderedrequests(_:).md)
  Returns a Boolean value that indicates whether authentication requests should be made one at a time.
- [func CFHTTPAuthenticationRequiresUserNameAndPassword(CFHTTPAuthentication) -> Bool](cfhttpauthenticationrequiresusernameandpassword(_:).md)
  Returns a Boolean value that indicates whether a CFHTTPAuthentication object uses an authentication method that requires a username and a password.
- [let kCFHTTPAuthenticationAccountDomain: CFString](kcfhttpauthenticationaccountdomain.md)
  Account domain to use for authentication.
- [let kCFHTTPAuthenticationPassword: CFString](kcfhttpauthenticationpassword.md)
  Password to use for authentication.
- [let kCFHTTPAuthenticationSchemeBasic: CFString](kcfhttpauthenticationschemebasic.md)
  Request the HTTP basic authentication scheme.
- [let kCFHTTPAuthenticationSchemeDigest: CFString](kcfhttpauthenticationschemedigest.md)
  Request the HTTP digest authentication scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationusername)*