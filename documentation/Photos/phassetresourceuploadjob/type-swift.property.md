# type

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The type of this upload job.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var type: PHAssetResourceUploadJob.Type { get }
```

```objc
@property (readonly) PHAssetResourceUploadJobType type;
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

## See Also

### Inspecting a job
- [PHAssetResourceUploadJob.Type](./type-swift.enum.md)
  Indicates whether a job downloads and then uploads an asset to the server or only downloads it.
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

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjob/type-swift.property)*