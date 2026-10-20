# comboBoxWillPopUp(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate that the pop-up list is about to be displayed.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func comboBoxWillPopUp(_ notification: Notification)
```

```objc
- (void) comboBoxWillPopUp:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`willPopUpNotification`](../nscombobox/willpopupnotification.md).

## See Also

### Manipulating the selection
- [func comboBoxSelectionDidChange(Notification)](./comboboxselectiondidchange%28_%29.md)
  Informs the delegate that the pop-up list selection has finished changing.
- [func comboBoxSelectionIsChanging(Notification)](./comboboxselectionischanging%28_%29.md)
  Informs the delegate that the pop-up list selection is changing.
- [func comboBoxWillDismiss(Notification)](./comboboxwilldismiss%28_%29.md)
  Informs the delegate that the pop-up list is about to be dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdelegate/comboboxwillpopup(_:))*