# CFUserNotificationDisplayAlert(_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Displays a user notification dialog and waits for a user response.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func CFUserNotificationDisplayAlert(_ timeout: CFTimeInterval, _ flags: CFOptionFlags, _ iconURL: CFURL!, _ soundURL: CFURL!, _ localizationURL: CFURL!, _ alertHeader: CFString!, _ alertMessage: CFString!, _ defaultButtonTitle: CFString!, _ alternateButtonTitle: CFString!, _ otherButtonTitle: CFString!, _ responseFlags: UnsafeMutablePointer<CFOptionFlags>!) -> Int32
```

```c
extern SInt32 CFUserNotificationDisplayAlert(CFTimeInterval timeout, CFOptionFlags flags, CFURLRef iconURL, CFURLRef soundURL, CFURLRef localizationURL, CFStringRef alertHeader, CFStringRef alertMessage, CFStringRef defaultButtonTitle, CFStringRef alternateButtonTitle, CFStringRef otherButtonTitle, CFOptionFlags *responseFlags);
```

## Return Value

`0` if the cancel was successful; a non-`0` value otherwise.

## Discussion

This function blocks the current thread’s execution until the dialog is dismissed, either by the user or by timing out.

## Parameters

- `timeout`: The amount of time to wait for the user to dismiss the notification dialog before the dialog dismisses itself. Pass `0` to have the dialog never time out.
- `flags`: A set of flags describing the type of notification dialog to display. The value is normally just the alert level from [Alert Levels](./api-1534483-alert-levels.md). If you don’t want a default button displayed, perform a bitwise-OR operation with the alert level and the constant [`kCFUserNotificationNoDefaultButtonFlag`](./kcfusernotificationnodefaultbuttonflag.md).
- `iconURL`: A file URL pointing to the icon to display in the dialog. If `NULL`, a default icon is used based on the notification’s alert level specified in `flags`.
- `soundURL`: Not used.
- `localizationURL`: A file URL pointing to a bundle that contains localized versions of the strings displayed in the dialog. Can be `NULL`.
- `alertHeader`: The title of the notification dialog. Cannot be `NULL`.
- `alertMessage`: The message string to display in the dialog. Can be `NULL`.
- `defaultButtonTitle`: The title of the default button. If `NULL`, the string `OK` is used.
- `alternateButtonTitle`: The title of an optional alternate button. Can be `NULL`.
- `otherButtonTitle`: The title of an optional third button. Can be `NULL`.
- `responseFlags`: On return, contains flags identifying how the notification was dismissed. See [Response Codes](./api-1534504-response-codes.md) for details.

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfusernotificationdisplayalert(_:_:_:_:_:_:_:_:_:_:_:))*