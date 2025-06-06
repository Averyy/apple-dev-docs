# CFUserNotificationDisplayAlert(_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Displays a user notification dialog and waits for a user response.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func CFUserNotificationDisplayAlert(_ timeout: CFTimeInterval, _ flags: CFOptionFlags, _ iconURL: CFURL!, _ soundURL: CFURL!, _ localizationURL: CFURL!, _ alertHeader: CFString!, _ alertMessage: CFString!, _ defaultButtonTitle: CFString!, _ alternateButtonTitle: CFString!, _ otherButtonTitle: CFString!, _ responseFlags: UnsafeMutablePointer<CFOptionFlags>!) -> Int32
```

#### Return Value

`0` if the cancel was successful; a non-`0` value otherwise.

#### Discussion

This function blocks the current thread’s execution until the dialog is dismissed, either by the user or by timing out.

## Parameters

- `timeout`: The amount of time to wait for the user to dismiss the notification dialog before the dialog dismisses itself. Pass   to have the dialog never time out.
- `flags`: A set of flags describing the type of notification dialog to display. The value is normally just the alert level from  . If you don’t want a default button displayed, perform a bitwise-OR operation with the alert level and the constant  .
- `iconURL`: A file URL pointing to the icon to display in the dialog. If  , a default icon is used based on the notification’s alert level specified in  .
- `soundURL`: Not used.
- `localizationURL`: A file URL pointing to a bundle that contains localized versions of the strings displayed in the dialog. Can be  .
- `alertHeader`: The title of the notification dialog. Cannot be  .
- `alertMessage`: The message string to display in the dialog. Can be  .
- `defaultButtonTitle`: The title of the default button. If  , the string   is used.
- `alternateButtonTitle`: The title of an optional alternate button. Can be  .
- `otherButtonTitle`: The title of an optional third button. Can be  .
- `responseFlags`: On return, contains flags identifying how the notification was dismissed. See   for details.

## See Also

- [func CFUserNotificationCancel(CFUserNotification!) -> Int32](cfusernotificationcancel(_:).md)
  Cancels a user notification dialog.
- [func CFUserNotificationCheckBoxChecked(CFIndex) -> CFOptionFlags](cfusernotificationcheckboxchecked(_:).md)
  Returns a flag used to set or test a checkbox’s state.
- [func CFUserNotificationCreate(CFAllocator!, CFTimeInterval, CFOptionFlags, UnsafeMutablePointer<Int32>!, CFDictionary!) -> CFUserNotification!](cfusernotificationcreate(_:_:_:_:_:).md)
  Creates a CFUserNotification object and displays its notification dialog on screen.
- [func CFUserNotificationCreateRunLoopSource(CFAllocator!, CFUserNotification!, CFUserNotificationCallBack!, CFIndex) -> CFRunLoopSource!](cfusernotificationcreaterunloopsource(_:_:_:_:).md)
  Creates a run loop source for a user notification.
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
- [func CFUserNotificationReceiveResponse(CFUserNotification!, CFTimeInterval, UnsafeMutablePointer<CFOptionFlags>!) -> Int32](cfusernotificationreceiveresponse(_:_:_:).md)
  Waits for the user to respond to a notification or for the notification to time out.
- [func CFUserNotificationSecureTextField(CFIndex) -> CFOptionFlags](cfusernotificationsecuretextfield(_:).md)
  Returns a flag used to set the secure state of a text field.
- [func CFUserNotificationUpdate(CFUserNotification!, CFTimeInterval, CFOptionFlags, CFDictionary!) -> Int32](cfusernotificationupdate(_:_:_:_:).md)
  Updates a displayed user notification dialog with new user interface information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfusernotificationdisplayalert(_:_:_:_:_:_:_:_:_:_:_:))*