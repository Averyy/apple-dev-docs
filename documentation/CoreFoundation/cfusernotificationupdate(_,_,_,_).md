# CFUserNotificationUpdate(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Updates a displayed user notification dialog with new user interface information.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func CFUserNotificationUpdate(_ userNotification: CFUserNotification!, _ timeout: CFTimeInterval, _ flags: CFOptionFlags, _ dictionary: CFDictionary!) -> Int32
```

```c
extern SInt32 CFUserNotificationUpdate(CFUserNotificationRef userNotification, CFTimeInterval timeout, CFOptionFlags flags, CFDictionaryRef dictionary);
```

## Return Value

`0` if the cancel was successful; a non-`0` value otherwise.

## Parameters

- `userNotification`: The user notification to update.
- `timeout`: The new timeout value for the dialog.
- `flags`: A set of flags describing the type of notification to display. See [`CFUserNotificationCreate(_:_:_:_:_:)`](./cfusernotificationcreate%28_,_,_,_,_%29.md) for details.
- `dictionary`: A description of the elements to display in the notification dialog. The possible keys are listed in [Dialog Description Keys](./dialog-description-keys.md).

## See Also

### CFUserNotification Miscellaneous Functions
- [func CFUserNotificationCancel(CFUserNotification!) -> Int32](./cfusernotificationcancel%28_%29.md)
  Cancels a user notification dialog.
- [func CFUserNotificationCheckBoxChecked(CFIndex) -> CFOptionFlags](./cfusernotificationcheckboxchecked%28_%29.md)
  Returns a flag used to set or test a checkbox’s state.
- [func CFUserNotificationCreate(CFAllocator!, CFTimeInterval, CFOptionFlags, UnsafeMutablePointer<Int32>!, CFDictionary!) -> CFUserNotification!](./cfusernotificationcreate%28_,_,_,_,_%29.md)
  Creates a CFUserNotification object and displays its notification dialog on screen.
- [func CFUserNotificationCreateRunLoopSource(CFAllocator!, CFUserNotification!, CFUserNotificationCallBack!, CFIndex) -> CFRunLoopSource!](./cfusernotificationcreaterunloopsource%28_,_,_,_%29.md)
  Creates a run loop source for a user notification.
- [func CFUserNotificationDisplayAlert(CFTimeInterval, CFOptionFlags, CFURL!, CFURL!, CFURL!, CFString!, CFString!, CFString!, CFString!, CFString!, UnsafeMutablePointer<CFOptionFlags>!) -> Int32](./cfusernotificationdisplayalert%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Displays a user notification dialog and waits for a user response.
- [func CFUserNotificationDisplayNotice(CFTimeInterval, CFOptionFlags, CFURL!, CFURL!, CFURL!, CFString!, CFString!, CFString!) -> Int32](./cfusernotificationdisplaynotice%28_,_,_,_,_,_,_,_%29.md)
  Displays a user notification dialog that does not need a user response.
- [func CFUserNotificationGetResponseDictionary(CFUserNotification!) -> CFDictionary!](./cfusernotificationgetresponsedictionary%28_%29.md)
  Returns the dictionary containing all the text field values from a dismissed notification dialog.
- [func CFUserNotificationGetResponseValue(CFUserNotification!, CFString!, CFIndex) -> CFString!](./cfusernotificationgetresponsevalue%28_,_,_%29.md)
  Extracts the values of the text fields from a dismissed notification dialog.
- [func CFUserNotificationGetTypeID() -> CFTypeID](./cfusernotificationgettypeid%28%29.md)
  Returns the type identifier for the `CFUserNotification` opaque type.
- [func CFUserNotificationPopUpSelection(CFIndex) -> CFOptionFlags](./cfusernotificationpopupselection%28_%29.md)
  Returns a flag used to set the selected element of a pop-up menu.
- [func CFUserNotificationReceiveResponse(CFUserNotification!, CFTimeInterval, UnsafeMutablePointer<CFOptionFlags>!) -> Int32](./cfusernotificationreceiveresponse%28_,_,_%29.md)
  Waits for the user to respond to a notification or for the notification to time out.
- [func CFUserNotificationSecureTextField(CFIndex) -> CFOptionFlags](./cfusernotificationsecuretextfield%28_%29.md)
  Returns a flag used to set the secure state of a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfusernotificationupdate(_:_:_:_:))*