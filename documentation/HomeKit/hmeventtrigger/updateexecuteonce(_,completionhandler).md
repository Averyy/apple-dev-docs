# updateExecuteOnce(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Updates the repetition status of the event trigger.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func updateExecuteOnce(_ executeOnce: Bool, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func updateExecuteOnce(_ executeOnce: Bool) async throws
```

```objc
- (void) updateExecuteOnce:(BOOL) executeOnce completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `executeOnce`: A Boolean value that specifies whether to repeat the trigger.
- `completion`: A block that executes after processing the request.

  The block takes the following parameter:

  - **error**: If the request was successful, the value of `error` is `nil`; otherwise, the value provides more information about the request status.

## See Also

### Controlling recurrence
- [var recurrences: [DateComponents]?](./recurrences.md)
  Specifies the days on which the trigger can execute.
- [func updateRecurrences([DateComponents]?, completionHandler: ((any Error)?) -> Void)](./updaterecurrences%28_,completionhandler%29.md)
  Updates the days of the week the trigger can repeat.
- [var executeOnce: Bool](./executeonce.md)
  A Boolean that can execute the trigger many times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/updateexecuteonce(_:completionhandler:))*