# createJob(destination:resource:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Creates an asset resource upload job.

**Availability**:
- iOS 26.1+ - Deprecated in 26.4
- iPadOS 26.1+ - Deprecated in 26.4
- Mac Catalyst 26.1+ - Deprecated in 26.4
- macOS 27.0+

## Declaration

```swift
class func createJob(destination: URLRequest, resource: PHAssetResource)
```

```objc
+ (void) createJobWithDestination:(NSURLRequest *) destination resource:(PHAssetResource *) resource;
```

#### Discussion

- Parameter:

  - destination: the destination NSURLRequest to which this asset resource will be sent.
  - resource: the asset resource to be uploaded.

If the number of jobs exceeds [`jobLimit`](../phassetresourceuploadjob/joblimit.md) the photo library [`performChanges(_:completionHandler:)`](../phphotolibrary/performchanges%28_,completionhandler%29.md) request will fail with a [`limitExceeded`](../phphotoserror-swift.struct/limitexceeded.md) error. To generate jobs after this limit is triggered, you must acknowledge succeeded/failed jobs, and wait for the registered/pending ones to finish uploading, which will make those jobs also succeeded/failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest/createjob(destination:resource:))*