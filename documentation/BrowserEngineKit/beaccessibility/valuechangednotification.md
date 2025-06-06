# valueChangedNotification

**Framework**: BrowserEngineKit  
**Kind**: property

The notification you post when the value of an element changes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
static var valueChangedNotification: UIAccessibility.Notification
```

#### Overview

Post this notification when the value of an input element changes, when someone or a script adds text to a text control or removes text from a text control, or when the `aria-valuenow` or `aria-valuetext` attributes of an element change.

If an element contains a text selection and the content changes, or the editing cursor position changes, post this notification followed by [`selectionChangedNotification`](beaccessibility/selectionchangednotification.md) for the element.

## See Also

- [protocol BEAccessibilityTextMarkerSupport](beaccessibilitytextmarkersupport.md)
  A set of methods that provide information about text offsets to support assistive features.
- [static var selectionChangedNotification: UIAccessibility.Notification](beaccessibility/selectionchangednotification.md)
  The notification you post when the selection inside an element changes.
- [struct BEAccessibilityContainerType](beaccessibilitycontainertype.md)
  An enumeration that indicates the type of container in which an element is located.
- [enum BEAccessibilityPressedState](beaccessibilitypressedstate.md)
  An enumeration that indicates whether an element is pressed.
- [static var menuItem: UIAccessibilityTraits](beaccessibility/menuitem.md)
  The accessibility element behaves like a menu item.
- [static var popUpButton: UIAccessibilityTraits](beaccessibility/popupbutton.md)
  The accessibility element behaves like a pop-up button.
- [static var radioButton: UIAccessibilityTraits](beaccessibility/radiobutton.md)
  The accessibility element behaves like a radio button.
- [static var readOnly: UIAccessibilityTraits](beaccessibility/readonly.md)
  The accessibility element is read-only.
- [static var visited: UIAccessibilityTraits](beaccessibility/visited.md)
  The accessibility element behaves like a link that someone previously visited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibility/valuechangednotification)*