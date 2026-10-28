# accessibilityRoleDescription

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A localized, human-intelligible description of the accessibility element’s role, such as *radio button*.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (copy, nullable) NSString * accessibilityRoleDescription;
```

## Discussion

This property is set automatically based on the value of the [`accessibilityRole`](./accessibilityrole.md) property; however, you can customize the value of this property to better describe your element’s role. Keep role descriptions short. If possible, use a single word. These descriptions should be noun phrases, all lowercase, with no period at the end.

## See Also

### Related Documentation
- [accessibilityLabel](./accessibilitylabel.md)
  A short description of the accessibility element.
- [accessibilityHelp](./accessibilityhelp.md)
  The help text for the accessibility element.
### Assigning roles
- [accessibilityRequired](./accessibilityrequired.md)
  A Boolean value that determines whether the accessibility element must have content for successful submission of a form.
- [accessibilityRole](./accessibilityrole.md)
  The type of interface element that the accessibility element represents.
- [accessibilitySubrole](./accessibilitysubrole.md)
  The specialized interface element type that the accessibility element represents.
- [NSAccessibility.Role](../nsaccessibility-swift.struct/role.md)
  Values that describe types of objects that accessibility elements represent.
- [NSAccessibility.Subrole](../nsaccessibility-swift.struct/subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityroledescription)*