# SecACLCreateWithSimpleContents(_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Creates a new ACL entry with the given characteristics, and adds it to an access instance.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecACLCreateWithSimpleContents(_ access: SecAccess, _ applicationList: CFArray?, _ description: CFString, _ promptSelector: SecKeychainPromptSelector, _ newAcl: UnsafeMutablePointer<SecACL?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

The ACL entry returned by this method includes a list of trusted apps, the name of the keychain item as it appears in user prompts, the prompt selector flag, and a list of one or more operations to which this ACL entry applies. By default, a new ACL entry applies to all operations. Use the [`SecACLUpdateAuthorizations(_:_:)`](secaclupdateauthorizations(_:_:).md) method to set the list of operations for an ACL entry.

> **Note**:  Starting in macOS 10.13.1, for added security, the system ignores the `promptSelector` property of an ACL object and always prompts for the keychain password when asking the user whether to add an app to the list of trusted apps.

The system requires exactly one owner ACL entry in each access instance. The [`SecACLCreateWithSimpleContents(_:_:_:_:_:)`](secaclcreatewithsimplecontents(_:_:_:_:_:).md) method fails if you attempt to add a second owner entry. To change owner access controls, use the [`SecAccessCopyMatchingACLList(_:_:)`](secaccesscopymatchingacllist(_:_:).md) function to find the owner entry (the only one with an authorization tag of [`kSecACLAuthorizationChangeACL`](ksecaclauthorizationchangeacl.md)) and the [`SecACLSetContents(_:_:_:_:)`](secaclsetcontents(_:_:_:_:).md) method to change it as needed.

## Parameters

- `access`: The access instance to which to add the information.
- `applicationList`: Set this parameter to   to indicate that any app can use this item. Pass an empty array to indicate that there are no trusted apps.
- `description`: The human readable name to be used to refer to this item when the user is prompted.
- `promptSelector`: A set of prompt selector flags. See   for possible values.
- `newAcl`: A pointer the method uses to return the new   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaclcreatewithsimplecontents(_:_:_:_:_:))*