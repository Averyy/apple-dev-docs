# perform(_:target:argument:order:modes:)

**Framework**: Foundation  
**Kind**: method

Schedules the sending of a message on the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func perform(_ aSelector: Selector, target: Any, argument arg: Any?, order: Int, modes: [RunLoop.Mode])
```

#### Discussion

This method sets up a timer to perform the `aSelector` message on the receiver at the start of the next run loop iteration. The timer is configured to run in the modes specified by the `modes` parameter. When the timer fires, the thread attempts to dequeue the message from the run loop and perform the selector. It succeeds if the run loop is running and in one of the specified modes; otherwise, the timer waits until the run loop is in one of those modes.

This method returns before the `aSelector` message is sent. The receiver retains the `target` and `anArgument` objects until the timer for the selector fires, and then releases them as part of its cleanup.

Use this method if you want multiple messages to be sent after the current event has been processed and you want to make sure these messages are sent in a certain order.

## Parameters

- `aSelector`: A selector that identifies the method to invoke. This method should not have a significant return value and should take a single argument of type id.
- `target`: The object that defines the selector in  .
- `arg`: The argument to pass to the method when it is invoked. Pass   if the method does not take an argument.
- `order`: The priority for the message. If multiple messages are scheduled, the messages with a lower order value are sent before messages with a higher order value.
- `modes`: An array of input modes for which the message may be sent. You may specify custom modes or use one of the modes listed in  .

## See Also

- [func perform(() -> Void)](runloop/perform(_:).md)
  Schedules a block that the run loop invokes.
- [func perform(inModes: [RunLoop.Mode], block: () -> Void)](runloop/perform(inmodes:block:).md)
  Schedules a block that the run loop invokes when it’s running in any of the specified modes.
- [func cancelPerform(Selector, target: Any, argument: Any?)](runloop/cancelperform(_:target:argument:).md)
  Cancels the sending of a previously scheduled message.
- [func cancelPerformSelectors(withTarget: Any)](runloop/cancelperformselectors(withtarget:).md)
  Cancels all outstanding ordered performs scheduled with a given target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/perform(_:target:argument:order:modes:))*