# SCPreferencesUnscheduleFromRunLoop(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Unschedules commit and apply notifications for the specified preferences session from the specified run loop and mode.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCPreferencesUnscheduleFromRunLoop(_ prefs: SCPreferences, _ runLoop: CFRunLoop, _ runLoopMode: CFString) -> Bool
```

```c
Boolean SCPreferencesUnscheduleFromRunLoop(SCPreferencesRef prefs, CFRunLoopRef runLoop, CFStringRef runLoopMode);
```

## Return Value

`TRUE` if the notifications are successfully unscheduled; otherwise, `FALSE`.

## Parameters

- `prefs`: The preferences session.
- `runLoop`: The run loop from which the notification should be unscheduled. Do not pass `NULL`.
- `runLoopMode`: The run loop mode associated with the scheduled notification. Do not pass `NULL`.

## See Also

### Managing Notifications and Callbacks
- [func SCPreferencesSetCallback(SCPreferences, SCPreferencesCallBack?, UnsafeMutablePointer<SCPreferencesContext>?) -> Bool](./scpreferencessetcallback%28_,_,_%29.md)
  Assigns the specified callback to the specified preferences session.
- [func SCPreferencesScheduleWithRunLoop(SCPreferences, CFRunLoop, CFString) -> Bool](./scpreferencesschedulewithrunloop%28_,_,_%29.md)
  Schedules commit and apply notifications for the specified preferences session using the specified run loop and mode.
- [func SCPreferencesSetDispatchQueue(SCPreferences, dispatch_queue_t?) -> Bool](./scpreferencessetdispatchqueue%28_,_%29.md)
  Schedules commit and apply notifications for the specified preferences session using the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesunschedulefromrunloop(_:_:_:))*