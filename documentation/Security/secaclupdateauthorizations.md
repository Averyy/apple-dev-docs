# SecACLUpdateAuthorizations(_:_:)

**Framework**: Security  
**Kind**: func

Sets the authorization tags for a given ACL.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecACLUpdateAuthorizations(_ acl: SecACL, _ authorizations: CFArray) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

An ACL entry includes a list of trusted apps, the name of the keychain item as it appears in user prompts, the prompt selector flag, and a list of one or more operations to which this ACL entry applies. Use this method to set a list of operations for an ACL entry, or set the [`kSecACLAuthorizationAny`](ksecaclauthorizationany.md) tag to allow all operations. Use the [`SecACLSetContents(_:_:_:_:)`](secaclsetcontents(_:_:_:_:).md) method to set the other information.

Because an ACL entry is always associated with an access instance, when you modify an entry, you are modifying the access instance as well.

## Parameters

- `acl`: An ACL object that identifies the access control list entry for which you wish to set authorization tags.
- `authorizations`: An array of authorization tags. See   for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaclupdateauthorizations(_:_:))*