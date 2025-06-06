# comboBoxSelectionIsChanging(_:)

**Framework**: AppKit  
**Kind**: method

Informs the delegate that the pop-up list selection is changing.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func comboBoxSelectionIsChanging(_ notification: Notification)
```

## Parameters

- `notification`: A notification named  .

## See Also

- [func comboBoxSelectionDidChange(Notification)](nscomboboxdelegate/comboboxselectiondidchange(_:).md)
  Informs the delegate that the pop-up list selection has finished changing.
- [func comboBoxWillDismiss(Notification)](nscomboboxdelegate/comboboxwilldismiss(_:).md)
  Informs the delegate that the pop-up list is about to be dismissed.
- [func comboBoxWillPopUp(Notification)](nscomboboxdelegate/comboboxwillpopup(_:).md)
  Informs the delegate that the pop-up list is about to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdelegate/comboboxselectionischanging(_:))*