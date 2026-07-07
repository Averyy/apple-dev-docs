# notify(queue:execute:)

**Framework**: Dispatch  
**Kind**: method

Schedules the execution of the specified work item after the completion of the current work item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func notify(queue: DispatchQueue, execute: DispatchWorkItem)
```

## Parameters

- `queue`: The queue on which to execute the work item in the `execute` parameter.
- `execute`: The work item to execute after the completion of the current work item.

## See Also

- [func notify(qos: DispatchQoS, flags: DispatchWorkItemFlags, queue: DispatchQueue, execute: () -> Void)](dispatchworkitem/notify(qos:flags:queue:execute:).md)
  Schedules the execution of the specified work item, with the specified quality-of-service, after the completion of the current work item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitem/notify(queue:execute:))*