# cancel(taskRequestWithIdentifier:)

**Framework**: Background Tasks  
**Kind**: method  
**Role**: Instance Method

Cancel a previously scheduled task request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func cancel(taskRequestWithIdentifier identifier: String)
```

```objc
- (void) cancelTaskRequestWithIdentifier:(NSString *) identifier;
```

## Parameters

- `identifier`: The string identifier of the task request to cancel.

## See Also

### Canceling a task
- [func cancelAllTaskRequests()](./cancelalltaskrequests%28%29.md)
  Cancel all scheduled task requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/cancel(taskrequestwithidentifier:))*