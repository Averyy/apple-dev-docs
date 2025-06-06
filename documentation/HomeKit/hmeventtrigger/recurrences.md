# recurrences

**Framework**: HomeKit  
**Kind**: property

Specifies the days on which the trigger can execute.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var recurrences: [DateComponents]? { get }
```

#### Discussion

This property represents the days of the week that the trigger recurs; the trigger ignores all properties other than [`weekday`](https://developer.apple.com/documentation/foundation/datecomponents/1780094-weekday) on the [`DateComponents`](https://developer.apple.com/documentation/Foundation/DateComponents) object.

## See Also

- [func updateRecurrences([DateComponents]?, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updaterecurrences(_:completionhandler:).md)
  Updates the days of the week the trigger can repeat.
- [var executeOnce: Bool](hmeventtrigger/executeonce.md)
  A Boolean that can execute the trigger many times.
- [func updateExecuteOnce(Bool, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updateexecuteonce(_:completionhandler:).md)
  Updates the repetition status of the event trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/recurrences)*