# SCPreferencesUnscheduleFromRunLoop(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Unschedules commit and apply notifications for the specified preferences session from the specified run loop and mode.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCPreferencesUnscheduleFromRunLoop(_ prefs: SCPreferences, _ runLoop: CFRunLoop, _ runLoopMode: CFString) -> Bool
```

#### Return Value

`TRUE` if the notifications are successfully unscheduled; otherwise, `FALSE`.

## Parameters

- `prefs`: The preferences session.
- `runLoop`: The run loop from which the notification should be unscheduled. Do not pass  .
- `runLoopMode`: The run loop mode associated with the scheduled notification. Do not pass  .

## See Also

- [func SCPreferencesSetCallback(SCPreferences, SCPreferencesCallBack?, UnsafeMutablePointer<SCPreferencesContext>?) -> Bool](scpreferencessetcallback(_:_:_:).md)
  Assigns the specified callback to the specified preferences session.
- [func SCPreferencesScheduleWithRunLoop(SCPreferences, CFRunLoop, CFString) -> Bool](scpreferencesschedulewithrunloop(_:_:_:).md)
  Schedules commit and apply notifications for the specified preferences session using the specified run loop and mode.
- [func SCPreferencesSetDispatchQueue(SCPreferences, dispatch_queue_t?) -> Bool](scpreferencessetdispatchqueue(_:_:).md)
  Schedules commit and apply notifications for the specified preferences session using the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesunschedulefromrunloop(_:_:_:))*