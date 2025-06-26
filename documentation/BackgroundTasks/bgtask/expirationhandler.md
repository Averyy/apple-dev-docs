# expirationHandler

**Framework**: Background Tasks  
**Kind**: property

A handler called shortly before the task’s background time expires.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var expirationHandler: (() -> Void)? { get set }
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md)

#### Discussion

The time allocated by the system for expiration handlers doesn’t vary with the number of background tasks. All expiration handlers must complete before the allocated time.

Not setting an expiration handler results in the system marking your task as complete and unsuccessful instead of sending a warning.

The manager sets the value `expirationHandler` to `nil` after the handler completes.

## Parameters

- `expirationHandler`: The handler may be called before the background process uses the full amount of its allocated time.

## See Also

- [func setTaskCompleted(success: Bool)](bgtask/settaskcompleted(success:).md)
  Informs the background task scheduler that the task is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtask/expirationhandler)*