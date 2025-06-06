# NSComboBoxDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of optional methods implemented by delegates of combo box objects.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSComboBoxDelegate : NSTextFieldDelegate
```

## Topics

### Manipulating the selection
- [func comboBoxSelectionDidChange(Notification)](nscomboboxdelegate/comboboxselectiondidchange(_:).md)
  Informs the delegate that the pop-up list selection has finished changing.
- [func comboBoxSelectionIsChanging(Notification)](nscomboboxdelegate/comboboxselectionischanging(_:).md)
  Informs the delegate that the pop-up list selection is changing.
- [func comboBoxWillDismiss(Notification)](nscomboboxdelegate/comboboxwilldismiss(_:).md)
  Informs the delegate that the pop-up list is about to be dismissed.
- [func comboBoxWillPopUp(Notification)](nscomboboxdelegate/comboboxwillpopup(_:).md)
  Informs the delegate that the pop-up list is about to be displayed.

## Relationships

### Inherits From
- [NSControlTextEditingDelegate](nscontroltexteditingdelegate.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTextFieldDelegate](nstextfielddelegate.md)

## See Also

- [protocol NSComboBoxDataSource](nscomboboxdatasource.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdelegate)*