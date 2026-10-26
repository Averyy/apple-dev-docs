# PHBackgroundResourceUploadJobExtension

**Framework**: Photos  
**Kind**: protocol  
**Role**: Protocol

A protocol to interact with asset resource upload jobs during background processing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
protocol PHBackgroundResourceUploadJobExtension : AppExtension
```

## Mentions

- [Uploading asset resources in the background](../PhotoKit/uploading-asset-resources-in-the-background.md)

#### Overview

Use this protocol to create, acknowledge, retry asset resource upload jobs.

## Topics

### Instance Methods
- [func processJobs() async -> PHBackgroundResourceUploadProcessingResult](./phbackgroundresourceuploadjobextension/processjobs%28%29.md)
  Request to initiate processing background upload jobs.
- [func willTerminate() async](./phbackgroundresourceuploadjobextension/willterminate%28%29.md)
  Called by the host before suspending or terminating the extension process. Extension clients should use this to stop any in-progress work. When the extension is activated again, a new call will be made by the host.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/appextension.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phbackgroundresourceuploadjobextension)*