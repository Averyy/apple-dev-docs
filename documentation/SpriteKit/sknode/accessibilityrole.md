# accessibilityRole

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A string value describing the user interface element type; for example, a button.

**Availability**:
- macOS

## Declaration

```swift
var accessibilityRole: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * accessibilityRole;
```

#### Discussion

See [Roles](../../applicationservices/carbon_accessibility/roles.md) for more information.

## See Also

### Providing Accessibility
- [var accessibilityChildren: [Any]?](./accessibilitychildren.md)
  An array of user interface elements that represent children of this element.
- [var accessibilityFrame: CGRect](./accessibilityframe.md)
  The size of this user interface element, in screen points.
- [var accessibilityHelp: String?](./accessibilityhelp.md)
  The help description of this user interface element; for example, the text shown in a tooltip.
- [var accessibilityLabel: String?](./accessibilitylabel.md)
  A short description of this user interface element.
- [var accessibilityParent: AnyObject?](./accessibilityparent.md)
  The user interface element that contains this element.
- [var accessibilityRoleDescription: String?](./accessibilityroledescription.md)
  A string value describing the user interface element name and type; for example, the Buy button.
- [var accessibilitySubrole: String?](./accessibilitysubrole.md)
  A string that defines this user interface element’s subrole; for example, a full-screen button.
- [var isAccessibilityElement: Bool](./isaccessibilityelement.md)
  A toggle you implement to indicate to the system whether this user interface element should be exposed to the user.
- [var isAccessibilityEnabled: Bool](./isaccessibilityenabled.md)
  A toggle you implement to indicate to the system whether this user interface element should respond to user input.
- [func accessibilityHitTest(CGPoint) -> Any?](./accessibilityhittest%28_%29.md)
  Returns the frontmost user interface element in the element hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/accessibilityrole)*