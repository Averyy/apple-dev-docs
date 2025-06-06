# SCPreferencesSetDispatchQueue(_:_:)

**Framework**: System Configuration  
**Kind**: func

Schedules commit and apply notifications for the specified preferences session using the specified dispatch queue.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func SCPreferencesSetDispatchQueue(_ prefs: SCPreferences, _ queue: dispatch_queue_t?) -> Bool
```

#### Return Value

`TRUE` if the notifications are successfully scheduled; otherwise, `FALSE`.

## Parameters

- `prefs`: The preferences session.
- `queue`: The dispatch queue on which to run the callback function.

## See Also

- [func SCPreferencesSetCallback(SCPreferences, SCPreferencesCallBack?, UnsafeMutablePointer<SCPreferencesContext>?) -> Bool](scpreferencessetcallback(_:_:_:).md)
  Assigns the specified callback to the specified preferences session.
- [func SCPreferencesScheduleWithRunLoop(SCPreferences, CFRunLoop, CFString) -> Bool](scpreferencesschedulewithrunloop(_:_:_:).md)
  Schedules commit and apply notifications for the specified preferences session using the specified run loop and mode.
- [func SCPreferencesUnscheduleFromRunLoop(SCPreferences, CFRunLoop, CFString) -> Bool](scpreferencesunschedulefromrunloop(_:_:_:).md)
  Unschedules commit and apply notifications for the specified preferences session from the specified run loop and mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencessetdispatchqueue(_:_:))*