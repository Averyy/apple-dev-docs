# analyzeImage(at:completionHandler:)

**Framework**: SensitiveContentAnalysis  
**Kind**: method

Analyzes an image file on disk at a URL and runs code on completion.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.0+

## Declaration

```swift
func analyzeImage(at fileURL: URL) async throws -> SCSensitivityAnalysis
```

#### Discussion

The completion handler:

- Runs on an unspecified queue.
- Provides a `results` parameter that indicates if checked content contains nudity.

## Parameters

- `fileURL`: The URL for an image file on disk.
- `completionHandler`: Code that your app provides for the system to run on completion.

## See Also

- [func analyzeImage(CGImage, completionHandler: (SCSensitivityAnalysis?, (any Error)?) -> Void)](scsensitivityanalyzer/analyzeimage(_:completionhandler:).md)
  Analyzes an image for sensitive content and runs code on completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalyzer/analyzeimage(at:completionhandler:))*