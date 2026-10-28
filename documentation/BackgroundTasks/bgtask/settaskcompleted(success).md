# setTaskCompleted(success:)

**Framework**: Background Tasks  
**Kind**: method  
**Role**: Instance Method

Informs the background task scheduler that the task is complete.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setTaskCompleted(success: Bool)
```

```objc
- (void) setTaskCompletedWithSuccess:(BOOL) success;
```

## Mentions

- [Choosing Background Strategies for Your App](../choosing-background-strategies-for-your-app.md)

## Discussion

Not calling [`setTaskCompleted(success:)`](./settaskcompleted%28success%29.md) before the time for the task expires may result in the system killing your app.

You can reschedule an unsuccessful required task.

> ❗ **Important**: If you don’t set an expiration handler, the system will mark your task as complete and unsuccessful instead of sending a warning.

## Parameters

- `success`: A `Boolean` indicating if the task completed successfully or not.

## See Also

### Configuring a Task
- [var expirationHandler: (() -> Void)?](./expirationhandler.md)
  A handler called shortly before the task’s background time expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtask/settaskcompleted(success:))*