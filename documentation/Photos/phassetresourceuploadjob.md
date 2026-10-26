# PHAssetResourceUploadJob

**Framework**: Photos  
**Kind**: class  
**Role**: Class

An object that represents a request to upload an asset resource.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
class PHAssetResourceUploadJob
```

```objc
@interface PHAssetResourceUploadJob : PHObject
```

#### Overview

Use within an application’s `com.apple.photos.background-upload` extension to request an upload of a [`PHAssetResource`](./phassetresource.md) to a destination [`NSURLRequest`](../Foundation/nsurlrequest.md).

When the extension’s principal class receives a call to [`process()`](./phbackgroundresourceuploadextension/process%28%29.md) background uploads, it can create new [`PHAssetResourceUploadJob`](./phassetresourceuploadjob.md) objects using [`PHAssetResourceUploadJobChangeRequest`](./phassetresourceuploadjobchangerequest.md).

The maximum number of jobs that can be in flight is limited to the [`jobLimit`](./phassetresourceuploadjob/joblimit.md). To make space for new jobs, you must call [`fetchJobs(action:options:)`](./phassetresourceuploadjob/fetchjobs%28action,options%29.md) and retry/acknowledge them with [`acknowledge()`](./phassetresourceuploadjobchangerequest/acknowledge%28%29.md) or [`retry(destination:)`](./phassetresourceuploadjobchangerequest/retry%28destination%29.md) respectively.

## Topics

### Fetching jobs
- [class var jobLimit: Int](./phassetresourceuploadjob/joblimit.md)
  The maximum number of unacknowledged upload jobs allowed.
- [class func fetchJobs(action: PHAssetResourceUploadJob.Action, options: PHFetchOptions?) -> PHFetchResult<PHAssetResourceUploadJob>](./phassetresourceuploadjob/fetchjobs%28action,options%29.md)
  Returns all asset resource upload jobs applicable for a given action.
- [PHAssetResourceUploadJob.Action](./phassetresourceuploadjob/action.md)
  An action to perform on an upload job.
### Inspecting a job
- [var type: PHAssetResourceUploadJob.Type](./phassetresourceuploadjob/type-swift.property.md)
  The type of this upload job.
- [PHAssetResourceUploadJob.Type](./phassetresourceuploadjob/type-swift.enum.md)
  Indicates whether a job downloads and then uploads an asset to the server or only downloads it.
- [var destination: URLRequest](./phassetresourceuploadjob/destination.md)
  The destination to send the job’s resource.
- [var resource: PHAssetResource](./phassetresourceuploadjob/resource.md)
  The asset resource this job promises to upload.
- [var state: PHAssetResourceUploadJob.State](./phassetresourceuploadjob/state-swift.property.md)
  The state of this upload job.
- [PHAssetResourceUploadJob.State](./phassetresourceuploadjob/state-swift.enum.md)
  The stages of an upload job’s life cycle, from registered with the system through to completion.
- [var error: (any Error)?](./phassetresourceuploadjob/error.md)
  The error that caused the job to fail.
- [var responseHeaderFields: [String : String]?](./phassetresourceuploadjob/responseheaderfields.md)
  The HTTP response headers received from the server upon completion of the upload.

## Relationships

### Inherits From
- [PHObject](./phobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Background resource upload extensions
- [Uploading asset resources in the background](../PhotoKit/uploading-asset-resources-in-the-background.md)
  Enable reliable cloud backup for photo library assets with background processing.
- [protocol PHBackgroundResourceUploadExtension](./phbackgroundresourceuploadextension.md)
  A protocol to interact with asset resource upload jobs during background processing.
- [class PHAssetResourceUploadJobChangeRequest](./phassetresourceuploadjobchangerequest.md)
  Use within an application’s `com.apple.photos.background-upload` extension to create and change [`PHAssetResourceUploadJob`](./phassetresourceuploadjob.md) records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjob)*