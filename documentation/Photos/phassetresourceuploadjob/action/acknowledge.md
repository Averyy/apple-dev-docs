# PHAssetResourceUploadJob.Action.acknowledge

**Framework**: Photos  
**Kind**: case  
**Role**: Case

A job that requires acknowledgement.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+

## Declaration

```swift
case acknowledge
```

```c
PHAssetResourceUploadJobActionAcknowledge
```

## Mentions

- [Uploading asset resources in the background](../../../PhotoKit/uploading-asset-resources-in-the-background.md)

#### Discussion

An acknowledgeable job has a [`state`](../state-swift.property.md) of `succeeded` or `failed` and hasn’t been acknowledged.

Call [`acknowledge()`](../../phassetresourceuploadjobchangerequest/acknowledge%28%29.md) to acknowledge a job and free queue capacity for new uploads.

## See Also

### Actions
- [PHAssetResourceUploadJob.Action.retry](./retry.md)
  A job to retry processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjob/action/acknowledge)*