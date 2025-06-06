# fireDate

**Framework**: HomeKit  
**Kind**: property

The time at which the trigger will next fire.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var fireDate: Date { get }
```

#### Discussion

Timer triggers are only set at the beginning of a minute. Seconds are not used and an error will be returned if the fire date includes a seconds value other than 0. When the timer fires, it will typically fire within 1 minute of the scheduled fire date or calculated recurrence fire date, depending on system power and resource management.

## See Also

- [func updateFireDate(Date, completionHandler: ((any Error)?) -> Void)](hmtimertrigger/updatefiredate(_:completionhandler:).md)
  Updates the next fire date for the trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/firedate)*