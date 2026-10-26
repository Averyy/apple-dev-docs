# PHAssetResourceUploadJob.Type

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Indicates whether a job downloads and then uploads an asset to the server or only downloads it.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
enum `Type`
```

```c
enum PHAssetResourceUploadJobType : int16_t;
```

## Topics

### Enumeration Cases
- [PHAssetResourceUploadJob.Type.downloadOnly](./type-swift.enum/downloadonly.md)
  A download job type (will download the resource from iCloud if required)
- [PHAssetResourceUploadJob.Type.upload](./type-swift.enum/upload.md)
  An upload job type (will download the resource from iCloud if required. then upload)
### Initializers
- [init?(rawValue: Int16)](./type-swift.enum/init%28rawvalue%29.md)

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
- [var destination: URLRequest](./destination.md)
  The destination to send the job’s resource.
- [var resource: PHAssetResource](./resource.md)
  The asset resource this job promises to upload.
- [var state: PHAssetResourceUploadJob.State](./state-swift.property.md)
  The state of this upload job.
- [PHAssetResourceUploadJob.State](./state-swift.enum.md)
  The stages of an upload job’s life cycle, from registered with the system through to completion.
- [var error: (any Error)?](./error.md)
  The error that caused the job to fail.
- [var responseHeaderFields: [String : String]?](./responseheaderfields.md)
  The HTTP response headers received from the server upon completion of the upload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjob/type-swift.enum)*