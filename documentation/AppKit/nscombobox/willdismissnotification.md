# willDismissNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.

**Availability**:
- macOS ?+

## Declaration

```swift
class let willDismissNotification: NSNotification.Name
```

#### Discussion

The notification object is the `NSComboBox` whose pop-up list will be dismissed. This notification does not contain a `userInfo` dictionary.

## See Also

- [class let selectionDidChangeNotification: NSNotification.Name](nscombobox/selectiondidchangenotification.md)
  Posted after the pop-up list selection of the `NSComboBox` changes.
- [class let selectionIsChangingNotification: NSNotification.Name](nscombobox/selectionischangingnotification.md)
  Posted whenever the pop-up list selection of the `NSComboBox` is changing.
- [class let willPopUpNotification: NSNotification.Name](nscombobox/willpopupnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/willdismissnotification)*