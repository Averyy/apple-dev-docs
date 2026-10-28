# PHBackgroundResourceUploadExtension

**Framework**: Photos  
**Kind**: protocol  
**Role**: Protocol

A protocol to interact with asset resource upload jobs during background processing.

**Availability**:
- iOS 26.1+ - Deprecated in 27.0
- iPadOS 26.1+ - Deprecated in 27.0

> **Deprecated**: Adopt PHBackgroundResourceUploadJobExtension instead

## Declaration

```swift
protocol PHBackgroundResourceUploadExtension : AppExtension
```

## Mentions

- [Uploading asset resources in the background](../PhotoKit/uploading-asset-resources-in-the-background.md)

## Overview

Use this protocol to create, acknowledge, retry asset resource upload jobs.

## Topics

### Processing upload requests
- [func process() -> PHBackgroundResourceUploadProcessingResult](./phbackgroundresourceuploadextension/process%28%29.md)
  Request to initiate processing background upload jobs.
- [enum PHBackgroundResourceUploadProcessingResult](./phbackgroundresourceuploadprocessingresult.md)
### Handling termination
- [func notifyTermination()](./phbackgroundresourceuploadextension/notifytermination%28%29.md)
  This notification will be called if the host is going to suspend/terminate the current execution. Extension clients should use this to stop the current execution. When the extension is activated, a new call will be presented by the host.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/appextension.md)

## See Also

### Background resource upload extensions
- [Uploading asset resources in the background](../PhotoKit/uploading-asset-resources-in-the-background.md)
  Enable reliable cloud backup for photo library assets with background processing.
- [class PHAssetResourceUploadJob](./phassetresourceuploadjob.md)
  An object that represents a request to upload an asset resource.
- [class PHAssetResourceUploadJobChangeRequest](./phassetresourceuploadjobchangerequest.md)
  Use within an application’s `com.apple.photos.background-upload` extension to create and change [`PHAssetResourceUploadJob`](./phassetresourceuploadjob.md) records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phbackgroundresourceuploadextension)*