# shared

**Framework**: Media Intelligence  
**Kind**: property  
**Role**: Type Property

The shared video analyzer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static let shared: VideoAnalyzer
```

## Mentions

- [Finding the best moments in a video](../finding-the-best-moments-in-a-video.md)

## See Also

### Analyzing a video asset
- [VideoAnalyzer.Request](./request.md)
  A type that describes a video analysis operation.
- [VideoAnalyzer.Result](./result.md)
  A type that represents the output of a video analysis operation.
- [func analyze<each T>(MediaIntelligenceVideoAsset, for: repeat each T) async throws -> (repeat Result<(each T).Result, any Error>)](./analyze%28_,for%29.md)
  Analyzes a video asset using the specified requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/videoanalyzer/shared)*