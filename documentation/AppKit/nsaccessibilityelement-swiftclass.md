# NSAccessibilityElement

**Framework**: AppKit  
**Kind**: class

The basic infrastructure necessary for interacting with an assistive app.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class NSAccessibilityElement
```

#### Overview

Create subclasses of the [`NSAccessibilityElement`](nsaccessibilityelement-swift.class.md) class to represent any of your user interface elements that don’t inherit from [`NSView`](nsview.md) or from one of the standard AppKit controls. This class represents your user interface element in the accessibility hierarchy and manages the details necessary for working with assistive apps.

To support accessibility features for a custom user interface element:

1. Create your [`NSAccessibilityElement`](nsaccessibilityelement-swift.class.md) subclass by using [`element(withRole:frame:label:parent:)`](nsaccessibilityelement-swift.class/element(withrole:frame:label:parent:).md). You can also set these values using [`setAccessibilityRole(_:)`](nsaccessibilityprotocol/setaccessibilityrole(_:).md), [`setAccessibilityLabel(_:)`](nsaccessibilityprotocol/setaccessibilitylabel(_:).md) and [`setAccessibilityParent(_:)`](nsaccessibilityprotocol/setaccessibilityparent(_:).md).
2. Call the parent’s [`accessibilityAddChildElement(_:)`](nsaccessibilityelement-swift.class/accessibilityaddchildelement(_:).md) method to add your subclass. You can also add the subclass to its parent’s [`accessibilityChildren`](nsaccessibility-c.protocol/accessibilitychildren.md) array using [`setAccessibilityChildren(_:)`](nsaccessibilityprotocol/setaccessibilitychildren(_:).md).
3. In your subclass, call [`setAccessibilityFrameInParentSpace(_:)`](nsaccessibilityelement-swift.class/setaccessibilityframeinparentspace(_:).md). This ensures that your control moves with its superview.
4. In your subclass, adopt a role-specific protocol, customize the role, and post notifications just as you would handle any other accessible control. See [`Custom Controls`](custom-controls.md).
5. In your subclass, implement any additional properties and methods you may need to use to further customize your user interface element’s accessibility behavior. See [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md).

## Topics

### Supporting the Accessibility Hierarchy
- [class func element(withRole: NSAccessibility.Role, frame: NSRect, label: String?, parent: Any?) -> Any](nsaccessibilityelement-swift.class/element(withrole:frame:label:parent:).md)
  Instantiates and configures a new accessibility element.
- [func accessibilityAddChildElement(NSAccessibilityElement)](nsaccessibilityelement-swift.class/accessibilityaddchildelement(_:).md)
  Adds a child to the accessibility element in the accessibility hierarchy.
- [func accessibilityFrameInParentSpace() -> NSRect](nsaccessibilityelement-swift.class/accessibilityframeinparentspace.md)
  Returns the accessibility element’s frame in its parent’s coordinate system.
- [func setAccessibilityFrameInParentSpace(NSRect)](nsaccessibilityelement-swift.class/setaccessibilityframeinparentspace(_:).md)
  Sets the accessibility element’s frame in its parent’s coordinate system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelement-swift.class)*