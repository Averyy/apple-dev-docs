# SecACLSetContents(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Sets the application list, description, and prompt selector for a given ACL entry.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecACLSetContents(_ acl: SecACL, _ applicationList: CFArray?, _ description: CFString, _ promptSelector: SecKeychainPromptSelector) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Because an ACL entry is always associated with an access instance, when you modify the entry, you are modifying the access instance as well.

Use the [`SecACLCopyAuthorizations(_:)`](secaclcopyauthorizations(_:).md) method to get the list of operations for an ACL entry.

> **Note**:  Starting in macOS 10.13.1, for added security, the system ignores the `promptSelector` property of an ACL entry and always prompts for the keychain password when asking the user whether to add an app to the list of trusted apps.

## Parameters

- `acl`: The ACL entry to modify.
- `applicationList`: If you set this parameter to  , then any app can use this item. If you pass an empty array, then no apps are trusted.
- `description`: The name of the keychain item that appears in the dialog box when the user is prompted for permission to use the item. Note that this name is not necessarily the same as the one displayed for the item by the Keychain Access app.
- `promptSelector`: The prompt selector flags for the given access control list entry. See   for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaclsetcontents(_:_:_:_:))*