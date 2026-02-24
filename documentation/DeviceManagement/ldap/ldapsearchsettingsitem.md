# LDAP.LDAPSearchSettingsItem

**Framework**: Device Management  
**Kind**: dictionary

An array of search settings dictionaries.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- visionOS 1.1+

## Declaration

```swift
object LDAP.LDAPSearchSettingsItem
```

## Properties

- `LDAPSearchSettingDescription` (string): The description of this search setting.
- `LDAPSearchSettingScope` (string): The type of recursion to use in the search: - `LDAPSearchSettingScopeBase`: The search uses only the immediate node that the search base points to.
- `LDAPSearchSettingScopeOneLevel`: The search uses the node plus its immediate children.
- `LDAPSearchSettingScopeSubtree`: The search uses the node plus all children, regardless of depth.
- `LDAPSearchSettingSearchBase` (string) *(required)*: The path to the node where a search should start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/ldap/ldapsearchsettingsitem)*