# BEAccessibilityRemoteHostElement

**Framework**: BrowserEngineKit  
**Kind**: class

A class that connects the accessibility information of different processes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class BEAccessibilityRemoteHostElement
```

#### Overview

If a peripheral process in your browser app (such as a web content process or extension process) provides Accessibility elements in addition to your app’s main process, this class can connect the Accessibility element hierarchies across the two processes so that assistive technologies such as VoiceOver, Switch Control, and Voice Control can interact with both hierarchies.

Create an instance of this class in the main process and pass in the same identifier you use to create a [`BEAccessibilityRemoteElement`](beaccessibilityremoteelement.md) instance in the peripheral process. Add the instance of this class to the [`accessibilityElements`](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityelements) return value of an element’s parent view, and set the instance’s [`accessibilityContainer`](beaccessibilityremotehostelement/accessibilitycontainer.md) property to the parent view.

## Topics

### Creating a remote host element
- [init(identifier: String, remotePid: pid_t)](beaccessibilityremotehostelement/init(identifier:remotepid:).md)
  Initializes a remote element in the hosting process.
### Accessing containers
- [var accessibilityContainer: AnyObject?](beaccessibilityremotehostelement/accessibilitycontainer.md)
  The remote host’s parent Accessibility element.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

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
- [class BEAccessibilityRemoteElement](beaccessibilityremoteelement.md)
  A class that shares the accessibility information of a peripheral process with the main process.
- [struct BEAccessibility](beaccessibility.md)
  A category for accessibility features in the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilityremotehostelement)*