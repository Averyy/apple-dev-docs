# NSAccessibility.NotificationUserInfoKey

**Framework**: AppKit  
**Kind**: struct

The key in the user info dictionary for a notification.

**Availability**:
- macOS ?+

## Declaration

```swift
struct NotificationUserInfoKey
```

## Topics

### Constants
- [static let announcement: NSAccessibility.NotificationUserInfoKey](nsaccessibility-swift.struct/notificationuserinfokey/announcement.md)
  The announcement as a localized string.
- [static let uiElements: NSAccessibility.NotificationUserInfoKey](nsaccessibility-swift.struct/notificationuserinfokey/uielements.md)
  An array of elements for the notification.
- [static let priority: NSAccessibility.NotificationUserInfoKey](nsaccessibility-swift.struct/notificationuserinfokey/priority.md)
  A priority level that can help an assistive app determine how to handle the corresponding notification.
- [enum NSAccessibilityPriorityLevel](nsaccessibilityprioritylevel.md)
  A data type for notification priority levels.
### Initializers
- [init(rawValue: String)](nsaccessibility-swift.struct/notificationuserinfokey/init(rawvalue:).md)
  Returns a new notification object with a specified name and object.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSAccessibility.Action](nsaccessibility-swift.struct/action.md)
  Constants that describe types of actions.
- [NSAccessibility.AnnotationAttributeKey](nsaccessibility-swift.struct/annotationattributekey.md)
  Keys for annotation attributes.
- [NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute.md)
  Constants that describe attributes.
- [NSAccessibility.FontAttributeKey](nsaccessibility-swift.struct/fontattributekey.md)
  Keys for font attributes.
- [NSAccessibility.Notification](nsaccessibility-swift.struct/notification.md)
  The name of the notification.
- [NSAccessibility.OrientationValue](nsaccessibility-swift.struct/orientationvalue.md)
  Values that indicate the orientation of user interface elements, such as scroll bars and split views.
- [NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute.md)
  Values that describe parameterized attributes.
- [NSAccessibility.Role](nsaccessibility-swift.struct/role.md)
  Values that describe types of objects that accessibility elements represent.
- [NSAccessibility.RulerMarkerTypeValue](nsaccessibility-swift.struct/rulermarkertypevalue.md)
  Values that describe ruler marker types.
- [NSAccessibility.RulerUnitValue](nsaccessibility-swift.struct/rulerunitvalue.md)
  Values that indicate the unit values of a ruler or layout area.
- [NSAccessibility.SortDirectionValue](nsaccessibility-swift.struct/sortdirectionvalue.md)
  Values that indicate the sort direction of a column.
- [NSAccessibility.Subrole](nsaccessibility-swift.struct/subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/notificationuserinfokey)*