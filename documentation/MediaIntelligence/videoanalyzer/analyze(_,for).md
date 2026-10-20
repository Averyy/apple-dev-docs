# analyze(_:for:)

**Framework**: Media Intelligence  
**Kind**: method  
**Role**: Instance Method

Analyzes a video asset using the specified requests.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final nonisolated(nonsending) func analyze<each T>(_ asset: MediaIntelligenceVideoAsset, for request: repeat each T) async throws -> (repeat Result<(each T).Result, any Error>) where repeat each T : VideoAnalyzer.Request
```

## Mentions

- [Finding the best moments in a video](../finding-the-best-moments-in-a-video.md)

#### Return Value

A tuple of [`Result`](../../Swift/result.md) values, one per request.

#### Discussion

Pass one or more values of type [`VideoAnalyzer.Request`](./request.md). The method returns a tuple containing one [`Result`](../../Swift/result.md) per request, in the same order you provided them. Check each element individually because a failure in one request doesn’t affect the others.

## Parameters

- `asset`: The video asset to analyze.
- `request`: One or more analysis requests to perform.

## See Also

### Analyzing a video asset
- [static let shared: VideoAnalyzer](./shared.md)
  The shared video analyzer.
- [VideoAnalyzer.Request](./request.md)
  A type that describes a video analysis operation.
- [VideoAnalyzer.Result](./result.md)
  A type that represents the output of a video analysis operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/videoanalyzer/analyze(_:for:))*