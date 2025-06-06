# NSAccessibility.Notification

**Framework**: AppKit  
**Kind**: struct

The name of the notification.

**Availability**:
- macOS ?+

## Declaration

```swift
struct Notification
```

## Topics

### Notification Names
- [static let announcementRequested: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/announcementrequested.md)
  This notification is posted whenever an accessibility element needs to make an announcement to the user. This notification requires a `userInfo` dictionary with the key [`announcement`](nsaccessibility-swift.struct/notificationuserinfokey/announcement.md) and a localized string containing the announcement. To help an assistive app determine the importance of the announcement, add the appropriate [`priority`](nsaccessibility-swift.struct/notificationuserinfokey/priority.md) to the `userInfo` dictionary.
- [static let applicationActivated: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/applicationactivated.md)
  This notification is posted after the app has been activated. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let applicationDeactivated: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/applicationdeactivated.md)
  This notification is posted after the app has been deactivated.  Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let applicationHidden: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/applicationhidden.md)
  This notification is posted after the app is hidden. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let applicationShown: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/applicationshown.md)
  This notification is posted after the app is shown. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let created: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/created.md)
  This notification is posted after an accessibility element is created. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let drawerCreated: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/drawercreated.md)
  This notification is posted after a drawer appears. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let focusedUIElementChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/focuseduielementchanged.md)
  This notification is posted after an accessibility element gains focus. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let focusedWindowChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/focusedwindowchanged.md)
  This notification is posted after the key window changes. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let helpTagCreated: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/helptagcreated.md)
  This notification is posted after a help tag appears. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let layoutChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/layoutchanged.md)
  This notification is posted after the UI changes in a way that requires the attention of an accessibility client. This notification should be accompanied by a `userInfo` dictionary with the key [`uiElements`](nsaccessibility-swift.struct/notificationuserinfokey/uielements.md) and an array containing the UI elements that have been added or changed. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let mainWindowChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/mainwindowchanged.md)
  This notification is posted after the main window changes. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let moved: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/moved.md)
  This notification is posted after an accessibility element moves. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let resized: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/resized.md)
  This notification is posted after an accessibility element’s size changes. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let rowCollapsed: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/rowcollapsed.md)
  This notification is posted after a row collapses. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let rowCountChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/rowcountchanged.md)
  This notification is posted after a row is added or deleted. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let rowExpanded: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/rowexpanded.md)
  This notification is posted after a row expands. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let selectedCellsChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/selectedcellschanged.md)
  This notification is posted after one or more cells in a cell-based table are selected or deselected. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let selectedChildrenChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/selectedchildrenchanged.md)
  This notification is posted after one or more child elements are selected or deselected. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let selectedChildrenMoved: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/selectedchildrenmoved.md)
  This notification is posted after the selected items in a layout area move. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let selectedColumnsChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/selectedcolumnschanged.md)
  This notification is posted after one or more columns are selected or deselected. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let selectedRowsChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/selectedrowschanged.md)
  This notification is posted after one or more rows are selected or deselected. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let selectedTextChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/selectedtextchanged.md)
  This notification is posted after text is selected or deselected.  Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let sheetCreated: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/sheetcreated.md)
  This notification is posted after a sheet appears.  Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let titleChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/titlechanged.md)
  This notification is posted after an accessibility element’s title changes. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let uiElementDestroyed: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/uielementdestroyed.md)
  This notification is posted after an accessibility element is destroyed. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let unitsChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/unitschanged.md)
  This notification is posted after the units in a layout area change. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let valueChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/valuechanged.md)
  This notification is posted after an accessibility element’s value changes. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let windowCreated: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/windowcreated.md)
  This notification is posted after a new window appears. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let windowDeminiaturized: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/windowdeminiaturized.md)
  This notification is posted after a window is restored to full size from the Dock.  Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let windowMiniaturized: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/windowminiaturized.md)
  This notification is posted after a window is put in the Dock. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let windowMoved: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/windowmoved.md)
  This notification is posted after a window moves.  Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let windowResized: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/windowresized.md)
  This notification is posted after a window’s size changes. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
### Initializers
- [init(rawValue: String)](nsaccessibility-swift.struct/notification/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSAccessibility.Action](nsaccessibility-swift.struct/action.md)
  Constants that describe types of actions.
- [NSAccessibility.AnnotationAttributeKey](nsaccessibility-swift.struct/annotationattributekey.md)
  Keys for annotation attributes.
- [NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute.md)
  Constants that describe attributes.
- [NSAccessibility.FontAttributeKey](nsaccessibility-swift.struct/fontattributekey.md)
  Keys for font attributes.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/notification)*