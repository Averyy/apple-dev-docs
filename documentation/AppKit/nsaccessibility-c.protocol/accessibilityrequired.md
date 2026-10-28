# accessibilityRequired

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the accessibility element must have content for successful submission of a form.

**Availability**:
- macOS 10.12+

## Declaration

```objc
@property (getter=isAccessibilityRequired) BOOL accessibilityRequired;
```

## Discussion

Returns YES if the element is required to have content; otherwise, NO.

## See Also

### Assigning roles
- [accessibilityRole](./accessibilityrole.md)
  The type of interface element that the accessibility element represents.
- [accessibilityRoleDescription](./accessibilityroledescription.md)
  A localized, human-intelligible description of the accessibility element’s role, such as *radio button*.
- [accessibilitySubrole](./accessibilitysubrole.md)
  The specialized interface element type that the accessibility element represents.
- [NSAccessibility.Role](../nsaccessibility-swift.struct/role.md)
  Values that describe types of objects that accessibility elements represent.
- [NSAccessibility.Subrole](../nsaccessibility-swift.struct/subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityrequired)*