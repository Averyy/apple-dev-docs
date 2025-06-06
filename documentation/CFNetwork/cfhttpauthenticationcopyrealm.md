# CFHTTPAuthenticationCopyRealm(_:)

**Framework**: CFNetwork  
**Kind**: func

Gets an authentication information’s namespace.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFHTTPAuthenticationCopyRealm(_ auth: CFHTTPAuthentication) -> Unmanaged<CFString>
```

#### Return Value

The namespace, if there is one; otherwise `NULL`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Some authentication methods provide a namespace, and it is usually used to prompt the user for a name and password.

## Parameters

- `auth`: The CFHTTPAuthentication object to examine.

## See Also

- [class CFHTTPAuthentication](cfhttpauthentication.md)
  An opaque reference representing HTTP authentication information.
- [func CFHTTPAuthenticationAppliesToRequest(CFHTTPAuthentication, CFHTTPMessage) -> Bool](cfhttpauthenticationappliestorequest(_:_:).md)
  Returns a Boolean value that indicates whether a CFHTTPAuthentication object is associated with a CFHTTPMessage object.
- [func CFHTTPAuthenticationCopyDomains(CFHTTPAuthentication) -> Unmanaged<CFArray>](cfhttpauthenticationcopydomains(_:).md)
  Returns an array of domain URLs to which a given CFHTTPAuthentication object can be applied.
- [func CFHTTPAuthenticationCopyMethod(CFHTTPAuthentication) -> Unmanaged<CFString>](cfhttpauthenticationcopymethod(_:).md)
  Gets the strongest authentication method that will be used when a CFHTTPAuthentication object is applied to a request.
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
- [let kCFHTTPAuthenticationSchemeKerberos: CFString](kcfhttpauthenticationschemekerberos.md)
  Request the HTTP Kerberos authentication scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhttpauthenticationcopyrealm(_:))*