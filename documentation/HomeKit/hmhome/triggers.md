# triggers

**Framework**: HomeKit  
**Kind**: property

An array of triggers defined in the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var triggers: [HMTrigger] { get }
```

## See Also

- [func addTrigger(HMTrigger, completionHandler: ((any Error)?) -> Void)](hmhome/addtrigger(_:completionhandler:).md)
  Adds a trigger to the home.
- [func removeTrigger(HMTrigger, completionHandler: ((any Error)?) -> Void)](hmhome/removetrigger(_:completionhandler:).md)
  Removes a trigger from the home.
- [class HMTimerTrigger](hmtimertrigger.md)
  A trigger to activate an action set based on a periodic timer.
- [class HMEventTrigger](hmeventtrigger.md)
  A trigger to activate an action set based on a set of events and optional conditions.
- [class HMTrigger](hmtrigger.md)
  An abstract base class for triggering actions based on a set of conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/triggers)*