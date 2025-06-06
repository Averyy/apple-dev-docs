# accessibilityRole

**Framework**: SpriteKit  
**Kind**: property

A string value describing the user interface element type; for example, a button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var accessibilityRole: String? { get set }
```

#### Discussion

See [`Roles`](https://developer.apple.com/documentation/applicationservices/carbon_accessibility/roles) for more information.

## See Also

- [var accessibilityChildren: [Any]?](sknode/accessibilitychildren.md)
  An array of user interface elements that represent children of this element.
- [var accessibilityFrame: CGRect](sknode/accessibilityframe.md)
  The size of this user interface element, in screen points.
- [var accessibilityHelp: String?](sknode/accessibilityhelp.md)
  The help description of this user interface element; for example, the text shown in a tooltip.
- [var accessibilityLabel: String?](sknode/accessibilitylabel.md)
  A short description of this user interface element.
- [var accessibilityParent: AnyObject?](sknode/accessibilityparent.md)
  The user interface element that contains this element.
- [var accessibilityRoleDescription: String?](sknode/accessibilityroledescription.md)
  A string value describing the user interface element name and type; for example, the Buy button.
- [var accessibilitySubrole: String?](sknode/accessibilitysubrole.md)
  A string that defines this user interface element’s subrole; for example, a full-screen button.
- [var isAccessibilityElement: Bool](sknode/isaccessibilityelement.md)
  A toggle you implement to indicate to the system whether this user interface element should be exposed to the user.
- [var isAccessibilityEnabled: Bool](sknode/isaccessibilityenabled.md)
  A toggle you implement to indicate to the system whether this user interface element should respond to user input.
- [func accessibilityHitTest(CGPoint) -> Any?](sknode/accessibilityhittest(_:).md)
  Returns the frontmost user interface element in the element hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/accessibilityrole)*