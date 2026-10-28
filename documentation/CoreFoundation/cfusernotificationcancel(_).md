# CFUserNotificationCancel(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Cancels a user notification dialog.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func CFUserNotificationCancel(_ userNotification: CFUserNotification!) -> Int32
```

```c
extern SInt32 CFUserNotificationCancel(CFUserNotificationRef userNotification);
```

## Return Value

`0` if the cancel was successful; a non-`0` value otherwise.

## Discussion

You must cancel a user notification if you want to remove its dialog from the screen before the user dismisses it. It is not sufficient to just release the object.

## Parameters

- `userNotification`: The user notification to cancel.

## See Also

### CFUserNotification Miscellaneous Functions
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
- [func CFUserNotificationUpdate(CFUserNotification!, CFTimeInterval, CFOptionFlags, CFDictionary!) -> Int32](./cfusernotificationupdate%28_,_,_,_%29.md)
  Updates a displayed user notification dialog with new user interface information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfusernotificationcancel(_:))*