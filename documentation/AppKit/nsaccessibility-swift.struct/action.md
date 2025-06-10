# NSAccessibility.Action

**Framework**: AppKit  
**Kind**: struct

Constants that describe types of actions.

**Availability**:
- macOS ?+

## Declaration

```swift
struct Action
```

## Topics

### Actions
- [static let cancel: NSAccessibility.Action](nsaccessibility-swift.struct/action/cancel.md)
  An action that cancels the operation.
- [static let confirm: NSAccessibility.Action](nsaccessibility-swift.struct/action/confirm.md)
  An action that simulates pressing Return in the object, such as a text field.
- [static let decrement: NSAccessibility.Action](nsaccessibility-swift.struct/action/decrement.md)
  An action that decrements the value of the object.
- [static let delete: NSAccessibility.Action](nsaccessibility-swift.struct/action/delete.md)
  An action that deletes the value of the object.
- [static let increment: NSAccessibility.Action](nsaccessibility-swift.struct/action/increment.md)
  An action that increments the value of the object.
- [static let pick: NSAccessibility.Action](nsaccessibility-swift.struct/action/pick.md)
  An action that selects the object, such as a menu item.
- [static let press: NSAccessibility.Action](nsaccessibility-swift.struct/action/press.md)
  An action that simulates clicking an object, such as a button.
- [static let raise: NSAccessibility.Action](nsaccessibility-swift.struct/action/raise.md)
  An action that simulates bringing a window forward by clicking on its title bar.
- [static let showAlternateUI: NSAccessibility.Action](nsaccessibility-swift.struct/action/showalternateui.md)
  An action that shows an alternate UI, for example, during a mouse-hover event.
- [static let showDefaultUI: NSAccessibility.Action](nsaccessibility-swift.struct/action/showdefaultui.md)
  An action that shows the original or default UI; for example, during a mouse-hover event.
- [static let showMenu: NSAccessibility.Action](nsaccessibility-swift.struct/action/showmenu.md)
  An action that simulates showing a menu by clicking on it.
### Descriptions
- [var description: String?](nsaccessibility-swift.struct/action/description.md)
  Returns a standard description for an action.
### Initializers
- [init(String)](nsaccessibility-swift.struct/action/init(_:).md)
- [init(rawValue: String)](nsaccessibility-swift.struct/action/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSAccessibility.AnnotationAttributeKey](nsaccessibility-swift.struct/annotationattributekey.md)
  Keys for annotation attributes.
- [enum NSAccessibilityAnnotationPosition](nsaccessibilityannotationposition.md)
  Constants that specify the position where the annotation applies.
- [NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute.md)
  Constants that describe attributes.
- [NSAccessibility.FontAttributeKey](nsaccessibility-swift.struct/fontattributekey.md)
  Keys for font attributes.
- [enum NSAccessibilityOrientation](nsaccessibilityorientation.md)
  Values that indicate the orientation of accessibility elements, such as scroll bars and split views.
- [NSAccessibility.OrientationValue](nsaccessibility-swift.struct/orientationvalue.md)
  Values that indicate the orientation of user interface elements, such as scroll bars and split views.
- [NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute.md)
  Values that describe parameterized attributes.
- [NSAccessibility.Role](nsaccessibility-swift.struct/role.md)
  Values that describe types of objects that accessibility elements represent.
- [enum NSAccessibilityRulerMarkerType](nsaccessibilityrulermarkertype.md)
  Values that indicate the marker type of an accessibility element.
- [NSAccessibility.RulerMarkerTypeValue](nsaccessibility-swift.struct/rulermarkertypevalue.md)
  Values that describe ruler marker types.
- [NSAccessibility.RulerUnitValue](nsaccessibility-swift.struct/rulerunitvalue.md)
  Values that indicate the unit values of a ruler or layout area.
- [NSAccessibility.SortDirectionValue](nsaccessibility-swift.struct/sortdirectionvalue.md)
  Values that indicate the sort direction of a column.
- [enum NSAccessibilitySortDirection](nsaccessibilitysortdirection.md)
  Values that indicate the sort direction of a column.
- [NSAccessibility.Subrole](nsaccessibility-swift.struct/subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.
- [enum NSAccessibilityUnits](nsaccessibilityunits.md)
  Values that indicate the unit values of a ruler or layout area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/action)*