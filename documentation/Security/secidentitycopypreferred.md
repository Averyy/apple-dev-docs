# SecIdentityCopyPreferred(_:_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the preferred identity for the specified name and key use.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecIdentityCopyPreferred(_ name: CFString, _ keyUsage: CFArray?, _ validIssuers: CFArray?) -> SecIdentity?
```

#### Return Value

Returns an identity, or `nil` if no identity from one of the specified issuers has been set as the preferred identity for the specified name and usage. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to free the identity’s memory when you are done with it.

#### Discussion

If a preferred identity has not been set for the supplied name, this function returns `NULL`. Your code should then perform a search for possible identities by calling [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md).

## Parameters

- `name`: A string containing an email address (RFC 822) or other name for which a preferred identity is requested.
- `keyUsage`: An array containing a list of usage attributes ( , for example), or   if you do not want to request an identity for a particular usage. See Attribute Item Keys for a complete list of possible usage attributes.
- `validIssuers`: An array of   objects whose contents are the subject names of allowable issuers, as returned by a call to  . Pass   to allow any issuer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secidentitycopypreferred(_:_:_:))*