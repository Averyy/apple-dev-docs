# comboBoxWillDismiss(_:)

**Framework**: AppKit  
**Kind**: method

Informs the delegate that the pop-up list is about to be dismissed.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func comboBoxWillDismiss(_ notification: Notification)
```

## Parameters

- `notification`: A notification named  .

## See Also

- [func comboBoxSelectionDidChange(Notification)](nscomboboxdelegate/comboboxselectiondidchange(_:).md)
  Informs the delegate that the pop-up list selection has finished changing.
- [func comboBoxSelectionIsChanging(Notification)](nscomboboxdelegate/comboboxselectionischanging(_:).md)
  Informs the delegate that the pop-up list selection is changing.
- [func comboBoxWillPopUp(Notification)](nscomboboxdelegate/comboboxwillpopup(_:).md)
  Informs the delegate that the pop-up list is about to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdelegate/comboboxwilldismiss(_:))*