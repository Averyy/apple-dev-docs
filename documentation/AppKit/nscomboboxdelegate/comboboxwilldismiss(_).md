# comboBoxWillDismiss(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate that the pop-up list is about to be dismissed.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func comboBoxWillDismiss(_ notification: Notification)
```

```objc
- (void) comboBoxWillDismiss:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`willDismissNotification`](../nscombobox/willdismissnotification.md).

## See Also

### Manipulating the selection
- [func comboBoxSelectionDidChange(Notification)](./comboboxselectiondidchange%28_%29.md)
  Informs the delegate that the pop-up list selection has finished changing.
- [func comboBoxSelectionIsChanging(Notification)](./comboboxselectionischanging%28_%29.md)
  Informs the delegate that the pop-up list selection is changing.
- [func comboBoxWillPopUp(Notification)](./comboboxwillpopup%28_%29.md)
  Informs the delegate that the pop-up list is about to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdelegate/comboboxwilldismiss(_:))*