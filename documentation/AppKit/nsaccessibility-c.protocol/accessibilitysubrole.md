# accessibilitySubrole

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The specialized interface element type that the accessibility element represents.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (copy, nullable) NSAccessibilitySubrole accessibilitySubrole;
```

#### Discussion

For a list of possible subroles, see `Subroles`.

## See Also

### Assigning roles
- [accessibilityRequired](./accessibilityrequired.md)
  A Boolean value that determines whether the accessibility element must have content for successful submission of a form.
- [accessibilityRole](./accessibilityrole.md)
  The type of interface element that the accessibility element represents.
- [accessibilityRoleDescription](./accessibilityroledescription.md)
  A localized, human-intelligible description of the accessibility element’s role, such as *radio button*.
- [NSAccessibility.Role](../nsaccessibility-swift.struct/role.md)
  Values that describe types of objects that accessibility elements represent.
- [NSAccessibility.Subrole](../nsaccessibility-swift.struct/subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilitysubrole)*