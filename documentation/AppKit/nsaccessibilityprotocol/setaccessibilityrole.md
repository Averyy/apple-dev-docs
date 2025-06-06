# setAccessibilityRole(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Sets the type of interface element that the accessibility element represents.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func setAccessibilityRole(_ accessibilityRole: NSAccessibility.Role?)
```

## See Also

- [func isAccessibilityRequired() -> Bool](nsaccessibilityprotocol/isaccessibilityrequired.md)
  Returns a Boolean value that determines whether the accessibility element must have content for successful submission of a form.
- [func setAccessibilityRequired(Bool)](nsaccessibilityprotocol/setaccessibilityrequired(_:).md)
  Sets a Boolean value that determines whether the accessibility element must have content for successful submission of a form.
- [func accessibilityRole() -> NSAccessibility.Role?](nsaccessibilityprotocol/accessibilityrole.md)
  Returns the type of interface element that the accessibility element represents.
- [func accessibilityRoleDescription() -> String?](nsaccessibilityprotocol/accessibilityroledescription.md)
  Returns a localized, human-intelligible description of the accessibility element’s role, such as .
- [func setAccessibilityRoleDescription(String?)](nsaccessibilityprotocol/setaccessibilityroledescription(_:).md)
  Sets the localized, human-intelligible description of the accessibility element’s role, such as .
- [func accessibilitySubrole() -> NSAccessibility.Subrole?](nsaccessibilityprotocol/accessibilitysubrole.md)
  Returns the specialized interface element type that the accessibility element represents.
- [func setAccessibilitySubrole(NSAccessibility.Subrole?)](nsaccessibilityprotocol/setaccessibilitysubrole(_:).md)
  Sets the specialized interface element type that the accessibility element represents.
- [NSAccessibility.Role](nsaccessibility-swift.struct/role.md)
  Values that describe types of objects that accessibility elements represent.
- [NSAccessibility.Subrole](nsaccessibility-swift.struct/subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/setaccessibilityrole(_:))*