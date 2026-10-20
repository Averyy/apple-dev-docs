# comboBoxSelectionDidChange(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate that the pop-up list selection has finished changing.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func comboBoxSelectionDidChange(_ notification: Notification)
```

```objc
- (void) comboBoxSelectionDidChange:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named  [`selectionDidChangeNotification`](../nscombobox/selectiondidchangenotification.md).

## See Also

### Related Documentation
- [func comboBoxSelectionIsChanging(Notification)](./comboboxselectionischanging%28_%29.md)
  Informs the delegate that the pop-up list selection is changing.
### Manipulating the selection
- [func comboBoxSelectionIsChanging(Notification)](./comboboxselectionischanging%28_%29.md)
  Informs the delegate that the pop-up list selection is changing.
- [func comboBoxWillDismiss(Notification)](./comboboxwilldismiss%28_%29.md)
  Informs the delegate that the pop-up list is about to be dismissed.
- [func comboBoxWillPopUp(Notification)](./comboboxwillpopup%28_%29.md)
  Informs the delegate that the pop-up list is about to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdelegate/comboboxselectiondidchange(_:))*