# init(qos:flags:block:)

**Framework**: Dispatch  
**Kind**: init

Creates a new dispatch work item from an existing block and assigns it the specified quality-of-service class.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], block: @escaping () -> Void)
```

#### Discussion

Submit the returned dispatch work item to a queue to schedule it for execution in that queue. Dispatch queues may alter the specified quality-of-service level based on the specified `flags` and the quality-of-service level of the queue’s underlying threads. However, the queue never executes the block with a quality-of-service level lower than the one in the `qos` parameter.

You can also execute the dispatch work item directly in the current context by calling its [`perform()`](dispatchworkitem/perform().md) method. When performing a work item directly, the system never executes the block with a quality-of-service level lower than the one in the `qos` parameter.

## Parameters

- `qos`: The quality-of-service class to use when prioritizing the work item’s execution. For a list of possible values, see  .
- `flags`: Configuration flags for the work item. For a list of possible values, see  .
- `block`: The block that performs the work.

## See Also

- [struct DispatchWorkItemFlags](dispatchworkitemflags.md)
  A set of behaviors for a work item, such as its quality-of-service class and whether to create a barrier or spawn a new detached thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitem/init(qos:flags:block:))*