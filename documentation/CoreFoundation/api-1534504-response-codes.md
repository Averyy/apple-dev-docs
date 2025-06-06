# Response Codes

**Framework**: Core Foundation

Response codes identifying the button that was pressed to dismiss a notification dialog.

#### Overview

To extract this value from the response flags of a dismissed notification (such as returned by [`CFUserNotificationReceiveResponse(_:_:_:)`](cfusernotificationreceiveresponse(_:_:_:).md)), you must perform a bitwise-AND operation between the returned response flags and `0x3` before comparing the value to these constants.

## Topics

### Constants
- [var kCFUserNotificationDefaultResponse: CFOptionFlags](kcfusernotificationdefaultresponse.md)
  The default button was pressed.
- [var kCFUserNotificationAlternateResponse: CFOptionFlags](kcfusernotificationalternateresponse.md)
  The alternate button was pressed.
- [var kCFUserNotificationOtherResponse: CFOptionFlags](kcfusernotificationotherresponse.md)
  The third button was pressed.
- [var kCFUserNotificationCancelResponse: CFOptionFlags](kcfusernotificationcancelresponse.md)
  No button was pressed and the notification timed out.

## See Also

- [Alert Levels](1534483-alert-levels.md)
  Flags identifying the seriousness of a user notification.
- [Button Flags](1534481-button-flags.md)
  Flags that alter the display of buttons in a user notification dialog.
- [Alert Levels](1534483-alert-levels.md)
  Flags identifying the seriousness of a user notification.
- [Button Flags](1534481-button-flags.md)
  Flags that alter the display of buttons in a user notification dialog.
- [Dialog Description Keys](dialog-description-keys.md)
  Keys used in a user notification’s description dictionary, which describes the contents of the notification dialog to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/1534504-response-codes)*