# performExpiringActivity(withReason:using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func performExpiringActivity(withReason reason: String, using block: @escaping @Sendable (Bool) -> Void)
```

```objc
- (void) performExpiringActivityWithReason:(NSString *) reason usingBlock:(void (^)(BOOL expired)) block;
```

## Discussion

Use this method to perform tasks when your process is executing in the background. This method queues `block` for asynchronous execution on a concurrent queue. When your process is in the background, the method tries to take a task assertion to ensure that your block has time to execute. If it is unable to take a task assertion, or if the time allotted for the task assertion expires, the system executes your block with the parameter set to [`true`](../../Swift/true.md). If it is able to take the task assertion, it executes the block and passes [`false`](../../Swift/false.md) for the expired parameter.

If your block is still executing and the system need to suspend the process, the system executes your block a second time with the `expired` parameter set to [`true`](../../Swift/true.md). Your block must be prepared to handle this case. When the expired parameter is [`true`](../../Swift/true.md), stop any in-progress tasks as quickly as possible.

## Parameters

- `reason`: A string used in debugging to indicate the reason the activity began. This parameter must not be `nil` or an empty string.
- `block`: A block containing the work to be performed by the activity. The block has no return value and takes the following parameter:

  - **expired**: A Boolean indicating whether the process is about to be suspended. If the value is [`true`](../../Swift/true.md), the process is about to be suspended so you should take whatever steps are needed to stop in progress work. If it is [`false`](../../Swift/false.md), start the planned tasks.

## See Also

### Managing activities
- [func beginActivity(options: ProcessInfo.ActivityOptions, reason: String) -> any NSObjectProtocol](./beginactivity%28options,reason%29.md)
  Begin an activity using the given options and reason.
- [func endActivity(any NSObjectProtocol)](./endactivity%28_%29.md)
  Ends the given activity.
- [func performActivity(options: ProcessInfo.ActivityOptions, reason: String, using: () -> Void)](./performactivity%28options,reason,using%29.md)
  Synchronously perform an activity defined by a given block using the given options.
- [ProcessInfo.ActivityOptions](./activityoptions.md)
  Option flags used with [`beginActivity(options:reason:)`](./beginactivity%28options,reason%29.md) and [`performActivity(options:reason:using:)`](./performactivity%28options,reason,using%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/performexpiringactivity(withreason:using:))*