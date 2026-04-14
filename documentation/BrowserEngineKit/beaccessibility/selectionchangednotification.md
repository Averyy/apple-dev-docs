# selectionChangedNotification

**Framework**: BrowserEngineKit  
**Kind**: property

A notification you post when the selection inside an element changes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
static var selectionChangedNotification: UIAccessibility.Notification
```

#### Discussion

If an element contains a text selection and the content changes, or the editing cursor position changes, post this notification after posting [`valueChangedNotification`](beaccessibility/valuechangednotification.md) for the element.

## See Also

- [protocol BEAccessibilityTextMarkerSupport](beaccessibilitytextmarkersupport.md)
  A set of methods that provide information about text offsets to support assistive features.
- [static var valueChangedNotification: UIAccessibility.Notification](beaccessibility/valuechangednotification.md)
  A notification you post when the value of an element changes.
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
- [class BEAccessibilityRemoteHostElement](beaccessibilityremotehostelement.md)
  A class that connects the accessibility information of different processes.
- [struct BEAccessibility](beaccessibility.md)
  A category for accessibility features in the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibility/selectionchangednotification)*