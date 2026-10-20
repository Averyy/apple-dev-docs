# NSAccessibility.Action

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that describe types of actions.

**Availability**:
- macOS

## Declaration

```swift
struct Action
```

```c
typedef NSString * NSAccessibilityActionName;
```

## Topics

### Actions
- [static let cancel: NSAccessibility.Action](./action/cancel.md)
  An action that cancels the operation.
- [static let confirm: NSAccessibility.Action](./action/confirm.md)
  An action that simulates pressing Return in the object, such as a text field.
- [static let decrement: NSAccessibility.Action](./action/decrement.md)
  An action that decrements the value of the object.
- [static let delete: NSAccessibility.Action](./action/delete.md)
  An action that deletes the value of the object.
- [static let increment: NSAccessibility.Action](./action/increment.md)
  An action that increments the value of the object.
- [static let pick: NSAccessibility.Action](./action/pick.md)
  An action that selects the object, such as a menu item.
- [static let press: NSAccessibility.Action](./action/press.md)
  An action that simulates clicking an object, such as a button.
- [static let raise: NSAccessibility.Action](./action/raise.md)
  An action that simulates bringing a window forward by clicking on its title bar.
- [static let scrollToVisibleAction: NSAccessibility.Action](./action/scrolltovisibleaction.md)
- [static let showAlternateUI: NSAccessibility.Action](./action/showalternateui.md)
  An action that shows an alternate UI, for example, during a mouse-hover event.
- [static let showDefaultUI: NSAccessibility.Action](./action/showdefaultui.md)
  An action that shows the original or default UI; for example, during a mouse-hover event.
- [static let showMenu: NSAccessibility.Action](./action/showmenu.md)
  An action that simulates showing a menu by clicking on it.
### Descriptions
- [var description: String?](./action/description.md)
  Returns a standard description for an action.
### Initializers
- [init(String)](./action/init%28_%29.md)
- [init(rawValue: String)](./action/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessibility Types
- [NSAccessibility.AnnotationAttributeKey](./annotationattributekey.md)
  Keys for annotation attributes.
- [enum NSAccessibilityAnnotationPosition](../nsaccessibilityannotationposition.md)
  Constants that specify the position where the annotation applies.
- [NSAccessibility.Attribute](./attribute.md)
  Constants that describe attributes.
- [NSAccessibility.FontAttributeKey](./fontattributekey.md)
  Keys for font attributes.
- [enum NSAccessibilityOrientation](../nsaccessibilityorientation.md)
  Values that indicate the orientation of accessibility elements, such as scroll bars and split views.
- [NSAccessibility.OrientationValue](./orientationvalue.md)
  Values that indicate the orientation of user interface elements, such as scroll bars and split views.
- [NSAccessibility.ParameterizedAttribute](./parameterizedattribute.md)
  Values that describe parameterized attributes.
- [NSAccessibility.Role](./role.md)
  Values that describe types of objects that accessibility elements represent.
- [enum NSAccessibilityRulerMarkerType](../nsaccessibilityrulermarkertype.md)
  Values that indicate the marker type of an accessibility element.
- [NSAccessibility.RulerMarkerTypeValue](./rulermarkertypevalue.md)
  Values that describe ruler marker types.
- [NSAccessibility.RulerUnitValue](./rulerunitvalue.md)
  Values that indicate the unit values of a ruler or layout area.
- [NSAccessibility.SortDirectionValue](./sortdirectionvalue.md)
  Values that indicate the sort direction of a column.
- [enum NSAccessibilitySortDirection](../nsaccessibilitysortdirection.md)
  Values that indicate the sort direction of a column.
- [NSAccessibility.Subrole](./subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.
- [enum NSAccessibilityUnits](../nsaccessibilityunits.md)
  Values that indicate the unit values of a ruler or layout area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/action)*