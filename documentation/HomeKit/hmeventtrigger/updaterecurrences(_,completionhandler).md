# updateRecurrences(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Updates the days of the week the trigger can repeat.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func updateRecurrences(_ recurrences: [DateComponents]?, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func updateRecurrences(_ recurrences: [DateComponents]?) async throws
```

```objc
- (void) updateRecurrences:(NSArray<NSDateComponents *> *) recurrences completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `recurrences`: An array of [`DateComponents`](../../Foundation/datecomponents.md) that represent the days of the week that the event trigger can repeat. Only respects the [`weekday`](../../Foundation/datecomponents/weekday.md) property of [`DateComponents`](../../Foundation/datecomponents.md).
- `completion`: A block that executes after processing the request.

  The block takes the following parameter:

  - **error**: If the request was successful, the value of `error` is `nil`; otherwise, the value provides more information about the request status.

## See Also

### Controlling recurrence
- [var recurrences: [DateComponents]?](./recurrences.md)
  Specifies the days on which the trigger can execute.
- [var executeOnce: Bool](./executeonce.md)
  A Boolean that can execute the trigger many times.
- [func updateExecuteOnce(Bool, completionHandler: ((any Error)?) -> Void)](./updateexecuteonce%28_,completionhandler%29.md)
  Updates the repetition status of the event trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/updaterecurrences(_:completionhandler:))*