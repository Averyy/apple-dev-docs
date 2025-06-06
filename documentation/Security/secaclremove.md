# SecACLRemove(_:)

**Framework**: Security  
**Kind**: func

Removes the specified ACL entry from the access instance that contains it.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SecACLRemove(_ aclRef: SecACL) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This method fails if you attempt to remove the owner entry because an access instance must have exactly one such ACL at all times. If you need to change ownership settings, modify the existing owner entry rather than replacing it. In particular, use the [`SecAccessCopyMatchingACLList(_:_:)`](secaccesscopymatchingacllist(_:_:).md) method with the [`kSecACLAuthorizationChangeACL`](ksecaclauthorizationchangeacl.md) authorization to find the existing entry, and the [`SecACLSetContents(_:_:_:_:)`](secaclsetcontents(_:_:_:_:).md) method to change it as needed.

## Parameters

- `aclRef`: An ACL entry to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaclremove(_:))*