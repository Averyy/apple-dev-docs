# SecACLCopyContents(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Returns the application list, description, and prompt selector for a given ACL entry.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecACLCopyContents(_ acl: SecACL, _ applicationList: UnsafeMutablePointer<CFArray?>, _ description: UnsafeMutablePointer<CFString?>, _ promptSelector: UnsafeMutablePointer<SecKeychainPromptSelector>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

An ACL entry applies to a specific use or set of uses for a specific keychain item. The entry includes a list of trusted applications, the name of the keychain item as it appears in user prompts, the prompt selector flag, and a list of one or more operations to which this ACL entry applies.

Use the [`SecACLCopyAuthorizations(_:)`](secaclcopyauthorizations(_:).md) method to get the list of operations for an ACL entry.

> **Note**:  Starting in macOS 10.13.1, for added security, the system ignores the `promptSelector` property of an ACL entry and always prompts for the keychain password when asking the user whether to add an app to the list of trusted apps.

## Parameters

- `acl`: The ACL entry from which you want information.
- `applicationList`: Call the   method to release this array when you are finished using it.
- `description`: Call the   method to release this string when you are finished using it.
- `promptSelector`: If the   bit is set, the user is prompted for the keychain password each time a non-trusted application attempts to access this item, even if the keychain is already unlocked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaclcopycontents(_:_:_:_:))*