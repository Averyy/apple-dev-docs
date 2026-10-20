# resume()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Resumes the task, if it is suspended.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func resume()
```

```objc
- (void) resume;
```

## Mentions

- [Downloading files from websites](../downloading-files-from-websites.md)
- [Uploading streams of data](../uploading-streams-of-data.md)
- [Downloading files in the background](../downloading-files-in-the-background.md)
- [Fetching website data into memory](../fetching-website-data-into-memory.md)
- [Pausing and resuming downloads](../pausing-and-resuming-downloads.md)
- [Pausing and resuming uploads](../pausing-and-resuming-uploads.md)
- [Uploading data to a website](../uploading-data-to-a-website.md)

#### Discussion

Newly-initialized tasks begin in a suspended state, so you need to call this method to start the task.

## See Also

### Controlling the task state
- [func cancel()](./cancel%28%29.md)
  Cancels the task.
- [func suspend()](./suspend%28%29.md)
  Temporarily suspends a task.
- [var state: URLSessionTask.State](./state-swift.property.md)
  The current state of the task—active, suspended, in the process of being canceled, or completed.
- [URLSessionTask.State](./state-swift.enum.md)
  Constants for determining the current state of a task.
- [var priority: Float](./priority.md)
  The relative priority at which you’d like a host to handle the task, specified as a floating point value between `0.0` (lowest priority) and `1.0` (highest priority).
- [URL session task priority](../url-session-task-priority.md)
  Constants for providing task priority hints to a host, used with the [`priority`](./priority.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/resume())*