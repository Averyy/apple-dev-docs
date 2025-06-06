# ProgressReporting

**Framework**: Foundation  
**Kind**: protocol

An interface for objects that report progress using a single progress instance.

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
protocol ProgressReporting : NSObjectProtocol
```

#### Overview

Create the returned progress object using [`ProgressReporting`](progressreporting.md). The resulting object has no parent allowing the caller to add it to a progress tree using [`ProgressReporting`](progressreporting.md).

You can return a single progress object or a progress tree. If you are creating a progress tree, add the children to the returned progress object as described in [`Reporting Progress for Multiple Operations`](progress#Reporting-Progress-for-Multiple-Operations.md).

You are responsible for setting and updating the [`ProgressReporting`](progressreporting.md) of any [`Progress`](progress.md) object you create.

## Topics

### Custom Class Progress
- [var progress: Progress](progressreporting/progress.md)
  The progress object returned by the class.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSBundleResourceRequest](nsbundleresourcerequest.md)
- [OperationQueue](operationqueue.md)
- [URLSessionDataTask](urlsessiondatatask.md)
- [URLSessionDownloadTask](urlsessiondownloadtask.md)
- [URLSessionStreamTask](urlsessionstreamtask.md)
- [URLSessionTask](urlsessiontask.md)
- [URLSessionUploadTask](urlsessionuploadtask.md)
- [URLSessionWebSocketTask](urlsessionwebsockettask.md)

## See Also

- [class Progress](progress.md)
  An object that conveys ongoing progress to the user for a specified task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressreporting)*