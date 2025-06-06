# performExpiringActivity(withReason:using:)

**Framework**: Foundation  
**Kind**: method

Performs the specified block asynchronously and notifies you if the process is about to be suspended.

**Availability**:
- iOS 8.2+
- iPadOS 8.2+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func performExpiringActivity(withReason reason: String, using block: @escaping (Bool) -> Void)
```

#### Discussion

Use this method to perform tasks when your process is executing in the background. This method queues `block` for asynchronous execution on a concurrent queue. When your process is in the background, the method tries to take a task assertion to ensure that your block has time to execute. If it is unable to take a task assertion, or if the time allotted for the task assertion expires, the system executes your block with the parameter set to [`true`](https://developer.apple.com/documentation/swift/true). If it is able to take the task assertion, it executes the block and passes [`false`](https://developer.apple.com/documentation/swift/false) for the expired parameter.

If your block is still executing and the system need to suspend the process, the system executes your block a second time with the `expired` parameter set to [`true`](https://developer.apple.com/documentation/swift/true). Your block must be prepared to handle this case. When the expired parameter is [`true`](https://developer.apple.com/documentation/swift/true), stop any in-progress tasks as quickly as possible.

## Parameters

- `reason`: A string used in debugging to indicate the reason the activity began. This parameter must not be   or an empty string.
- `block`: A block containing the work to be performed by the activity. The block has no return value and takes the following parameter:

## See Also

- [func beginActivity(options: ProcessInfo.ActivityOptions, reason: String) -> any NSObjectProtocol](processinfo/beginactivity(options:reason:).md)
  Begin an activity using the given options and reason.
- [func endActivity(any NSObjectProtocol)](processinfo/endactivity(_:).md)
  Ends the given activity.
- [func performActivity(options: ProcessInfo.ActivityOptions, reason: String, using: () -> Void)](processinfo/performactivity(options:reason:using:).md)
  Synchronously perform an activity defined by a given block using the given options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/performexpiringactivity(withreason:using:))*