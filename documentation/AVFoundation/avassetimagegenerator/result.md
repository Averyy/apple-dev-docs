# AVAssetImageGenerator.Result

**Framework**: AVFoundation  
**Kind**: enum

Constants that indicate the result of an image generation request.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum Result
```

#### Overview

The constants used in the block completion handler for [`generateCGImagesAsynchronously(forTimes:completionHandler:)`](avassetimagegenerator/generatecgimagesasynchronously(fortimes:completionhandler:).md).

## Topics

### Results
- [AVAssetImageGenerator.Result.succeeded](avassetimagegenerator/result/succeeded.md)
  A result that indicates that image generation succeeded.
- [AVAssetImageGenerator.Result.failed](avassetimagegenerator/result/failed.md)
  A result that indicates that image generation failed.
- [AVAssetImageGenerator.Result.cancelled](avassetimagegenerator/result/cancelled.md)
  A result that indicates you canceled image generation.
### Initializers
- [init?(rawValue: Int)](avassetimagegenerator/result/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [typealias AVAssetImageGeneratorCompletionHandler](avassetimagegeneratorcompletionhandler.md)
  A type alias for a closure that provides the result of an image generation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/result)*