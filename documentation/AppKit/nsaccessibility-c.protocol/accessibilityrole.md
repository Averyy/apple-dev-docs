# accessibilityRole

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The type of interface element that the accessibility element represents.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (copy, nullable) NSAccessibilityRole accessibilityRole;
```

#### Discussion

This property contains a nonlocalized string that defines the element’s role in the app. For a list of possible roles, see `Roles`. This property is set automatically when you adopt one of the accessibility protocols.

## See Also

### Assigning roles
- [accessibilityRequired](./accessibilityrequired.md)
  A Boolean value that determines whether the accessibility element must have content for successful submission of a form.
- [accessibilityRoleDescription](./accessibilityroledescription.md)
  A localized, human-intelligible description of the accessibility element’s role, such as *radio button*.
- [accessibilitySubrole](./accessibilitysubrole.md)
  The specialized interface element type that the accessibility element represents.
- [NSAccessibility.Role](../nsaccessibility-swift.struct/role.md)
  Values that describe types of objects that accessibility elements represent.
- [NSAccessibility.Subrole](../nsaccessibility-swift.struct/subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityrole)*