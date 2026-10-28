# PHAssetResourceUploadJobChangeRequest

**Framework**: Photos  
**Kind**: class  
**Role**: Class

Use within an application’s `com.apple.photos.background-upload` extension to create and change [`PHAssetResourceUploadJob`](./phassetresourceuploadjob.md) records.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
class PHAssetResourceUploadJobChangeRequest
```

```objc
@interface PHAssetResourceUploadJobChangeRequest : PHChangeRequest
```

## Overview

When the extension’s principal class receives a call to `process` background uploads, it can create new [`PHAssetResourceUploadJob`](./phassetresourceuploadjob.md)s through calls to perform changes on a PHPhotoLibrary using [`PHAssetResourceUploadJobChangeRequest`](./phassetresourceuploadjobchangerequest.md) and any in-flight upload jobs can be handled by updating their state to mark them as acknowledged, or to be retried. The maximum number of jobs that can be in flight is limited to the [`jobLimit`](./phassetresourceuploadjob/joblimit.md).

[`PHAssetResourceUploadJobChangeRequest`](./phassetresourceuploadjobchangerequest.md) can only be created or used within a photo library change block. For details on change blocks, see [`PHPhotoLibrary`](./phphotolibrary.md).

## Topics

### Creating a change request
- [convenience init?(for: PHAssetResourceUploadJob)](./phassetresourceuploadjobchangerequest/init%28for%29.md)
  Creates a request for modifying the specified upload job.
### Creating jobs
- [class func creationRequestForDownloadJob(resource: PHAssetResource) -> Self](./phassetresourceuploadjobchangerequest/creationrequestfordownloadjob%28resource%29.md)
  Creates a download-only job request for the specified asset resource.
- [class func creationRequestForJob(destination: URLRequest, resource: PHAssetResource) -> Self](./phassetresourceuploadjobchangerequest/creationrequestforjob%28destination,resource%29.md)
  Creates an asset resource upload job and returns the change request.
### Processing jobs
- [func acknowledge()](./phassetresourceuploadjobchangerequest/acknowledge%28%29.md)
  Acknowledges a successful or failed job. Jobs must be acknowledged to free up space for [`jobLimit`](./phassetresourceuploadjob/joblimit.md).
- [func retry(destination: URLRequest?)](./phassetresourceuploadjobchangerequest/retry%28destination%29.md)
  Retries a job that is failed, unacknowledged, and has not been retried before. Successful retries also free up space for [`jobLimit`](./phassetresourceuploadjob/joblimit.md).
- [func cancel()](./phassetresourceuploadjobchangerequest/cancel%28%29.md)
  Cancels an upload job that is registered or pending.
### Accessing details about the job
- [var placeholderForCreatedAssetResourceUploadJob: PHObjectPlaceholder?](./phassetresourceuploadjobchangerequest/placeholderforcreatedassetresourceuploadjob.md)
  A placeholder for the asset resource upload job created by this request.
### Deprecated
- [class func createJob(destination: URLRequest, resource: PHAssetResource)](./phassetresourceuploadjobchangerequest/createjob%28destination,resource%29.md)
  Creates an asset resource upload job.
### Initializers
- [convenience init?(forUploadJob: PHAssetResourceUploadJob)](./phassetresourceuploadjobchangerequest/init%28foruploadjob%29.md)

## Relationships

### Inherits From
- [PHChangeRequest](./phchangerequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Background resource upload extensions
- [Uploading asset resources in the background](../PhotoKit/uploading-asset-resources-in-the-background.md)
  Enable reliable cloud backup for photo library assets with background processing.
- [protocol PHBackgroundResourceUploadExtension](./phbackgroundresourceuploadextension.md)
  A protocol to interact with asset resource upload jobs during background processing.
- [class PHAssetResourceUploadJob](./phassetresourceuploadjob.md)
  An object that represents a request to upload an asset resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest)*