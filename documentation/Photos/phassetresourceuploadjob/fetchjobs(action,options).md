# fetchJobs(action:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Returns all asset resource upload jobs applicable for a given action.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
class func fetchJobs(action: PHAssetResourceUploadJob.Action, options: PHFetchOptions?) -> PHFetchResult<PHAssetResourceUploadJob>
```

```objc
+ (PHFetchResult<PHAssetResourceUploadJob *> *) fetchJobsWithAction:(PHAssetResourceUploadJobAction) action options:(PHFetchOptions *) options;
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

## Return Value

The jobs available on which you can apply an action found in [`PHAssetResourceUploadJob.Action`](./action.md).

## Parameters

- `action`: The actions a client can take on a job.
- `options`: The fetch options to be passed in.

## See Also

### Fetching jobs
- [class var jobLimit: Int](./joblimit.md)
  The maximum number of unacknowledged upload jobs allowed.
- [PHAssetResourceUploadJob.Action](./action.md)
  An action to perform on an upload job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjob/fetchjobs(action:options:))*