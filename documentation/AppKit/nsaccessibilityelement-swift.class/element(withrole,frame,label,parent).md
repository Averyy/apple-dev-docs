# element(withRole:frame:label:parent:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Instantiates and configures a new accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func element(withRole role: NSAccessibility.Role, frame: NSRect, label: String?, parent: Any?) -> Any
```

```objc
+ (id) accessibilityElementWithRole:(NSAccessibilityRole) role frame:(NSRect) frame label:(NSString *) label parent:(id) parent;
```

## Return Value

A newly instantiated and initialized accessibility element.

## Discussion

Alternatively, instead of calling this convenience method, you can create an accessibility element and set its [`accessibilityRole`](../nsaccessibility-c.protocol/accessibilityrole.md), [`accessibilityLabel`](../nsaccessibility-c.protocol/accessibilitylabel.md), and [`accessibilityParent`](../nsaccessibility-c.protocol/accessibilityparent.md) properties. Regardless of how you create the accessibility element, you need to set its [`accessibilityFrameInParentSpace`](./accessibilityframeinparentspace.md) property to ensure that the element’s frame is updated as its parent moves.

## Parameters

- `role`: The new element’s intended role. For a complete list of roles, see Roles.

  > **Note**:  Your subclass also needs to adopt the role-based protocol that corresponds with this role.
- `frame`: The element’s frame in screen coordinates. Additionally, you need to set the element’s [`accessibilityFrameInParentSpace`](./accessibilityframeinparentspace.md) property.

  > **Note**:  The [`accessibilityFrameInParentSpace`](./accessibilityframeinparentspace.md) property ensures that the element’s frame is updated as its parent moves.
- `label`: A short description of the new element. Do not include the element’s type in the label (for example, use `Play`, not `Play button`). If possible, use a single word. To help ensure that accessibility clients such as VoiceOver read the label with the correct intonation, start the label with a capital letter. Do not put a period at the end. Always localize the label.
- `parent`: The new element’s parent in the accessibility hierarchy.

## See Also

### Supporting the Accessibility Hierarchy
- [func accessibilityAddChildElement(NSAccessibilityElement)](./accessibilityaddchildelement%28_%29.md)
  Adds a child to the accessibility element in the accessibility hierarchy.
- [func accessibilityFrameInParentSpace() -> NSRect](./accessibilityframeinparentspace%28%29.md)
  Returns the accessibility element’s frame in its parent’s coordinate system.
- [func setAccessibilityFrameInParentSpace(NSRect)](./setaccessibilityframeinparentspace%28_%29.md)
  Sets the accessibility element’s frame in its parent’s coordinate system.
- [accessibilityFrameInParentSpace](./accessibilityframeinparentspace.md)
  The accessibility element’s frame in its parent’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelement-swift.class/element(withrole:frame:label:parent:))*