# error

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The error that caused the job to fail.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 27.0+

## Declaration

```swift
var error: (any Error)? { get }
```

```objc
@property (readonly, nullable) NSError * error;
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

## Return Value

An error object describing the failure, or `nil` if the job has not failed.

## Discussion

This property is populated when the job reaches the `PHAssetResourceUploadJobStateFailed` state. It provides detailed information about why the upload failed, including network errors, server errors, or client-side errors.

> **Note**: The error provided is sanitized and may not be the actual error returned from URLResponse.

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
- [PHAssetResourceUploadJob.State](./state-swift.enum.md)
  The stages of an upload job’s life cycle, from registered with the system through to completion.
- [var responseHeaderFields: [String : String]?](./responseheaderfields.md)
  The HTTP response headers received from the server upon completion of the upload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjob/error)*