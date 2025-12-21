# BEAccessibilityContainerType

**Framework**: BrowserEngineKit  
**Kind**: struct

An enumeration that indicates the type of container in which an element is located.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS ?+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct BEAccessibilityContainerType
```

#### Overview

Set a value from this enumeration for an element’s [`browserAccessibilityContainerType`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/browserAccessibilityContainerType) property to indicate the type of container in which the element is located. For example, set [`table`](beaccessibilitycontainertype/table.md) as the `browserAccessibilityContainerType` for an element within a table cell.

## Topics

### Container types
- [static var landmark: BEAccessibilityContainerType](beaccessibilitycontainertype/landmark.md)
  A website accessibility landmark contains the element.
- [static var table: BEAccessibilityContainerType](beaccessibilitycontainertype/table.md)
  A table contains the element.
- [static var list: BEAccessibilityContainerType](beaccessibilitycontainertype/list.md)
  A list contains the element.
- [static var fieldset: BEAccessibilityContainerType](beaccessibilitycontainertype/fieldset.md)
  An HTML fieldset element contains the element.
- [static var dialog: BEAccessibilityContainerType](beaccessibilitycontainertype/dialog.md)
  A dialog contains the element.
- [static var tree: BEAccessibilityContainerType](beaccessibilitycontainertype/tree.md)
  A tree contains the element.
- [static var frame: BEAccessibilityContainerType](beaccessibilitycontainertype/frame.md)
  A frame contains the element.
- [static var article: BEAccessibilityContainerType](beaccessibilitycontainertype/article.md)
  An HTML article element contains the alert.
- [static var semanticGroup: BEAccessibilityContainerType](beaccessibilitycontainertype/semanticgroup.md)
  A semantic group contains the element.
- [static var scrollArea: BEAccessibilityContainerType](beaccessibilitycontainertype/scrollarea.md)
  A scroll area contains the element.
- [static var alert: BEAccessibilityContainerType](beaccessibilitycontainertype/alert.md)
  An alert contains the element.
- [static var descriptionList: BEAccessibilityContainerType](beaccessibilitycontainertype/descriptionlist.md)
  A description list contains the element.
### Initializers
- [init(rawValue: UInt)](beaccessibilitycontainertype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [protocol BEAccessibilityTextMarkerSupport](beaccessibilitytextmarkersupport.md)
  A set of methods that provide information about text offsets to support assistive features.
- [static var valueChangedNotification: UIAccessibility.Notification](beaccessibility/valuechangednotification.md)
  The notification you post when the value of an element changes.
- [static var selectionChangedNotification: UIAccessibility.Notification](beaccessibility/selectionchangednotification.md)
  The notification you post when the selection inside an element changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitycontainertype)*