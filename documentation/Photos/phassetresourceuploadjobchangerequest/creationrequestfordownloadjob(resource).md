# creationRequestForDownloadJob(resource:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Creates a download-only job request for the specified asset resource.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 27.0+

## Declaration

```swift
class func creationRequestForDownloadJob(resource: PHAssetResource) -> Self
```

```objc
+ (instancetype) creationRequestForDownloadJobWithResource:(PHAssetResource *) resource;
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

#### Return Value

A change request for the created job.

#### Discussion

This method registers a job that requests an asset resource be downloaded from iCloud to the device without uploading it to a remote server. The download operation is performed asynchronously by the system over time. This is useful when you need to ensure a resource is available locally for processing.

The job will transition through the same states as upload jobs (`PHAssetResourceUploadJobStateRegistered`, `PHAssetResourceUploadJobStatePending`, and eventually `PHAssetResourceUploadJobStateSucceeded` or `PHAssetResourceUploadJobStateFailed`), but will only perform a download operation.

Use `fetchJobsWithAction:options:` to check the job’s state. When the job reaches `PHAssetResourceUploadJobStateSucceeded`, the download has completed successfully.

> **Note**: The system may subsequently purge the downloaded resource due to system conditions.

## Parameters

- `resource`: The asset resource to download.

## See Also

### Creating jobs
- [class func creationRequestForJob(destination: URLRequest, resource: PHAssetResource) -> Self](./creationrequestforjob%28destination,resource%29.md)
  Creates an asset resource upload job and returns the change request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest/creationrequestfordownloadjob(resource:))*