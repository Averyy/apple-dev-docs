# cancel()

**Framework**: Foundation  
**Kind**: method

Advises the operation object that it should stop executing its task.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func cancel()
```

#### Discussion

This method does not force your operation code to stop. Instead, it updates the object’s internal flags to reflect the change in state. If the operation has already finished executing, this method has no effect. Canceling an operation that is currently in an operation queue, but not yet executing, makes it possible to remove the operation from the queue sooner than usual.

In macOS 10.6 and later, if an operation is in a queue but waiting on unfinished dependent operations, those operations are subsequently ignored. Because it is already cancelled, this behavior allows the operation queue to call the operation’s [`start()`](operation/start().md) method sooner and clear the object out of the queue. If you cancel an operation that is not in a queue, this method immediately marks the object as finished. In each case, marking the object as ready or finished results in the generation of the appropriate KVO notifications.

In versions of macOS prior to 10.6, an operation object remains in the queue until all of its dependencies are removed through the normal processes. Thus, the operation must wait until all of its dependent operations finish executing or are themselves cancelled and have their [`start()`](operation/start().md) method called.

For more information on what you must do in your operation objects to support cancellation, see [`Responding to the Cancel Command`](operation#Responding-to-the-Cancel-Command.md).

## See Also

- [var isCancelled: Bool](operation/iscancelled.md)
  A Boolean value indicating whether the operation has been cancelled


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/cancel())*