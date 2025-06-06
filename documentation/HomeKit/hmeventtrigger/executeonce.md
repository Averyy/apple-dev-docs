# executeOnce

**Framework**: HomeKit  
**Kind**: property

A Boolean that can execute the trigger many times.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var executeOnce: Bool { get }
```

#### Discussion

Disables the trigger after its first execution if [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var recurrences: [DateComponents]?](hmeventtrigger/recurrences.md)
  Specifies the days on which the trigger can execute.
- [func updateRecurrences([DateComponents]?, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updaterecurrences(_:completionhandler:).md)
  Updates the days of the week the trigger can repeat.
- [func updateExecuteOnce(Bool, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updateexecuteonce(_:completionhandler:).md)
  Updates the repetition status of the event trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/executeonce)*