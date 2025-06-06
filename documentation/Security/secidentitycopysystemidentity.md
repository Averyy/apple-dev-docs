# SecIdentityCopySystemIdentity(_:_:_:)

**Framework**: Security  
**Kind**: func

Obtains the system identity associated with a specified domain.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SecIdentityCopySystemIdentity(_ domain: CFString, _ idRef: UnsafeMutablePointer<SecIdentity?>, _ actualDomain: UnsafeMutablePointer<CFString?>?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

If no system identity exists for the specified domain, a domain specific alternate may be returned instead. This is typically (but not exclusively) the system default identity. ([`kSecIdentityDomainDefault`](ksecidentitydomaindefault.md)).

## Parameters

- `domain`: The domain for which you want to find an identity, typically in reverse DNS notation, such as  . You may also pass the values defined in  .
- `idRef`: On return, the identity object of the system-wide identity associated with the specified domain. In Objective-C, call the   function to release this object when you are finished with it.
- `actualDomain`: On return, the actual domain name of the returned identity object is returned here. This may be different from the requested domain. Pass   if you do not want this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secidentitycopysystemidentity(_:_:_:))*