# selectionIsChangingNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever the pop-up list selection of the `NSComboBox` is changing.

**Availability**:
- macOS ?+

## Declaration

```swift
class let selectionIsChangingNotification: NSNotification.Name
```

#### Discussion

The notification object is the `NSComboBox` whose selection is changing. This notification does not contain a `userInfo` dictionary.

## See Also

- [class let selectionDidChangeNotification: NSNotification.Name](nscombobox/selectiondidchangenotification.md)
  Posted after the pop-up list selection of the `NSComboBox` changes.
- [class let willDismissNotification: NSNotification.Name](nscombobox/willdismissnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.
- [class let willPopUpNotification: NSNotification.Name](nscombobox/willpopupnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/selectionischangingnotification)*