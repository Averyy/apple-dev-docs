# selectionIsChangingNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted whenever the pop-up list selection of the `NSComboBox` is changing.

**Availability**:
- macOS

## Declaration

```swift
class let selectionIsChangingNotification: NSNotification.Name
```

```c
extern NSNotificationName NSComboBoxSelectionIsChangingNotification;
```

## Discussion

The notification object is the `NSComboBox` whose selection is changing. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSComboBox.SelectionIsChangingMessage`](./selectionischangingmessage.md).

## See Also

### Notifications
- [class let selectionDidChangeNotification: NSNotification.Name](./selectiondidchangenotification.md)
  Posted after the pop-up list selection of the `NSComboBox` changes.
- [class let willDismissNotification: NSNotification.Name](./willdismissnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.
- [class let willPopUpNotification: NSNotification.Name](./willpopupnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/selectionischangingnotification)*