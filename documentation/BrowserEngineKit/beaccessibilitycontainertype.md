# BEAccessibilityContainerType

**Framework**: BrowserEngineKit  
**Kind**: struct

Types of containers for an element.

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

Choose a value from this enumeration and set it as an element’s [`browserAccessibilityContainerType`](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/browseraccessibilitycontainertype) to indicate the element’s container.

For example, set [`table`](beaccessibilitycontainertype/table.md) as the `browserAccessibilityContainerType` for an element within a table cell.

## Topics

### Layout and navigation
- [static var landmark: BEAccessibilityContainerType](beaccessibilitycontainertype/landmark.md)
  A website accessibility landmark that contains the element.
- [static var frame: BEAccessibilityContainerType](beaccessibilitycontainertype/frame.md)
  A frame that contains the element.
- [static var scrollArea: BEAccessibilityContainerType](beaccessibilitycontainertype/scrollarea.md)
  A scroll area that contains the element.
- [static var semanticGroup: BEAccessibilityContainerType](beaccessibilitycontainertype/semanticgroup.md)
  A semantic group that contains the element.
### Content grouping
- [static var article: BEAccessibilityContainerType](beaccessibilitycontainertype/article.md)
  An HTML article element that contains the alert.
- [static var fieldset: BEAccessibilityContainerType](beaccessibilitycontainertype/fieldset.md)
  An HTML fieldset element that contains the element.
- [static var descriptionList: BEAccessibilityContainerType](beaccessibilitycontainertype/descriptionlist.md)
  A description list that contains the element.
- [static var list: BEAccessibilityContainerType](beaccessibilitycontainertype/list.md)
  A list contains the element.
- [static var table: BEAccessibilityContainerType](beaccessibilitycontainertype/table.md)
  A table that contains the element.
- [static var tree: BEAccessibilityContainerType](beaccessibilitycontainertype/tree.md)
  A tree that contains the element.
### Interactive and dynamic
- [static var alert: BEAccessibilityContainerType](beaccessibilitycontainertype/alert.md)
  An alert that contains the element.
- [static var dialog: BEAccessibilityContainerType](beaccessibilitycontainertype/dialog.md)
  A dialog that contains the element.
### Initializers
- [init(rawValue: UInt)](beaccessibilitycontainertype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [protocol BEAccessibilityTextMarkerSupport](beaccessibilitytextmarkersupport.md)
  A set of methods that provide information about text offsets to support assistive features.
- [static var valueChangedNotification: UIAccessibility.Notification](beaccessibility/valuechangednotification.md)
  A notification you post when the value of an element changes.
- [static var selectionChangedNotification: UIAccessibility.Notification](beaccessibility/selectionchangednotification.md)
  A notification you post when the selection inside an element changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitycontainertype)*