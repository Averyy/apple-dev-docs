# NSAccessibilityElement

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

The basic infrastructure necessary for interacting with an assistive app.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class NSAccessibilityElement
```

```objc
@interface NSAccessibilityElement : NSObject
```

## Overview

Create subclasses of the [`NSAccessibilityElement`](./nsaccessibilityelement-swift.class.md) class to represent any of your user interface elements that don’t inherit from [`NSView`](./nsview.md) or from one of the standard AppKit controls. This class represents your user interface element in the accessibility hierarchy and manages the details necessary for working with assistive apps.

To support accessibility features for a custom user interface element:

1. Create your [`NSAccessibilityElement`](./nsaccessibilityelement-swift.class.md) subclass by using [`element(withRole:frame:label:parent:)`](./nsaccessibilityelement-swift.class/element%28withrole,frame,label,parent%29.md). You can also set these values using [`setAccessibilityRole(_:)`](./nsaccessibilityprotocol/setaccessibilityrole%28_%29.md), [`setAccessibilityLabel(_:)`](./nsaccessibilityprotocol/setaccessibilitylabel%28_%29.md) and [`setAccessibilityParent(_:)`](./nsaccessibilityprotocol/setaccessibilityparent%28_%29.md).
2. Call the parent’s [`accessibilityAddChildElement(_:)`](./nsaccessibilityelement-swift.class/accessibilityaddchildelement%28_%29.md) method to add your subclass. You can also add the subclass to its parent’s [`accessibilityChildren`](./nsaccessibility-c.protocol/accessibilitychildren.md) array using [`setAccessibilityChildren(_:)`](./nsaccessibilityprotocol/setaccessibilitychildren%28_%29.md).
3. In your subclass, call [`setAccessibilityFrameInParentSpace(_:)`](./nsaccessibilityelement-swift.class/setaccessibilityframeinparentspace%28_%29.md). This ensures that your control moves with its superview.
4. In your subclass, adopt a role-specific protocol, customize the role, and post notifications just as you would handle any other accessible control. See [Custom Controls](./custom-controls.md).
5. In your subclass, implement any additional properties and methods you may need to use to further customize your user interface element’s accessibility behavior. See [`NSAccessibilityProtocol`](./nsaccessibilityprotocol.md).

## Topics

### Supporting the Accessibility Hierarchy
- [class func element(withRole: NSAccessibility.Role, frame: NSRect, label: String?, parent: Any?) -> Any](./nsaccessibilityelement-swift.class/element%28withrole,frame,label,parent%29.md)
  Instantiates and configures a new accessibility element.
- [func accessibilityAddChildElement(NSAccessibilityElement)](./nsaccessibilityelement-swift.class/accessibilityaddchildelement%28_%29.md)
  Adds a child to the accessibility element in the accessibility hierarchy.
- [func accessibilityFrameInParentSpace() -> NSRect](./nsaccessibilityelement-swift.class/accessibilityframeinparentspace%28%29.md)
  Returns the accessibility element’s frame in its parent’s coordinate system.
- [func setAccessibilityFrameInParentSpace(NSRect)](./nsaccessibilityelement-swift.class/setaccessibilityframeinparentspace%28_%29.md)
  Sets the accessibility element’s frame in its parent’s coordinate system.
- [accessibilityFrameInParentSpace](./nsaccessibilityelement-swift.class/accessibilityframeinparentspace.md)
  The accessibility element’s frame in its parent’s coordinate system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityelement-swift.class)*