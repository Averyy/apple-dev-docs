# processJobs()

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Request to initiate processing background upload jobs.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
func processJobs() async -> PHBackgroundResourceUploadProcessingResult
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

## Return Value

A result type of [`PHBackgroundResourceUploadProcessingResult`](../phbackgroundresourceuploadprocessingresult.md) based on the state of the processing task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phbackgroundresourceuploadjobextension/processjobs())*