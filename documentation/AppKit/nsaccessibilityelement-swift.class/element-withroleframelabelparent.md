# element(withRole:frame:label:parent:)

**Framework**: AppKit  
**Kind**: method

Instantiates and configures a new accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func element(withRole role: NSAccessibility.Role, frame: NSRect, label: String?, parent: Any?) -> Any
```

#### Return Value

A newly instantiated and initialized accessibility element.

#### Discussion

Alternatively, instead of calling this convenience method, you can create an accessibility element and set its [`accessibilityRole`](nsaccessibility-c.protocol/accessibilityrole.md), [`accessibilityLabel`](nsaccessibility-c.protocol/accessibilitylabel.md), and [`accessibilityParent`](nsaccessibility-c.protocol/accessibilityparent.md) properties. Regardless of how you create the accessibility element, you need to set its [`accessibilityFrameInParentSpace`](nsaccessibilityelement-swift.class/accessibilityframeinparentspace.md) property to ensure that the element’s frame is updated as its parent moves.

## Parameters

- `role`: The new element’s intended role. For a complete list of roles, see Roles.
- `frame`: The element’s frame in screen coordinates. Additionally, you need to set the element’s   property.
- `label`: A short description of the new element. Do not include the element’s type in the label (for example, use  , not  ). If possible, use a single word. To help ensure that accessibility clients such as VoiceOver read the label with the correct intonation, start the label with a capital letter. Do not put a period at the end. Always localize the label.
- `parent`: The new element’s parent in the accessibility hierarchy.

## See Also

- [func accessibilityAddChildElement(NSAccessibilityElement)](nsaccessibilityelement-swift.class/accessibilityaddchildelement(_:).md)
  Adds a child to the accessibility element in the accessibility hierarchy.
- [func accessibilityFrameInParentSpace() -> NSRect](nsaccessibilityelement-swift.class/accessibilityframeinparentspace.md)
  Returns the accessibility element’s frame in its parent’s coordinate system.
- [func setAccessibilityFrameInParentSpace(NSRect)](nsaccessibilityelement-swift.class/setaccessibilityframeinparentspace(_:).md)
  Sets the accessibility element’s frame in its parent’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelement-swift.class/element(withrole:frame:label:parent:))*