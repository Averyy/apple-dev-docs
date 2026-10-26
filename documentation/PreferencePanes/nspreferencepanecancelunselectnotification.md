# NSPreferencePaneCancelUnselectNotification

**Framework**: Preference Panes  
**Kind**: var  
**Role**: Global Variable

Notifies observers that the preference pane should not be deselected.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```c
extern NSString * const NSPreferencePaneCancelUnselectNotification;
```

#### Discussion

Posted when [`reply(toShouldUnselect:)`](./nspreferencepane/reply%28toshouldunselect%29.md) is invoked with an argument of [`false`](../Swift/false.md) after [`shouldUnselect`](./nspreferencepane/shouldunselect.md) has returned a value of [`NSPreferencePaneUnselectReply.unselectLater`](./nspreferencepaneunselectreply/unselectlater.md).

## See Also

### Notifications
- [NSPreferencePrefPaneIsAvailableNotification](./nspreferenceprefpaneisavailablenotification.md)
  Notifies observers that the system preferences app is available to display your preferences.
- [NSPreferencePaneDoUnselectNotification](./nspreferencepanedounselectnotification.md)
  Notifies observers that the preference pane may be deselected.
- [NSPreferencePaneSwitchToPaneNotification](./nspreferencepaneswitchtopanenotification.md)
  Notifies observers that the user selected a new preference pane.
- [NSPreferencePaneUpdateHelpMenuNotification](./nspreferencepaneupdatehelpmenunotification.md)
  Notifies observers that your help menu content changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepanecancelunselectnotification)*