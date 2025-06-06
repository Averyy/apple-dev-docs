# kCFUserNotificationNoDefaultButtonFlag

**Framework**: Core Foundation  
**Kind**: var

Displays the dialog without the default, alternate, or other buttons.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var kCFUserNotificationNoDefaultButtonFlag: CFOptionFlags { get }
```

#### Discussion

The dialog remains on screen until it times out or you cancel it with [`CFUserNotificationCancel(_:)`](cfusernotificationcancel(_:).md). If you provide a title for the default button in the user notification’s description dictionary, this flag is ignored and buttons show up normally.

## See Also

- [var kCFUserNotificationUseRadioButtonsFlag: CFOptionFlags](kcfusernotificationuseradiobuttonsflag.md)
  Creates a group of radio buttons instead of checkboxes for the elements in the [`kCFUserNotificationCheckBoxTitlesKey`](kcfusernotificationcheckboxtitleskey.md) array in the user notification’s description dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfusernotificationnodefaultbuttonflag)*