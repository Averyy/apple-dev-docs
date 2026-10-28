# NSPreferencePaneCancelUnselect

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Notifies observers that the preference pane should not be deselected.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let NSPreferencePaneCancelUnselect: NSNotification.Name
```

## Discussion

Posted when [`reply(toShouldUnselect:)`](../../../PreferencePanes/nspreferencepane/reply%28toshouldunselect%29.md) is invoked with an argument of [`false`](../../../Swift/false.md) after [`shouldUnselect`](../../../PreferencePanes/nspreferencepane/shouldunselect.md) has returned a value of [`NSPreferencePaneUnselectReply.unselectLater`](../../../PreferencePanes/nspreferencepaneunselectreply/unselectlater.md).

## See Also

### PreferencePanes
- [static let NSPreferencePaneDoUnselect: NSNotification.Name](./nspreferencepanedounselect.md)
  Notifies observers that the preference pane may be deselected.
- [static let NSPreferencePaneSwitchToPane: NSNotification.Name](./nspreferencepaneswitchtopane.md)
  Notifies observers that the user selected a new preference pane.
- [static let NSPreferencePaneUpdateHelpMenu: NSNotification.Name](./nspreferencepaneupdatehelpmenu.md)
  Notifies observers that your help menu content changed.
- [static let NSPreferencePrefPaneIsAvailable: NSNotification.Name](./nspreferenceprefpaneisavailable.md)
  Notifies observers that the system preferences app is available to display your preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspreferencepanecancelunselect)*