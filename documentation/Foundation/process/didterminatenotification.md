# didTerminateNotification

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Posted when the task has stopped execution.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class let didTerminateNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSTaskDidTerminateNotification;
```

## Discussion

The notification object is the `NSTask` object that the system terminated. This notification doesn’t contain a `userInfo` dictionary.

The system posts this notification from the thread in which the `NSTask` object called [`launch()`](./launch%28%29.md). When launching a task from a secondary thread or background queue, you can use the [`terminationHandler`](./terminationhandler.md) property instead for greater control over the execution context of any operations to be performed after the task finishes.

This notification can be posted either when the task has exited normally or as a result of [`terminate()`](./terminate%28%29.md) being sent to the `NSTask` object. If the `NSTask` object gets released, however, this notification won’t get sent, as the port the message would have been sent on was released as part of the task release. The observer method can use [`terminationStatus`](./terminationstatus.md) to determine why the task died.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/didterminatenotification)*