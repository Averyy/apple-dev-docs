# SCPreferencesScheduleWithRunLoop(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Schedules commit and apply notifications for the specified preferences session using the specified run loop and mode.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCPreferencesScheduleWithRunLoop(_ prefs: SCPreferences, _ runLoop: CFRunLoop, _ runLoopMode: CFString) -> Bool
```

#### Return Value

`TRUE` if the notifications are successfully scheduled; otherwise, `FALSE`.

## Parameters

- `prefs`: The preferences session.
- `runLoop`: The run loop on which the notification should be scheduled. Do not pass  .
- `runLoopMode`: The run loop mode with which to schedule the notification. Do not pass  .

## See Also

- [func SCPreferencesSetCallback(SCPreferences, SCPreferencesCallBack?, UnsafeMutablePointer<SCPreferencesContext>?) -> Bool](scpreferencessetcallback(_:_:_:).md)
  Assigns the specified callback to the specified preferences session.
- [func SCPreferencesUnscheduleFromRunLoop(SCPreferences, CFRunLoop, CFString) -> Bool](scpreferencesunschedulefromrunloop(_:_:_:).md)
  Unschedules commit and apply notifications for the specified preferences session from the specified run loop and mode.
- [func SCPreferencesSetDispatchQueue(SCPreferences, dispatch_queue_t?) -> Bool](scpreferencessetdispatchqueue(_:_:).md)
  Schedules commit and apply notifications for the specified preferences session using the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesschedulewithrunloop(_:_:_:))*