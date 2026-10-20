# NSAccessibility.NotificationUserInfoKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The key in the user info dictionary for a notification.

**Availability**:
- macOS

## Declaration

```swift
struct NotificationUserInfoKey
```

```c
typedef NSString * NSAccessibilityNotificationUserInfoKey;
```

## Topics

### Constants
- [static let announcement: NSAccessibility.NotificationUserInfoKey](./notificationuserinfokey/announcement.md)
  The announcement as a localized string.
- [static let uiElements: NSAccessibility.NotificationUserInfoKey](./notificationuserinfokey/uielements.md)
  An array of elements for the notification.
- [static let priority: NSAccessibility.NotificationUserInfoKey](./notificationuserinfokey/priority.md)
  A priority level that can help an assistive app determine how to handle the corresponding notification.
- [enum NSAccessibilityPriorityLevel](../nsaccessibilityprioritylevel.md)
  A data type for notification priority levels.
### Initializers
- [init(rawValue: String)](./notificationuserinfokey/init%28rawvalue%29.md)
  Returns a new notification object with a specified name and object.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Using Accessibility Types
- [NSAccessibility.Action](./action.md)
  Constants that describe types of actions.
- [NSAccessibility.AnnotationAttributeKey](./annotationattributekey.md)
  Keys for annotation attributes.
- [NSAccessibility.Attribute](./attribute.md)
  Constants that describe attributes.
- [NSAccessibility.FontAttributeKey](./fontattributekey.md)
  Keys for font attributes.
- [NSAccessibility.Notification](./notification.md)
  The name of the notification.
- [NSAccessibility.OrientationValue](./orientationvalue.md)
  Values that indicate the orientation of user interface elements, such as scroll bars and split views.
- [NSAccessibility.ParameterizedAttribute](./parameterizedattribute.md)
  Values that describe parameterized attributes.
- [NSAccessibility.Role](./role.md)
  Values that describe types of objects that accessibility elements represent.
- [NSAccessibility.RulerMarkerTypeValue](./rulermarkertypevalue.md)
  Values that describe ruler marker types.
- [NSAccessibility.RulerUnitValue](./rulerunitvalue.md)
  Values that indicate the unit values of a ruler or layout area.
- [NSAccessibility.SortDirectionValue](./sortdirectionvalue.md)
  Values that indicate the sort direction of a column.
- [NSAccessibility.Subrole](./subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/notificationuserinfokey)*