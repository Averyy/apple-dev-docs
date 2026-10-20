# comboBoxSelectionIsChanging(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate that the pop-up list selection is changing.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func comboBoxSelectionIsChanging(_ notification: Notification)
```

```objc
- (void) comboBoxSelectionIsChanging:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`selectionIsChangingNotification`](../nscombobox/selectionischangingnotification.md).

## See Also

### Manipulating the selection
- [func comboBoxSelectionDidChange(Notification)](./comboboxselectiondidchange%28_%29.md)
  Informs the delegate that the pop-up list selection has finished changing.
- [func comboBoxWillDismiss(Notification)](./comboboxwilldismiss%28_%29.md)
  Informs the delegate that the pop-up list is about to be dismissed.
- [func comboBoxWillPopUp(Notification)](./comboboxwillpopup%28_%29.md)
  Informs the delegate that the pop-up list is about to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdelegate/comboboxselectionischanging(_:))*