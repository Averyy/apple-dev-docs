# willDismissNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.

**Availability**:
- macOS

## Declaration

```swift
class let willDismissNotification: NSNotification.Name
```

```c
extern NSNotificationName NSComboBoxWillDismissNotification;
```

#### Discussion

The notification object is the `NSComboBox` whose pop-up list will be dismissed. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSComboBox.WillDismissMessage`](./willdismissmessage.md).

## See Also

### Notifications
- [class let selectionDidChangeNotification: NSNotification.Name](./selectiondidchangenotification.md)
  Posted after the pop-up list selection of the `NSComboBox` changes.
- [class let selectionIsChangingNotification: NSNotification.Name](./selectionischangingnotification.md)
  Posted whenever the pop-up list selection of the `NSComboBox` is changing.
- [class let willPopUpNotification: NSNotification.Name](./willpopupnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/willdismissnotification)*