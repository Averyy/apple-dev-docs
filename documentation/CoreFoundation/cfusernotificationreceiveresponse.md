# CFUserNotificationReceiveResponse(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Waits for the user to respond to a notification or for the notification to time out.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func CFUserNotificationReceiveResponse(_ userNotification: CFUserNotification!, _ timeout: CFTimeInterval, _ responseFlags: UnsafeMutablePointer<CFOptionFlags>!) -> Int32
```

#### Return Value

`0` if the call successfully received a response; a non-`0` value otherwise.

#### Discussion

Use this function to poll a user notification for a user response. You can call it any number of times on the same user notification.

To avoid polling and blocking your thread’s execution, you can create a run loop source for the user notification with [`CFUserNotificationCreateRunLoopSource(_:_:_:_:)`](cfusernotificationcreaterunloopsource(_:_:_:_:).md). You will then receive a callback when the dialog is dismissed.

## Parameters

- `userNotification`: The user notification to use.
- `timeout`: The amount of time to wait for the user to respond to   or for the notification to time out. If neither happens before   passes, this function returns a non-  value. If   is  , the function blocks until the user notification is dismissed.
- `responseFlags`: On return, contains flags identifying how the notification was dismissed, the state of any checkboxes, and the selected element of the pop-up menu. Bits 0-1 of the value hold an identifier for the button pressed by the user (see  ). Extract the identifier by performing a bitwise-AND operation with  . Bits 8-15 of   hold the state of up to 8 checkboxes or radio buttons, if present. Extract the flags by performing bitwise-AND operations with the return value of  . Bits 24-31 hold the index number of the element selected in a pop-up menu, if present. Extract the index by performing a 24-bit right shift:  .

## See Also

- [func CFUserNotificationCancel(CFUserNotification!) -> Int32](cfusernotificationcancel(_:).md)
  Cancels a user notification dialog.
- [func CFUserNotificationCheckBoxChecked(CFIndex) -> CFOptionFlags](cfusernotificationcheckboxchecked(_:).md)
  Returns a flag used to set or test a checkbox’s state.
- [func CFUserNotificationCreate(CFAllocator!, CFTimeInterval, CFOptionFlags, UnsafeMutablePointer<Int32>!, CFDictionary!) -> CFUserNotification!](cfusernotificationcreate(_:_:_:_:_:).md)
  Creates a CFUserNotification object and displays its notification dialog on screen.
- [func CFUserNotificationCreateRunLoopSource(CFAllocator!, CFUserNotification!, CFUserNotificationCallBack!, CFIndex) -> CFRunLoopSource!](cfusernotificationcreaterunloopsource(_:_:_:_:).md)
  Creates a run loop source for a user notification.
- [func CFUserNotificationDisplayAlert(CFTimeInterval, CFOptionFlags, CFURL!, CFURL!, CFURL!, CFString!, CFString!, CFString!, CFString!, CFString!, UnsafeMutablePointer<CFOptionFlags>!) -> Int32](cfusernotificationdisplayalert(_:_:_:_:_:_:_:_:_:_:_:).md)
  Displays a user notification dialog and waits for a user response.
- [func CFUserNotificationDisplayNotice(CFTimeInterval, CFOptionFlags, CFURL!, CFURL!, CFURL!, CFString!, CFString!, CFString!) -> Int32](cfusernotificationdisplaynotice(_:_:_:_:_:_:_:_:).md)
  Displays a user notification dialog that does not need a user response.
- [func CFUserNotificationGetResponseDictionary(CFUserNotification!) -> CFDictionary!](cfusernotificationgetresponsedictionary(_:).md)
  Returns the dictionary containing all the text field values from a dismissed notification dialog.
- [func CFUserNotificationGetResponseValue(CFUserNotification!, CFString!, CFIndex) -> CFString!](cfusernotificationgetresponsevalue(_:_:_:).md)
  Extracts the values of the text fields from a dismissed notification dialog.
- [func CFUserNotificationGetTypeID() -> CFTypeID](cfusernotificationgettypeid().md)
  Returns the type identifier for the `CFUserNotification` opaque type.
- [func CFUserNotificationPopUpSelection(CFIndex) -> CFOptionFlags](cfusernotificationpopupselection(_:).md)
  Returns a flag used to set the selected element of a pop-up menu.
- [func CFUserNotificationSecureTextField(CFIndex) -> CFOptionFlags](cfusernotificationsecuretextfield(_:).md)
  Returns a flag used to set the secure state of a text field.
- [func CFUserNotificationUpdate(CFUserNotification!, CFTimeInterval, CFOptionFlags, CFDictionary!) -> Int32](cfusernotificationupdate(_:_:_:_:).md)
  Updates a displayed user notification dialog with new user interface information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfusernotificationreceiveresponse(_:_:_:))*