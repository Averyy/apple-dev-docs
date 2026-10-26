# responseHeaderFields

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The HTTP response headers received from the server upon completion of the upload.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 27.0+

## Declaration

```swift
var responseHeaderFields: [String : String]? { get }
```

```objc
@property (copy, readonly, nullable) NSDictionary<NSString *,NSString *> * responseHeaderFields;
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

#### Return Value

A dictionary of response header fields, or `nil` if the job has not completed or no HTTP response was received.

#### Discussion

This property is populated when the job reaches a terminal state (`PHAssetResourceUploadJobStateSucceeded` or `PHAssetResourceUploadJobStateFailed`). It contains the HTTP response headers returned by the destination server.

Header field names are normalized to lowercase for consistent lookup.

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
- [var error: (any Error)?](./error.md)
  The error that caused the job to fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjob/responseheaderfields)*