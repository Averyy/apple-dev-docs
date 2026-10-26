# PHAssetResourceUploadJob.State

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

The stages of an upload job’s life cycle, from registered with the system through to completion.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
enum State
```

```c
enum PHAssetResourceUploadJobState : NSInteger;
```

## Topics

### States
- [PHAssetResourceUploadJob.State.registered](./state-swift.enum/registered.md)
  The job has been registered.
- [PHAssetResourceUploadJob.State.pending](./state-swift.enum/pending.md)
  A request has been made to send the asset resource to the destination, but has not yet been fulfilled.
- [PHAssetResourceUploadJob.State.succeeded](./state-swift.enum/succeeded.md)
  The job has sent over successfully.
- [PHAssetResourceUploadJob.State.failed](./state-swift.enum/failed.md)
  The job has failed to send over.
- [PHAssetResourceUploadJob.State.cancelled](./state-swift.enum/cancelled.md)
  The job has been cancelled.
### Initializers
- [init?(rawValue: Int)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting a job
- [var type: PHAssetResourceUploadJob.Type](./type-swift.property.md)
  The type of this upload job.
- [PHAssetResourceUploadJob.Type](./type-swift.enum.md)
  Indicates whether a job downloads and then uploads an asset to the server or only downloads it.
- [var destination: URLRequest](./destination.md)
  The destination to send the job’s resource.
- [var resource: PHAssetResource](./resource.md)
  The asset resource this job promises to upload.
- [var state: PHAssetResourceUploadJob.State](./state-swift.property.md)
  The state of this upload job.
- [var error: (any Error)?](./error.md)
  The error that caused the job to fail.
- [var responseHeaderFields: [String : String]?](./responseheaderfields.md)
  The HTTP response headers received from the server upon completion of the upload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjob/state-swift.enum)*