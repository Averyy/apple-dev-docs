# SCPreferencesSetDispatchQueue(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Schedules commit and apply notifications for the specified preferences session using the specified dispatch queue.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func SCPreferencesSetDispatchQueue(_ prefs: SCPreferences, _ queue: dispatch_queue_t?) -> Bool
```

```c
Boolean SCPreferencesSetDispatchQueue(SCPreferencesRef prefs, dispatch_queue_t queue);
```

## Return Value

`TRUE` if the notifications are successfully scheduled; otherwise, `FALSE`.

## Parameters

- `prefs`: The preferences session.
- `queue`: The dispatch queue on which to run the callback function.

## See Also

### Managing Notifications and Callbacks
- [func SCPreferencesSetCallback(SCPreferences, SCPreferencesCallBack?, UnsafeMutablePointer<SCPreferencesContext>?) -> Bool](./scpreferencessetcallback%28_,_,_%29.md)
  Assigns the specified callback to the specified preferences session.
- [func SCPreferencesScheduleWithRunLoop(SCPreferences, CFRunLoop, CFString) -> Bool](./scpreferencesschedulewithrunloop%28_,_,_%29.md)
  Schedules commit and apply notifications for the specified preferences session using the specified run loop and mode.
- [func SCPreferencesUnscheduleFromRunLoop(SCPreferences, CFRunLoop, CFString) -> Bool](./scpreferencesunschedulefromrunloop%28_,_,_%29.md)
  Unschedules commit and apply notifications for the specified preferences session from the specified run loop and mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencessetdispatchqueue(_:_:))*