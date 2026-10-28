# NSPreferencePaneUpdateHelpMenu

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Notifies observers that your help menu content changed.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let NSPreferencePaneUpdateHelpMenu: NSNotification.Name
```

## Discussion

The object of the notification is an array of dictionaries containing the new help menu contents.

## See Also

### PreferencePanes
- [static let NSPreferencePaneCancelUnselect: NSNotification.Name](./nspreferencepanecancelunselect.md)
  Notifies observers that the preference pane should not be deselected.
- [static let NSPreferencePaneDoUnselect: NSNotification.Name](./nspreferencepanedounselect.md)
  Notifies observers that the preference pane may be deselected.
- [static let NSPreferencePaneSwitchToPane: NSNotification.Name](./nspreferencepaneswitchtopane.md)
  Notifies observers that the user selected a new preference pane.
- [static let NSPreferencePrefPaneIsAvailable: NSNotification.Name](./nspreferenceprefpaneisavailable.md)
  Notifies observers that the system preferences app is available to display your preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspreferencepaneupdatehelpmenu)*