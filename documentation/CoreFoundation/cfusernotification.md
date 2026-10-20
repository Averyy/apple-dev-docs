# CFUserNotification

**Framework**: Core Foundation  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class CFUserNotification
```

```c
typedef struct __CFUserNotification * CFUserNotificationRef;
```

#### Overview

A `CFUserNotification` object presents a simple dialog on the screen and optionally receives feedback from the user. The contents of the dialog can include a header, a message, an icon, text fields, a pop-up button, radio buttons or checkboxes, and up to three ordinary buttons. Use `CFUserNotification` in processes that do not otherwise have user interfaces, but may need occasional interaction with the user.

You create a user notification with the [`CFUserNotificationCreate(_:_:_:_:_:)`](./cfusernotificationcreate%28_,_,_,_,_%29.md) function. You pass in a dictionary whose keys describe the items to place into the dialog. (See [Dialog Description Keys](./dialog-description-keys.md) for the list of keys.) A set of flags passed to the function determines, among other things, whether secure text fields are used (such as for password fields), whether radio buttons or checkboxes are used, and which of these buttons are checked by default. You can also specify a timeout for the dialog, in which case the dialog cancels itself if the user does not respond in the allotted time period.

A user notification displays its dialog as soon as it is created. If any reply is required, it may be awaited in one of two ways: either synchronously, using [`CFUserNotificationReceiveResponse(_:_:_:)`](./cfusernotificationreceiveresponse%28_,_,_%29.md), or asynchronously, using a run loop source created with [`CFUserNotificationCreateRunLoopSource(_:_:_:_:)`](./cfusernotificationcreaterunloopsource%28_,_,_,_%29.md). [`CFUserNotificationReceiveResponse(_:_:_:)`](./cfusernotificationreceiveresponse%28_,_,_%29.md) has a timeout parameter that determines how long it will block (zero meaning indefinitely) and it may be called as many times as necessary until a response arrives. If a user notification has not yet received a response, it may be updated with new information or it may be cancelled. User notifications may not be reused.

`CFUserNotification` provides two convenience functions, [`CFUserNotificationDisplayNotice(_:_:_:_:_:_:_:_:)`](./cfusernotificationdisplaynotice%28_,_,_,_,_,_,_,_%29.md) and [`CFUserNotificationDisplayAlert(_:_:_:_:_:_:_:_:_:_:_:)`](./cfusernotificationdisplayalert%28_,_,_,_,_,_,_,_,_,_,_%29.md), to display very basic dialogs that either require no response from the user or require only a single button to be pressed, respectively.

## Topics

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
- [func CFUserNotificationUpdate(CFUserNotification!, CFTimeInterval, CFOptionFlags, CFDictionary!) -> Int32](./cfusernotificationupdate%28_,_,_,_%29.md)
  Updates a displayed user notification dialog with new user interface information.
### Callbacks
- [typealias CFUserNotificationCallBack](./cfusernotificationcallback.md)
  Callback invoked when an asynchronous user notification dialog is dismissed.
### Constants
- [Alert Levels](./api-1534483-alert-levels.md)
  Flags identifying the seriousness of a user notification.
- [Response Codes](./api-1534504-response-codes.md)
  Response codes identifying the button that was pressed to dismiss a notification dialog.
- [Button Flags](./api-1534481-button-flags.md)
  Flags that alter the display of buttons in a user notification dialog.
- [Alert Levels](./api-1534483-alert-levels.md)
  Flags identifying the seriousness of a user notification.
- [Response Codes](./api-1534504-response-codes.md)
  Response codes identifying the button that was pressed to dismiss a notification dialog.
- [Button Flags](./api-1534481-button-flags.md)
  Flags that alter the display of buttons in a user notification dialog.
- [Dialog Description Keys](./dialog-description-keys.md)
  Keys used in a user notification’s description dictionary, which describes the contents of the notification dialog to display.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Opaque Types
- [class CFAllocator](./cfallocator.md)
- [class CFArray](./cfarray.md)
- [class CFAttributedString](./cfattributedstring.md)
- [class CFBag](./cfbag.md)
- [class CFBinaryHeap](./cfbinaryheap.md)
- [class CFBitVector](./cfbitvector.md)
- [class CFBoolean](./cfboolean.md)
- [class CFBundle](./cfbundle.md)
- [class CFCalendar](./cfcalendar.md)
- [class CFCharacterSet](./cfcharacterset.md)
- [class CFData](./cfdata.md)
- [class CFDate](./cfdate.md)
- [class CFDateFormatter](./cfdateformatter.md)
- [class CFDictionary](./cfdictionary.md)
- [class CFError](./cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfusernotification)*