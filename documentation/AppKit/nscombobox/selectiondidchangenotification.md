# selectionDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted after the pop-up list selection of the `NSComboBox` changes.

**Availability**:
- macOS

## Declaration

```swift
class let selectionDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName NSComboBoxSelectionDidChangeNotification;
```

## Discussion

The notification object is the `NSComboBox` whose selection changed. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSComboBox.SelectionDidChangeMessage`](./selectiondidchangemessage.md).

## See Also

### Notifications
- [class let selectionIsChangingNotification: NSNotification.Name](./selectionischangingnotification.md)
  Posted whenever the pop-up list selection of the `NSComboBox` is changing.
- [class let willDismissNotification: NSNotification.Name](./willdismissnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.
- [class let willPopUpNotification: NSNotification.Name](./willpopupnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/selectiondidchangenotification)*