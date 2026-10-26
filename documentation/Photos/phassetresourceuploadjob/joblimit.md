# jobLimit

**Framework**: Photos  
**Kind**: property  
**Role**: Type Property

The maximum number of unacknowledged upload jobs allowed.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
class var jobLimit: Int { get }
```

```objc
@property (class, readonly) NSInteger jobLimit;
```

#### Discussion

This includes jobs that are in-flight and those that have succeeded or failed.

## See Also

### Fetching jobs
- [class func fetchJobs(action: PHAssetResourceUploadJob.Action, options: PHFetchOptions?) -> PHFetchResult<PHAssetResourceUploadJob>](./fetchjobs%28action,options%29.md)
  Returns all asset resource upload jobs applicable for a given action.
- [PHAssetResourceUploadJob.Action](./action.md)
  An action to perform on an upload job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjob/joblimit)*