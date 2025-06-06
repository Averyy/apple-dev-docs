# NSAccessibility

**Framework**: AppKit  
**Kind**: struct

A namespace for accessibility symbols for AppKit apps.

**Availability**:
- macOS ?+

## Declaration

```swift
struct NSAccessibility
```

## Topics

### Posting Notifications
- [static func post(element: Any, notification: NSAccessibility.Notification)](nsaccessibility-swift.struct/post(element:notification:).md)
  Sends a notification to any observing assistive apps.
- [static func post(element: Any, notification: NSAccessibility.Notification, userInfo: [NSAccessibility.NotificationUserInfoKey : Any]?)](nsaccessibility-swift.struct/post(element:notification:userinfo:).md)
  Sends a notification and an optional user info dictionary to any observing assistive apps.
### Getting Accessibility Objects
- [static func unignoredAncestor(of: Any) -> Any?](nsaccessibility-swift.struct/unignoredancestor(of:).md)
  Returns an unignored accessibility object, ascending the hierarchy, if necessary.
- [static func unignoredChildren(from: [Any]) -> [Any]](nsaccessibility-swift.struct/unignoredchildren(from:).md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredChildrenForOnlyChild(from: Any) -> [Any]](nsaccessibility-swift.struct/unignoredchildrenforonlychild(from:).md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredDescendant(of: Any) -> Any?](nsaccessibility-swift.struct/unignoreddescendant(of:).md)
  Returns an unignored accessibility object, descending the hierarchy, if necessary.
### Getting Screen Coordinates
- [static func screenPoint(fromView: NSView, point: NSPoint) -> NSPoint](nsaccessibility-swift.struct/screenpoint(fromview:point:).md)
  Returns the point in screen coordinates.
- [static func screenRect(fromView: NSView, rect: NSRect) -> NSRect](nsaccessibility-swift.struct/screenrect(fromview:rect:).md)
  Returns the frame in screen coordinates.
### Specifying Protected Content
- [static func setMayContainProtectedContent(Bool) -> Bool](nsaccessibility-swift.struct/setmaycontainprotectedcontent(_:).md)
  Sets whether the app may have protected content.
### Handling Errors
- [static let ErrorCodeExceptionInfo: String](nsaccessibility-swift.struct/errorcodeexceptioninfo.md)
  An integer error code for debugging.
### Using Accessibility Types
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
- [NSAccessibility.NotificationUserInfoKey](nsaccessibility-swift.struct/notificationuserinfokey.md)
  The key in the user info dictionary for a notification.
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
### Deprecated
- [static func raiseBadArgumentException(Any!, NSAccessibility.Attribute!, Any!)](nsaccessibility-swift.struct/raisebadargumentexception(_:_:_:).md)
  Raises an error if the parameter is the wrong type or has an illegal value

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [protocol NSAccessibilityProtocol](nsaccessibilityprotocol.md)
  The complete list of properties and methods for accessible elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct)*