# updateExecuteOnce(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the repetition status of the event trigger.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func updateExecuteOnce(_ executeOnce: Bool) async throws
```

## Parameters

- `executeOnce`: A Boolean value that specifies whether to repeat the trigger.
- `completion`: The block takes the following parameter:

## See Also

- [var recurrences: [DateComponents]?](hmeventtrigger/recurrences.md)
  Specifies the days on which the trigger can execute.
- [func updateRecurrences([DateComponents]?, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updaterecurrences(_:completionhandler:).md)
  Updates the days of the week the trigger can repeat.
- [var executeOnce: Bool](hmeventtrigger/executeonce.md)
  A Boolean that can execute the trigger many times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/updateexecuteonce(_:completionhandler:))*