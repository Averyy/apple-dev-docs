# placeholderForCreatedAssetResourceUploadJob

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A placeholder for the asset resource upload job created by this request.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var placeholderForCreatedAssetResourceUploadJob: PHObjectPlaceholder? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) PHObjectPlaceholder * placeholderForCreatedAssetResourceUploadJob;
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

## Discussion

The placeholder can be used to obtain the local identifier of the job that will be created when the change block completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest/placeholderforcreatedassetresourceuploadjob)*