# CFUserNotificationCreate(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a CFUserNotification object and displays its notification dialog on screen.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func CFUserNotificationCreate(_ allocator: CFAllocator!, _ timeout: CFTimeInterval, _ flags: CFOptionFlags, _ error: UnsafeMutablePointer<Int32>!, _ dictionary: CFDictionary!) -> CFUserNotification!
```

```c
extern CFUserNotificationRefCFUserNotificationCreate(CFAllocatorRef allocator, CFTimeInterval timeout, CFOptionFlags flags, SInt32 *error, CFDictionaryRef dictionary);
```

## Return Value

The new CFUserNotification object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `timeout`: The time to wait before the notification dialog dismisses itself if the user does not respond. If `0`, the notification never times out.
- `flags`: A set of flags describing the type of notification to display. These flags specify an alert level for the notification (see [Alert Levels](./api-1534483-alert-levels.md)), determine whether radio buttons or checkboxes are to be used (see [Button Flags](./api-1534481-button-flags.md)), specify which, if any, of these buttons are checked by default (see [`CFUserNotificationCheckBoxChecked(_:)`](./cfusernotificationcheckboxchecked%28_%29.md)), specify whether any of the text fields are to be secure text fields (see [`CFUserNotificationSecureTextField(_:)`](./cfusernotificationsecuretextfield%28_%29.md)), and determine which element of a pop-up menu, if present, should be selected by default (see [`CFUserNotificationPopUpSelection(_:)`](./cfusernotificationpopupselection%28_%29.md)). Combine these flags together by performing a bitwise-OR operation with all the individual flags.
- `error`: On return contains an integer error code. If `0`, the user notification was successfully created and displayed.
- `dictionary`: A description of the elements to display in the notification dialog. The possible keys are listed in [Dialog Description Keys](./dialog-description-keys.md). The dictionary must contain a value for the key [`kCFUserNotificationAlertHeaderKey`](./kcfusernotificationalertheaderkey.md), but the other keys are optional.

## See Also

### CFUserNotification Miscellaneous Functions
- [func CFUserNotificationCancel(CFUserNotification!) -> Int32](./cfusernotificationcancel%28_%29.md)
  Cancels a user notification dialog.
- [func CFUserNotificationCheckBoxChecked(CFIndex) -> CFOptionFlags](./cfusernotificationcheckboxchecked%28_%29.md)
  Returns a flag used to set or test a checkbox’s state.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfusernotificationcreate(_:_:_:_:_:))*