# exportClip(to:duration:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func exportClip(to url: URL, duration: TimeInterval) async throws
```

#### Discussion

Export buffered content as a clip to the specified URL

This method exports the most recent buffered samples as a video file. The export happens asynchronously and does not interrupt ongoing buffering - new samples continue to be buffered during export. The clip buffering output must be added to a stream before exports can be requested.

## Parameters

- `url`: URL containing absolute path for where to save the clip. Must be a file URL. The file will be created; if it already exists, it will be overwritten.
- `duration`: Length of time in seconds for clip export. The clip will contain the most recent samples from the buffer for this duration. Maximum duration is 15 seconds. If the requested duration exceeds available buffered content, the clip will contain all available buffered content.
- `completionHandler`: Handler called after clip export completes or fails. Will be passed an optional NSError in the SCStreamErrorDomain domain if there was an issue exporting the clip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scclipbufferingoutput/exportclip(to:duration:completionhandler:))*