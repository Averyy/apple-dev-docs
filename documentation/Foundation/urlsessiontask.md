# URLSessionTask

**Framework**: Foundation  
**Kind**: class

A task, like downloading a specific resource, performed in a URL session.

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
class URLSessionTask
```

## Mentions

- [Uploading streams of data](uploading-streams-of-data.md)
- [Uploading data to a website](uploading-data-to-a-website.md)

#### Overview

The [`URLSessionTask`](urlsessiontask.md) class is the base class for tasks in a URL session. Tasks are always part of a session; you create a task by calling one of the task creation methods on a [`URLSession`](urlsession.md) instance. The method you call determines the type of task.

- Use [`URLSession`](urlsession.md)‘s [`dataTask(with:)`](urlsession/datatask(with:)-10dy7.md) and related methods to create [`URLSessionDataTask`](urlsessiondatatask.md) instances. Data tasks request a resource, returning the server’s response as one or more `NSData` objects in memory. They are supported in default, ephemeral, and shared sessions, but are not supported in background sessions.
- Use [`URLSession`](urlsession.md)‘s [`uploadTask(with:from:)`](urlsession/uploadtask(with:from:).md) and related methods to create [`URLSessionUploadTask`](urlsessionuploadtask.md) instances. Upload tasks are like data tasks, except that they make it easier to provide a request body so you can upload data before retrieving the server’s response. Additionally, upload tasks are supported in background sessions.
- Use [`URLSession`](urlsession.md)’s [`downloadTask(with:)`](urlsession/downloadtask(with:)-1onj.md) and related methods to create [`URLSessionDownloadTask`](urlsessiondownloadtask.md) instances. Download tasks download a resource directly to a file on disk. Download tasks are supported in any type of session.
- Use [`URLSession`](urlsession.md)’s [`streamTask(withHostName:port:)`](urlsession/streamtask(withhostname:port:).md) or [`streamTask(with:)`](urlsession/streamtask(with:).md) to create [`URLSessionStreamTask`](urlsessionstreamtask.md) instances. Stream tasks establish a TCP/IP connection from a host name and port or a net service object.

After you create a task, you start it by calling its [`resume()`](urlsessiontask/resume().md) method. The session then maintains a strong reference to the task until the request finishes or fails; you don’t need to maintain a reference to the task unless it’s useful for your app’s internal bookkeeping.

> **Note**:  All task properties support key-value observing.

## Topics

### Controlling the task state
- [func cancel()](urlsessiontask/cancel.md)
  Cancels the task.
- [func resume()](urlsessiontask/resume.md)
  Resumes the task, if it is suspended.
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
### Obtaining task progress
- [var progress: Progress](urlsessiontask/progress.md)
  A representation of the overall task progress.
- [var countOfBytesExpectedToReceive: Int64](urlsessiontask/countofbytesexpectedtoreceive.md)
  The number of bytes that the task expects to receive in the response body.
- [var countOfBytesReceived: Int64](urlsessiontask/countofbytesreceived.md)
  The number of bytes that the task has received from the server in the response body.
- [var countOfBytesExpectedToSend: Int64](urlsessiontask/countofbytesexpectedtosend.md)
  The number of bytes that the task expects to send in the request body.
- [var countOfBytesSent: Int64](urlsessiontask/countofbytessent.md)
  The number of bytes that the task has sent to the server in the request body.
- [let NSURLSessionTransferSizeUnknown: Int64](nsurlsessiontransfersizeunknown.md)
  The total size of the transfer cannot be determined.
### Obtaining general task information
- [var currentRequest: URLRequest?](urlsessiontask/currentrequest.md)
  The URL request object currently being handled by the task.
- [var originalRequest: URLRequest?](urlsessiontask/originalrequest.md)
  The original request object passed when the task was created.
- [var response: URLResponse?](urlsessiontask/response.md)
  The server’s response to the currently active request.
- [var taskDescription: String?](urlsessiontask/taskdescription.md)
  An app-provided string value for the current task.
- [var taskIdentifier: Int](urlsessiontask/taskidentifier.md)
  An identifier uniquely identifying the task within a given session.
- [var error: (any Error)?](urlsessiontask/error.md)
  An error object that indicates why the task failed.
### Determining task behavior
- [var prefersIncrementalDelivery: Bool](urlsessiontask/prefersincrementaldelivery.md)
  A Boolean value that determines whether to deliver a partial response body in increments.
### Using a task-specific delegate
- [var delegate: (any URLSessionTaskDelegate)?](urlsessiontask/delegate.md)
  A delegate specific to the task.
- [protocol URLSessionTaskDelegate](urlsessiontaskdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events.
### Scheduling tasks
- [var countOfBytesClientExpectsToReceive: Int64](urlsessiontask/countofbytesclientexpectstoreceive.md)
  A best-guess upper bound on the number of bytes the client expects to receive.
- [var countOfBytesClientExpectsToSend: Int64](urlsessiontask/countofbytesclientexpectstosend.md)
  A best-guess upper bound on the number of bytes the client expects to send.
- [let NSURLSessionTransferSizeUnknown: Int64](nsurlsessiontransfersizeunknown.md)
  The total size of the transfer cannot be determined.
- [var earliestBeginDate: Date?](urlsessiontask/earliestbegindate.md)
  The earliest date at which the network load should begin.
### Deprecated
- [init()](urlsessiontask/init.md)
  Initializes an empty URL sesson task.
- [class func new() -> Self](urlsessiontask/new.md)
  Creates a new URL session task.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [URLSessionDataTask](urlsessiondatatask.md)
- [URLSessionDownloadTask](urlsessiondownloadtask.md)
- [URLSessionStreamTask](urlsessionstreamtask.md)
- [URLSessionWebSocketTask](urlsessionwebsockettask.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [ProgressReporting](progressreporting.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Fetching website data into memory](fetching-website-data-into-memory.md)
  Receive data directly into memory by creating a data task from a URL session.
- [Analyzing HTTP traffic with Instruments](analyzing-http-traffic-with-instruments.md)
  Measure HTTP-based network performance and usage of your apps.
- [class URLSession](urlsession.md)
  An object that coordinates a group of related, network data transfer tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask)*