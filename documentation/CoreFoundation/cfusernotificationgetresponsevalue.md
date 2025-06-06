# CFUserNotificationGetResponseValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Extracts the values of the text fields from a dismissed notification dialog.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func CFUserNotificationGetResponseValue(_ userNotification: CFUserNotification!, _ key: CFString!, _ idx: CFIndex) -> CFString!
```

#### Return Value

The value of the text field identified by `key` and `idx`. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `userNotification`: The user notification to use.
- `key`: The dictionary key identifying the text fields to use. Currently, only   is supported.
- `idx`: The index of the text field value to return. The index corresponds to the order in which text fields are listed in the   array in the user notification’s description dictionary.

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
- [func CFUserNotificationGetTypeID() -> CFTypeID](cfusernotificationgettypeid().md)
  Returns the type identifier for the `CFUserNotification` opaque type.
- [func CFUserNotificationPopUpSelection(CFIndex) -> CFOptionFlags](cfusernotificationpopupselection(_:).md)
  Returns a flag used to set the selected element of a pop-up menu.
- [func CFUserNotificationReceiveResponse(CFUserNotification!, CFTimeInterval, UnsafeMutablePointer<CFOptionFlags>!) -> Int32](cfusernotificationreceiveresponse(_:_:_:).md)
  Waits for the user to respond to a notification or for the notification to time out.
- [func CFUserNotificationSecureTextField(CFIndex) -> CFOptionFlags](cfusernotificationsecuretextfield(_:).md)
  Returns a flag used to set the secure state of a text field.
- [func CFUserNotificationUpdate(CFUserNotification!, CFTimeInterval, CFOptionFlags, CFDictionary!) -> Int32](cfusernotificationupdate(_:_:_:_:).md)
  Updates a displayed user notification dialog with new user interface information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfusernotificationgetresponsevalue(_:_:_:))*