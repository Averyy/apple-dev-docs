# init(applyingFiltersTo:applier:isolation:)

**Framework**: AVFoundation  
**Kind**: init

Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init(applyingFiltersTo asset: AVAsset, applier: @escaping (AVCIImageFilteringParameters) async throws -> AVCIImageFilteringResult, isolation: isolated (any Actor)? = #isolation) async throws
```

#### Return Value

A new AVVideoComposition instance configured for Core Image filtering.

## Parameters

- `asset`: The asset whose configuration matches the intended use of the video composition.
- `applier`: A closure that AVFoundation calls when processing each video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/init(applyingfiltersto:applier:isolation:))*