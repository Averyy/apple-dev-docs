# PHAssetResourceUploadJob.Action

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

An action to perform on an upload job.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
enum Action
```

```c
enum PHAssetResourceUploadJobAction : NSInteger;
```

#### Overview

Determine the available jobs for an action by calling the [`fetchJobs(action:options:)`](./fetchjobs%28action,options%29.md) method.

## Topics

### Actions
- [PHAssetResourceUploadJob.Action.acknowledge](./action/acknowledge.md)
  A job that requires acknowledgement.
- [PHAssetResourceUploadJob.Action.retry](./action/retry.md)
  A job to retry processing.
### Initializers
- [init?(rawValue: Int)](./action/init%28rawvalue%29.md)
### Enumeration Cases
- [PHAssetResourceUploadJob.Action.process](./action/process.md)
  A job to process.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Fetching jobs
- [class var jobLimit: Int](./joblimit.md)
  The maximum number of unacknowledged upload jobs allowed.
- [class func fetchJobs(action: PHAssetResourceUploadJob.Action, options: PHFetchOptions?) -> PHFetchResult<PHAssetResourceUploadJob>](./fetchjobs%28action,options%29.md)
  Returns all asset resource upload jobs applicable for a given action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjob/action)*