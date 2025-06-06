# selectionDidChangeNotification

**Framework**: AppKit  
**Kind**: property

Posted after the pop-up list selection of the `NSComboBox` changes.

**Availability**:
- macOS ?+

## Declaration

```swift
class let selectionDidChangeNotification: NSNotification.Name
```

#### Discussion

The notification object is the `NSComboBox` whose selection changed. This notification does not contain a `userInfo` dictionary.

## See Also

- [class let selectionIsChangingNotification: NSNotification.Name](nscombobox/selectionischangingnotification.md)
  Posted whenever the pop-up list selection of the `NSComboBox` is changing.
- [class let willDismissNotification: NSNotification.Name](nscombobox/willdismissnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.
- [class let willPopUpNotification: NSNotification.Name](nscombobox/willpopupnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/selectiondidchangenotification)*