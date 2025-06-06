# comboBoxSelectionDidChange(_:)

**Framework**: AppKit  
**Kind**: method

Informs the delegate that the pop-up list selection has finished changing.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func comboBoxSelectionDidChange(_ notification: Notification)
```

## Parameters

- `notification`: A notification named   .

## See Also

- [Combo Box Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ComboBox/ComboBox.html#//apple_ref/doc/uid/10000020i)
- [func comboBoxSelectionIsChanging(Notification)](nscomboboxdelegate/comboboxselectionischanging(_:).md)
  Informs the delegate that the pop-up list selection is changing.
- [func comboBoxWillDismiss(Notification)](nscomboboxdelegate/comboboxwilldismiss(_:).md)
  Informs the delegate that the pop-up list is about to be dismissed.
- [func comboBoxWillPopUp(Notification)](nscomboboxdelegate/comboboxwillpopup(_:).md)
  Informs the delegate that the pop-up list is about to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdelegate/comboboxselectiondidchange(_:))*