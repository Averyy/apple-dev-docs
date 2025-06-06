# comboBoxWillPopUp(_:)

**Framework**: AppKit  
**Kind**: method

Informs the delegate that the pop-up list is about to be displayed.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func comboBoxWillPopUp(_ notification: Notification)
```

## Parameters

- `notification`: A notification named  .

## See Also

- [func comboBoxSelectionDidChange(Notification)](nscomboboxdelegate/comboboxselectiondidchange(_:).md)
  Informs the delegate that the pop-up list selection has finished changing.
- [func comboBoxSelectionIsChanging(Notification)](nscomboboxdelegate/comboboxselectionischanging(_:).md)
  Informs the delegate that the pop-up list selection is changing.
- [func comboBoxWillDismiss(Notification)](nscomboboxdelegate/comboboxwilldismiss(_:).md)
  Informs the delegate that the pop-up list is about to be dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdelegate/comboboxwillpopup(_:))*