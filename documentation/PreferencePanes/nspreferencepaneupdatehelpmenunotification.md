# NSPreferencePaneUpdateHelpMenuNotification

**Framework**: Preference Panes  
**Kind**: var  
**Role**: Global Variable

Notifies observers that your help menu content changed.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```c
extern NSString * const NSPreferencePaneUpdateHelpMenuNotification;
```

## Discussion

The object of the notification is an array of dictionaries containing the new help menu contents.

## See Also

### Notifications
- [NSPreferencePrefPaneIsAvailableNotification](./nspreferenceprefpaneisavailablenotification.md)
  Notifies observers that the system preferences app is available to display your preferences.
- [NSPreferencePaneDoUnselectNotification](./nspreferencepanedounselectnotification.md)
  Notifies observers that the preference pane may be deselected.
- [NSPreferencePaneCancelUnselectNotification](./nspreferencepanecancelunselectnotification.md)
  Notifies observers that the preference pane should not be deselected.
- [NSPreferencePaneSwitchToPaneNotification](./nspreferencepaneswitchtopanenotification.md)
  Notifies observers that the user selected a new preference pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepaneupdatehelpmenunotification)*