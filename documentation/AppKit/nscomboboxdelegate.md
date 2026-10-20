# NSComboBoxDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods implemented by delegates of combo box objects.

**Availability**:
- macOS

## Declaration

```swift
protocol NSComboBoxDelegate : NSTextFieldDelegate
```

```objc
@protocol NSComboBoxDelegate <NSTextFieldDelegate>
```

## Topics

### Manipulating the selection
- [func comboBoxSelectionDidChange(Notification)](./nscomboboxdelegate/comboboxselectiondidchange%28_%29.md)
  Informs the delegate that the pop-up list selection has finished changing.
- [func comboBoxSelectionIsChanging(Notification)](./nscomboboxdelegate/comboboxselectionischanging%28_%29.md)
  Informs the delegate that the pop-up list selection is changing.
- [func comboBoxWillDismiss(Notification)](./nscomboboxdelegate/comboboxwilldismiss%28_%29.md)
  Informs the delegate that the pop-up list is about to be dismissed.
- [func comboBoxWillPopUp(Notification)](./nscomboboxdelegate/comboboxwillpopup%28_%29.md)
  Informs the delegate that the pop-up list is about to be displayed.

## Relationships

### Inherits From
- [NSControlTextEditingDelegate](./nscontroltexteditingdelegate.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTextFieldDelegate](./nstextfielddelegate.md)

## See Also

### Management
- [protocol NSComboBoxDataSource](./nscomboboxdatasource.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdelegate)*