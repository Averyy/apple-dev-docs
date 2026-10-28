# PHAssetResourceUploadJob.Action.retry

**Framework**: Photos  
**Kind**: case  
**Role**: Case

A job to retry processing.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+

## Declaration

```swift
case retry
```

```c
PHAssetResourceUploadJobActionRetry
```

## Mentions

- [Uploading asset resources in the background](../../../PhotoKit/uploading-asset-resources-in-the-background.md)

## Discussion

A retryable job has a [`state`](../state-swift.property.md) of `failed` and hasn’t previously been retried.

Call [`retry(destination:)`](../../phassetresourceuploadjobchangerequest/retry%28destination%29.md) to retry the job.

## See Also

### Actions
- [PHAssetResourceUploadJob.Action.acknowledge](./acknowledge.md)
  A job that requires acknowledgement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjob/action/retry)*