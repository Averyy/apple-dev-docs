# NSAccessibility.Notification

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The name of the notification.

**Availability**:
- macOS

## Declaration

```swift
struct Notification
```

```c
typedef NSString * NSAccessibilityNotificationName;
```

## Topics

### Notification names
- [static let announcementRequested: NSAccessibility.Notification](./notification/announcementrequested.md)
  This notification posts when an app needs to make an announcement to the user. If VoiceOver is enabled, it’s presented via speech and/or braille. Otherwise, it does nothing.
- [static let applicationActivated: NSAccessibility.Notification](./notification/applicationactivated.md)
  This notification is posted after the app has been activated. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let applicationDeactivated: NSAccessibility.Notification](./notification/applicationdeactivated.md)
  This notification is posted after the app has been deactivated.  Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let applicationHidden: NSAccessibility.Notification](./notification/applicationhidden.md)
  This notification is posted after the app is hidden. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let applicationShown: NSAccessibility.Notification](./notification/applicationshown.md)
  This notification is posted after the app is shown. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let created: NSAccessibility.Notification](./notification/created.md)
  This notification is posted after an accessibility element is created. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let drawerCreated: NSAccessibility.Notification](./notification/drawercreated.md)
  This notification is posted after a drawer appears. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let focusedUIElementChanged: NSAccessibility.Notification](./notification/focuseduielementchanged.md)
  This notification is posted after an accessibility element gains focus. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let focusedWindowChanged: NSAccessibility.Notification](./notification/focusedwindowchanged.md)
  This notification is posted after the key window changes. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let helpTagCreated: NSAccessibility.Notification](./notification/helptagcreated.md)
  This notification is posted after a help tag appears. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let layoutChanged: NSAccessibility.Notification](./notification/layoutchanged.md)
  This notification is posted after the UI changes in a way that requires the attention of an accessibility client. This notification should be accompanied by a `userInfo` dictionary with the key [`uiElements`](./notificationuserinfokey/uielements.md) and an array containing the UI elements that have been added or changed. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let mainWindowChanged: NSAccessibility.Notification](./notification/mainwindowchanged.md)
  This notification is posted after the main window changes. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let moved: NSAccessibility.Notification](./notification/moved.md)
  This notification is posted after an accessibility element moves. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let resized: NSAccessibility.Notification](./notification/resized.md)
  This notification is posted after an accessibility element’s size changes. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let rowCollapsed: NSAccessibility.Notification](./notification/rowcollapsed.md)
  This notification is posted after a row collapses. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let rowCountChanged: NSAccessibility.Notification](./notification/rowcountchanged.md)
  This notification is posted after a row is added or deleted. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let rowExpanded: NSAccessibility.Notification](./notification/rowexpanded.md)
  This notification is posted after a row expands. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let selectedCellsChanged: NSAccessibility.Notification](./notification/selectedcellschanged.md)
  This notification is posted after one or more cells in a cell-based table are selected or deselected. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let selectedChildrenChanged: NSAccessibility.Notification](./notification/selectedchildrenchanged.md)
  This notification is posted after one or more child elements are selected or deselected. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let selectedChildrenMoved: NSAccessibility.Notification](./notification/selectedchildrenmoved.md)
  This notification is posted after the selected items in a layout area move. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let selectedColumnsChanged: NSAccessibility.Notification](./notification/selectedcolumnschanged.md)
  This notification is posted after one or more columns are selected or deselected. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let selectedRowsChanged: NSAccessibility.Notification](./notification/selectedrowschanged.md)
  This notification is posted after one or more rows are selected or deselected. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let selectedTextChanged: NSAccessibility.Notification](./notification/selectedtextchanged.md)
  This notification is posted after text is selected or deselected.  Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let sheetCreated: NSAccessibility.Notification](./notification/sheetcreated.md)
  This notification is posted after a sheet appears.  Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let titleChanged: NSAccessibility.Notification](./notification/titlechanged.md)
  This notification is posted after an accessibility element’s title changes. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let uiElementDestroyed: NSAccessibility.Notification](./notification/uielementdestroyed.md)
  This notification is posted after an accessibility element is destroyed. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let unitsChanged: NSAccessibility.Notification](./notification/unitschanged.md)
  This notification is posted after the units in a layout area change. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let valueChanged: NSAccessibility.Notification](./notification/valuechanged.md)
  This notification is posted after an accessibility element’s value changes. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let windowCreated: NSAccessibility.Notification](./notification/windowcreated.md)
  This notification is posted after a new window appears. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let windowDeminiaturized: NSAccessibility.Notification](./notification/windowdeminiaturized.md)
  This notification is posted after a window is restored to full size from the Dock.  Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let windowMiniaturized: NSAccessibility.Notification](./notification/windowminiaturized.md)
  This notification is posted after a window is put in the Dock. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let windowMoved: NSAccessibility.Notification](./notification/windowmoved.md)
  This notification is posted after a window moves.  Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let windowResized: NSAccessibility.Notification](./notification/windowresized.md)
  This notification is posted after a window’s size changes. Post this notification using the [`post(element:notification:)`](./post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
### Accessibility notification names
- [static let NSAccessibilityAutocorrectionOccurred: NSAccessibility.Notification](./notification/nsaccessibilityautocorrectionoccurred.md)
- [static let NSAccessibilityDraggingDestinationDragAccepted: NSAccessibility.Notification](./notification/nsaccessibilitydraggingdestinationdragaccepted.md)
- [static let NSAccessibilityDraggingDestinationDragNotAccepted: NSAccessibility.Notification](./notification/nsaccessibilitydraggingdestinationdragnotaccepted.md)
- [static let NSAccessibilityDraggingDestinationDropAllowed: NSAccessibility.Notification](./notification/nsaccessibilitydraggingdestinationdropallowed.md)
- [static let NSAccessibilityDraggingDestinationDropNotAllowed: NSAccessibility.Notification](./notification/nsaccessibilitydraggingdestinationdropnotallowed.md)
- [static let NSAccessibilityDraggingSourceDragBegan: NSAccessibility.Notification](./notification/nsaccessibilitydraggingsourcedragbegan.md)
- [static let NSAccessibilityDraggingSourceDragEnded: NSAccessibility.Notification](./notification/nsaccessibilitydraggingsourcedragended.md)
- [static let NSAccessibilityTextInputMarkingSessionBegan: NSAccessibility.Notification](./notification/nsaccessibilitytextinputmarkingsessionbegan.md)
- [static let NSAccessibilityTextInputMarkingSessionEnded: NSAccessibility.Notification](./notification/nsaccessibilitytextinputmarkingsessionended.md)
### Initializers
- [init(rawValue: String)](./notification/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

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
- [NSAccessibility.NotificationUserInfoKey](./notificationuserinfokey.md)
  The key in the user info dictionary for a notification.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/notification)*