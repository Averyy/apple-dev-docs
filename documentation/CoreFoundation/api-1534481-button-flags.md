# Button Flags

**Framework**: Core Foundation  
**Role**: API Collection

Flags that alter the display of buttons in a user notification dialog.

#### Overview

You specify these flags when you create the user notification with [`CFUserNotificationCreate(_:_:_:_:_:)`](./cfusernotificationcreate%28_,_,_,_,_%29.md).

## Topics

### Constants
- [var kCFUserNotificationNoDefaultButtonFlag: CFOptionFlags](./kcfusernotificationnodefaultbuttonflag.md)
  Displays the dialog without the default, alternate, or other buttons.
- [var kCFUserNotificationUseRadioButtonsFlag: CFOptionFlags](./kcfusernotificationuseradiobuttonsflag.md)
  Creates a group of radio buttons instead of checkboxes for the elements in the [`kCFUserNotificationCheckBoxTitlesKey`](./kcfusernotificationcheckboxtitleskey.md) array in the user notification’s description dictionary.

## See Also

### Constants
- [Alert Levels](./api-1534483-alert-levels.md)
  Flags identifying the seriousness of a user notification.
- [Response Codes](./api-1534504-response-codes.md)
  Response codes identifying the button that was pressed to dismiss a notification dialog.
- [Alert Levels](./api-1534483-alert-levels.md)
  Flags identifying the seriousness of a user notification.
- [Response Codes](./api-1534504-response-codes.md)
  Response codes identifying the button that was pressed to dismiss a notification dialog.
- [Dialog Description Keys](./dialog-description-keys.md)
  Keys used in a user notification’s description dictionary, which describes the contents of the notification dialog to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/1534481-button-flags)*