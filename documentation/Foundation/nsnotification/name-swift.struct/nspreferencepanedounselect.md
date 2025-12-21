# NSPreferencePaneDoUnselect

**Framework**: Foundation  
**Kind**: property

Notifies observers that the preference pane may be deselected.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let NSPreferencePaneDoUnselect: NSNotification.Name
```

#### Discussion

Posted when [`reply(toShouldUnselect:)`](https://developer.apple.com/documentation/PreferencePanes/NSPreferencePane/reply(toShouldUnselect:)) is invoked with an argument of [`true`](https://developer.apple.com/documentation/Swift/true) after [`shouldUnselect`](https://developer.apple.com/documentation/PreferencePanes/NSPreferencePane/shouldUnselect) has returned a value of [`NSPreferencePaneUnselectReply.unselectLater`](https://developer.apple.com/documentation/PreferencePanes/NSPreferencePaneUnselectReply/unselectLater).

## See Also

- [static let NSPreferencePaneCancelUnselect: NSNotification.Name](nsnotification/name-swift.struct/nspreferencepanecancelunselect.md)
  Notifies observers that the preference pane should not be deselected.
- [static let NSPreferencePaneSwitchToPane: NSNotification.Name](nsnotification/name-swift.struct/nspreferencepaneswitchtopane.md)
  Notifies observers that the user selected a new preference pane.
- [static let NSPreferencePaneUpdateHelpMenu: NSNotification.Name](nsnotification/name-swift.struct/nspreferencepaneupdatehelpmenu.md)
  Notifies observers that your help menu content changed.
- [static let NSPreferencePrefPaneIsAvailable: NSNotification.Name](nsnotification/name-swift.struct/nspreferenceprefpaneisavailable.md)
  Notifies observers that the system preferences app is available to display your preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspreferencepanedounselect)*