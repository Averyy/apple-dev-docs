# CFHTTPAuthenticationCreateFromResponse(_:_:)

**Framework**: CFNetwork  
**Kind**: func

Uses an authentication failure response to create a CFHTTPAuthentication object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFHTTPAuthenticationCreateFromResponse(_ alloc: CFAllocator?, _ response: CFHTTPMessage) -> Unmanaged<CFHTTPAuthentication>
```

#### Return Value

CFHTTPAuthentication object that can be used for adding credentials to future requests. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function uses a response containing authentication failure information to create a reference to a CFHTTPAuthentication object. You can use the object to add credentials to future requests. You can query the object to get the following information:

- whether it can be used and re-used to authenticate with its corresponding server [[`CFHTTPAuthenticationIsValid(_:_:)`](cfhttpauthenticationisvalid(_:_:).md)]
- the authentication method that will be used when it is used to perform an authentication [[`CFHTTPAuthenticationCopyMethod(_:)`](cfhttpauthenticationcopymethod(_:).md)]
- whether it is associated with a particular CFHTTPMessageRef [[`CFHTTPAuthenticationAppliesToRequest(_:_:)`](cfhttpauthenticationappliestorequest(_:_:).md)
- whether a user name and a password will be required when it is used to perform an authentication [[`CFHTTPAuthenticationRequiresUserNameAndPassword(_:)`](cfhttpauthenticationrequiresusernameandpassword(_:).md)]
- whether an account domain will be required when it is used to perform an authentication [[`CFHTTPAuthenticationRequiresAccountDomain(_:)`](cfhttpauthenticationrequiresaccountdomain(_:).md)]
- whether authentication requests should be sent one at a time to the corresponding server [[`CFHTTPAuthenticationRequiresOrderedRequests(_:)`](cfhttpauthenticationrequiresorderedrequests(_:).md)]
- the namespace (if any) that the domain uses to prompt for a name and password [[`CFHTTPAuthenticationCopyRealm(_:)`](cfhttpauthenticationcopyrealm(_:).md)]
- the domain URLs the instance applies to [[`CFHTTPAuthenticationCopyDomains(_:)`](cfhttpauthenticationcopydomains(_:).md)]

When you have determined what information will be needed to perform the authentication and accumulated that information, call [`CFHTTPMessageApplyCredentials(_:_:_:_:_:)`](cfhttpmessageapplycredentials(_:_:_:_:_:).md) or [`CFHTTPMessageApplyCredentialDictionary(_:_:_:_:)`](cfhttpmessageapplycredentialdictionary(_:_:_:_:).md) to perform the authentication.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `response`: Response indicating an authentication failure; usually a 401 or a 407 response.

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

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhttpauthenticationcreatefromresponse(_:_:))*