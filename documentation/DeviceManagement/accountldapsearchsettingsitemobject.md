# AccountLDAPSearchSettingsItemObject

**Framework**: Device Management  
**Kind**: dictionary

The settings for configuring the search behavior with an LDAP server.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AccountLDAPSearchSettingsItemObject
```

## Properties

- `Scope` (string): The type of recursion to use in the search: - `Base`: The search uses only the `SearchBase` node.
- `OneLevel`: The search uses the `SearchBase` node and its immediate children.
- `Subtree`: The search uses the `SearchBase` node and all its children, regardless of depth.
- `SearchBase` (string) *(required)*: The path to the node where a search starts. For example, `ou=people,o=example corp`.
- `VisibleDescription` (string): The description of this search setting in the Contacts and Settings apps. If not present, the apps display no name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountldapsearchsettingsitemobject)*