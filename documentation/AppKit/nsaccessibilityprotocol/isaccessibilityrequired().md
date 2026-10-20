# isAccessibilityRequired()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that determines whether the accessibility element must have content for successful submission of a form.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func isAccessibilityRequired() -> Bool
```

## See Also

### Assigning roles
- [func setAccessibilityRequired(Bool)](./setaccessibilityrequired%28_%29.md)
  Sets a Boolean value that determines whether the accessibility element must have content for successful submission of a form.
- [func accessibilityRole() -> NSAccessibility.Role?](./accessibilityrole%28%29.md)
  Returns the type of interface element that the accessibility element represents.
- [func setAccessibilityRole(NSAccessibility.Role?)](./setaccessibilityrole%28_%29.md)
  Sets the type of interface element that the accessibility element represents.
- [func accessibilityRoleDescription() -> String?](./accessibilityroledescription%28%29.md)
  Returns a localized, human-intelligible description of the accessibility element’s role, such as *radio button*.
- [func setAccessibilityRoleDescription(String?)](./setaccessibilityroledescription%28_%29.md)
  Sets the localized, human-intelligible description of the accessibility element’s role, such as *radio button*.
- [func accessibilitySubrole() -> NSAccessibility.Subrole?](./accessibilitysubrole%28%29.md)
  Returns the specialized interface element type that the accessibility element represents.
- [func setAccessibilitySubrole(NSAccessibility.Subrole?)](./setaccessibilitysubrole%28_%29.md)
  Sets the specialized interface element type that the accessibility element represents.
- [NSAccessibility.Role](../nsaccessibility-swift.struct/role.md)
  Values that describe types of objects that accessibility elements represent.
- [NSAccessibility.Subrole](../nsaccessibility-swift.struct/subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/isaccessibilityrequired())*