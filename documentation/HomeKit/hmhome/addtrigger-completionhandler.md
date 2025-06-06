# addTrigger(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Adds a trigger to the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func addTrigger(_ trigger: HMTrigger) async throws
```

## Parameters

- `trigger`: The name of the new trigger. Must not be  , and must not be the name of a trigger already in the home.
- `completion`: The block executed after the request is processed.

## See Also

- [var triggers: [HMTrigger]](hmhome/triggers.md)
  An array of triggers defined in the home.
- [func removeTrigger(HMTrigger, completionHandler: ((any Error)?) -> Void)](hmhome/removetrigger(_:completionhandler:).md)
  Removes a trigger from the home.
- [class HMTimerTrigger](hmtimertrigger.md)
  A trigger to activate an action set based on a periodic timer.
- [class HMEventTrigger](hmeventtrigger.md)
  A trigger to activate an action set based on a set of events and optional conditions.
- [class HMTrigger](hmtrigger.md)
  An abstract base class for triggering actions based on a set of conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addtrigger(_:completionhandler:))*