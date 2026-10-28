# willPopUpNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.

**Availability**:
- macOS

## Declaration

```swift
class let willPopUpNotification: NSNotification.Name
```

```c
extern NSNotificationName NSComboBoxWillPopUpNotification;
```

## Discussion

The notification object is the `NSComboBox` whose pop-up window will be displayed. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSComboBox.WillPopUpMessage`](./willpopupmessage.md).

## See Also

### Notifications
- [class let selectionDidChangeNotification: NSNotification.Name](./selectiondidchangenotification.md)
  Posted after the pop-up list selection of the `NSComboBox` changes.
- [class let selectionIsChangingNotification: NSNotification.Name](./selectionischangingnotification.md)
  Posted whenever the pop-up list selection of the `NSComboBox` is changing.
- [class let willDismissNotification: NSNotification.Name](./willdismissnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/willpopupnotification)*