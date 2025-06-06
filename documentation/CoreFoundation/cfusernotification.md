# CFUserNotification

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CFUserNotification
```

#### Overview

A `CFUserNotification` object presents a simple dialog on the screen and optionally receives feedback from the user. The contents of the dialog can include a header, a message, an icon, text fields, a pop-up button, radio buttons or checkboxes, and up to three ordinary buttons. Use `CFUserNotification` in processes that do not otherwise have user interfaces, but may need occasional interaction with the user.

You create a user notification with the [`CFUserNotificationCreate(_:_:_:_:_:)`](cfusernotificationcreate(_:_:_:_:_:).md) function. You pass in a dictionary whose keys describe the items to place into the dialog. (See [`Dialog Description Keys`](dialog-description-keys.md) for the list of keys.) A set of flags passed to the function determines, among other things, whether secure text fields are used (such as for password fields), whether radio buttons or checkboxes are used, and which of these buttons are checked by default. You can also specify a timeout for the dialog, in which case the dialog cancels itself if the user does not respond in the allotted time period.

A user notification displays its dialog as soon as it is created. If any reply is required, it may be awaited in one of two ways: either synchronously, using [`CFUserNotificationReceiveResponse(_:_:_:)`](cfusernotificationreceiveresponse(_:_:_:).md), or asynchronously, using a run loop source created with [`CFUserNotificationCreateRunLoopSource(_:_:_:_:)`](cfusernotificationcreaterunloopsource(_:_:_:_:).md). [`CFUserNotificationReceiveResponse(_:_:_:)`](cfusernotificationreceiveresponse(_:_:_:).md) has a timeout parameter that determines how long it will block (zero meaning indefinitely) and it may be called as many times as necessary until a response arrives. If a user notification has not yet received a response, it may be updated with new information or it may be cancelled. User notifications may not be reused.

`CFUserNotification` provides two convenience functions, [`CFUserNotificationDisplayNotice(_:_:_:_:_:_:_:_:)`](cfusernotificationdisplaynotice(_:_:_:_:_:_:_:_:).md) and [`CFUserNotificationDisplayAlert(_:_:_:_:_:_:_:_:_:_:_:)`](cfusernotificationdisplayalert(_:_:_:_:_:_:_:_:_:_:_:).md), to display very basic dialogs that either require no response from the user or require only a single button to be pressed, respectively.

## Topics

### CFUserNotification Miscellaneous Functions
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
- [func CFUserNotificationReceiveResponse(CFUserNotification!, CFTimeInterval, UnsafeMutablePointer<CFOptionFlags>!) -> Int32](cfusernotificationreceiveresponse(_:_:_:).md)
  Waits for the user to respond to a notification or for the notification to time out.
- [func CFUserNotificationSecureTextField(CFIndex) -> CFOptionFlags](cfusernotificationsecuretextfield(_:).md)
  Returns a flag used to set the secure state of a text field.
- [func CFUserNotificationUpdate(CFUserNotification!, CFTimeInterval, CFOptionFlags, CFDictionary!) -> Int32](cfusernotificationupdate(_:_:_:_:).md)
  Updates a displayed user notification dialog with new user interface information.
### Callbacks
- [typealias CFUserNotificationCallBack](cfusernotificationcallback.md)
  Callback invoked when an asynchronous user notification dialog is dismissed.
### Constants
- [Alert Levels](1534483-alert-levels.md)
  Flags identifying the seriousness of a user notification.
- [Response Codes](1534504-response-codes.md)
  Response codes identifying the button that was pressed to dismiss a notification dialog.
- [Button Flags](1534481-button-flags.md)
  Flags that alter the display of buttons in a user notification dialog.
- [Alert Levels](1534483-alert-levels.md)
  Flags identifying the seriousness of a user notification.
- [Response Codes](1534504-response-codes.md)
  Response codes identifying the button that was pressed to dismiss a notification dialog.
- [Button Flags](1534481-button-flags.md)
  Flags that alter the display of buttons in a user notification dialog.
- [Dialog Description Keys](dialog-description-keys.md)
  Keys used in a user notification’s description dictionary, which describes the contents of the notification dialog to display.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfusernotification)*