# BEAccessibilityPressedState

**Framework**: BrowserEngineKit  
**Kind**: enum

An enumeration that indicates whether an element is pressed.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS ?+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum BEAccessibilityPressedState
```

## Topics

### Element states
- [BEAccessibilityPressedState.false](beaccessibilitypressedstate/false.md)
  The element isn’t pressed.
- [BEAccessibilityPressedState.true](beaccessibilitypressedstate/true.md)
  The element is pressed.
- [BEAccessibilityPressedState.mixed](beaccessibilitypressedstate/mixed.md)
  The element is in a mixed state.
- [BEAccessibilityPressedState.undefined](beaccessibilitypressedstate/undefined.md)
  The element is in an undefined state.
### Initializers
- [init?(rawValue: Int)](beaccessibilitypressedstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol BEAccessibilityTextMarkerSupport](beaccessibilitytextmarkersupport.md)
  A set of methods that provide information about text offsets to support assistive features.
- [static var valueChangedNotification: UIAccessibility.Notification](beaccessibility/valuechangednotification.md)
  The notification you post when the value of an element changes.
- [static var selectionChangedNotification: UIAccessibility.Notification](beaccessibility/selectionchangednotification.md)
  The notification you post when the selection inside an element changes.
- [struct BEAccessibilityContainerType](beaccessibilitycontainertype.md)
  An enumeration that indicates the type of container in which an element is located.
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

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitypressedstate)*