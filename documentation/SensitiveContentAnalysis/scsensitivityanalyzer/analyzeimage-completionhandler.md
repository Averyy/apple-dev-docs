# analyzeImage(_:completionHandler:)

**Framework**: SensitiveContentAnalysis  
**Kind**: method

Analyzes an image for sensitive content and runs code on completion.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.0+

## Declaration

```swift
func analyzeImage(_ image: CGImage) async throws -> SCSensitivityAnalysis
```

## Mentions

- [Testing your app’s response to sensitive media](testing-your-app-s-response-to-sensitive-media.md)

#### Discussion

The completion handler:

- Runs on an unspecified queue.
- Provides a `results` parameter that indicates if checked content contains nudity.

## Parameters

- `image`: An image in memory.
- `completionHandler`: Code that your app provides for the system to run on completion.

## See Also

- [func analyzeImage(at: URL, completionHandler: (SCSensitivityAnalysis?, (any Error)?) -> Void)](scsensitivityanalyzer/analyzeimage(at:completionhandler:).md)
  Analyzes an image file on disk at a URL and runs code on completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalyzer/analyzeimage(_:completionhandler:))*