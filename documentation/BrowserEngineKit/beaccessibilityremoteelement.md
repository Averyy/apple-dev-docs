# BEAccessibilityRemoteElement

**Framework**: BrowserEngineKit  
**Kind**: class

A class that shares the accessibility information of a peripheral process with the main process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class BEAccessibilityRemoteElement
```

#### Overview

If a peripheral process in your browser app (such as a web content process or extension process) provides Accessibility elements, you can use this class to connect the Accessibility element hierarchies across the two processes so that assistive technologies such as VoiceOver, Switch Control, and Voice Control can interact with both hierarchies.

Create an instance of this class in the peripheral process and pass in the same identifier you use to create a [`BEAccessibilityRemoteHostElement`](beaccessibilityremotehostelement.md) instance on the main process. Add elements to the [`accessibilityElements`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/accessibilityElements) method return value of the instance of this class to enable assistive technologies to simultaneously access both Accessibility element hierarchies.

> **Note**: Unlike [`BEAccessibilityRemoteHostElement`](beaccessibilityremotehostelement.md), you don’t add an instance of this class to the [`accessibilityElements`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/accessibilityElements) method return value for a member of your view hierarchy.

## Topics

### Creating a remote element
- [init(identifier: String, hostPid: pid_t)](beaccessibilityremoteelement/init(identifier:hostpid:).md)
  Initializes and registers a remote element.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol BEAccessibilityTextMarkerSupport](beaccessibilitytextmarkersupport.md)
  A set of methods that provide information about text offsets to support assistive features.
- [static var valueChangedNotification: UIAccessibility.Notification](beaccessibility/valuechangednotification.md)
  A notification you post when the value of an element changes.
- [static var selectionChangedNotification: UIAccessibility.Notification](beaccessibility/selectionchangednotification.md)
  A notification you post when the selection inside an element changes.
- [struct BEAccessibilityContainerType](beaccessibilitycontainertype.md)
  Types of containers for an element.
- [enum BEAccessibilityPressedState](beaccessibilitypressedstate.md)
  An enumeration that indicates whether an element is pressed.
- [static var menuItem: UIAccessibilityTraits](beaccessibility/menuitem.md)
  An accessibility element with a menu interface.
- [static var popUpButton: UIAccessibilityTraits](beaccessibility/popupbutton.md)
  An accessibility element with a pop-up button interface.
- [static var radioButton: UIAccessibilityTraits](beaccessibility/radiobutton.md)
  An accessibility element with a radio button interface.
- [static var readOnly: UIAccessibilityTraits](beaccessibility/readonly.md)
  An accessibility element with a read-only interface.
- [static var visited: UIAccessibilityTraits](beaccessibility/visited.md)
  An accessibility element that resembles a visited link.
- [class BEAccessibilityRemoteHostElement](beaccessibilityremotehostelement.md)
  A class that connects the accessibility information of different processes.
- [struct BEAccessibility](beaccessibility.md)
  A category for accessibility features in the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilityremoteelement)*