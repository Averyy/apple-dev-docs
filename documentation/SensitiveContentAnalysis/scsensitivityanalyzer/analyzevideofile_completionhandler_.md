# analyzeVideoFile:completionHandler:

**Framework**: Sensitive Content Analysis  
**Kind**: method  
**Role**: Instance Method

Analyzes a video file on disk at the given URL and runs the given code on completion.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.0+

## Declaration

```objc
- (NSProgress *) analyzeVideoFile:(NSURL *) fileURL completionHandler:(void (^)(SCSensitivityAnalysis *results, NSError *error)) completionHandler;
```

## Mentions

- [Testing your app’s response to sensitive media](../testing-your-app-s-response-to-sensitive-media.md)

## Return Value

An object that indicates how far analysis progresses while the system checks the video for sensitive content.

## Discussion

The completion handler:

- Runs on an unspecified queue
- Provides a `results` parameter that indicates whether checked content contains nudity.

## Parameters

- `fileURL`: A URL to a video file on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalyzer/analyzevideofile:completionhandler:)*