# init(for:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Creates a request for modifying the specified upload job.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
convenience init?(for job: PHAssetResourceUploadJob)
```

```objc
+ (instancetype) changeRequestForUploadJob:(PHAssetResourceUploadJob *) job;
```

## Parameters

- `job`: A job to be modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest/init(for:))*