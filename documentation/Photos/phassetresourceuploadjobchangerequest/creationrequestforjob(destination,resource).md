# creationRequestForJob(destination:resource:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Creates an asset resource upload job and returns the change request.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 27.0+

## Declaration

```swift
class func creationRequestForJob(destination: URLRequest, resource: PHAssetResource) -> Self
```

```objc
+ (instancetype) creationRequestForJobWithDestination:(NSURLRequest *) destination resource:(PHAssetResource *) resource;
```

#### Return Value

A change request for the created job.

#### Discussion

This method creates an upload job and returns a change request that can be used to access the placeholder for the created job. Use the placeholder to obtain the local identifier before the change block completes.

If the number of jobs exceeds [`jobLimit`](../phassetresourceuploadjob/joblimit.md) the photo library [`performChanges(_:completionHandler:)`](../phphotolibrary/performchanges%28_,completionhandler%29.md) request will fail with a [`PHPhotosError.Code.limitExceeded`](../phphotoserror-swift.struct/code/limitexceeded.md) error. To generate jobs after this limit is triggered, you must acknowledge succeeded/failed jobs, and wait for the registered/pending ones to finish uploading, which will make those jobs also succeeded/failed.

## Parameters

- `destination`: The destination [`NSURLRequest`](../../Foundation/nsurlrequest.md) to which this asset resource will be sent.
- `resource`: The asset resource to be uploaded.

## See Also

### Creating jobs
- [class func creationRequestForDownloadJob(resource: PHAssetResource) -> Self](./creationrequestfordownloadjob%28resource%29.md)
  Creates a download-only job request for the specified asset resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest/creationrequestforjob(destination:resource:))*