# SCPreferencesSetCallback(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Assigns the specified callback to the specified preferences session.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCPreferencesSetCallback(_ prefs: SCPreferences, _ callout: SCPreferencesCallBack?, _ context: UnsafeMutablePointer<SCPreferencesContext>?) -> Bool
```

#### Return Value

`TRUE` if the callback was successfully associated with the preferences session; otherwise, `FALSE`.

#### Discussion

This function is called when the changes to the preferences have been committed or applied.

## Parameters

- `prefs`: The preferences session.
- `callout`: The function to be called when the preferences have been changed or applied. If  , the current callback is removed.
- `context`: The context associated with the callback function. See   for more information about this structure.

## See Also

- [func SCPreferencesScheduleWithRunLoop(SCPreferences, CFRunLoop, CFString) -> Bool](scpreferencesschedulewithrunloop(_:_:_:).md)
  Schedules commit and apply notifications for the specified preferences session using the specified run loop and mode.
- [func SCPreferencesUnscheduleFromRunLoop(SCPreferences, CFRunLoop, CFString) -> Bool](scpreferencesunschedulefromrunloop(_:_:_:).md)
  Unschedules commit and apply notifications for the specified preferences session from the specified run loop and mode.
- [func SCPreferencesSetDispatchQueue(SCPreferences, dispatch_queue_t?) -> Bool](scpreferencessetdispatchqueue(_:_:).md)
  Schedules commit and apply notifications for the specified preferences session using the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencessetcallback(_:_:_:))*