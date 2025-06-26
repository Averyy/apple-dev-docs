# resume()

**Framework**: Foundation  
**Kind**: method

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

## Mentions

- [Downloading files from websites](downloading-files-from-websites.md)
- [Uploading streams of data](uploading-streams-of-data.md)
- [Downloading files in the background](downloading-files-in-the-background.md)
- [Fetching website data into memory](fetching-website-data-into-memory.md)
- [Pausing and resuming downloads](pausing-and-resuming-downloads.md)
- [Uploading data to a website](uploading-data-to-a-website.md)
- [Pausing and resuming uploads](pausing-and-resuming-uploads.md)

#### Discussion

Newly-initialized tasks begin in a suspended state, so you need to call this method to start the task.

## See Also

- [func cancel()](urlsessiontask/cancel.md)
  Cancels the task.
- [func suspend()](urlsessiontask/suspend.md)
  Temporarily suspends a task.
- [var state: URLSessionTask.State](urlsessiontask/state-swift.property.md)
  The current state of the task—active, suspended, in the process of being canceled, or completed.
- [URLSessionTask.State](urlsessiontask/state-swift.enum.md)
  Constants for determining the current state of a task.
- [var priority: Float](urlsessiontask/priority.md)
  The relative priority at which you’d like a host to handle the task, specified as a floating point value between `0.0` (lowest priority) and `1.0` (highest priority).
- [URL session task priority](url-session-task-priority.md)
  Constants for providing task priority hints to a host, used with the [`priority`](urlsessiontask/priority.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/resume())*