# AVAssetImageGenerator.Result

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the result of an image generation request.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum Result
```

```c
enum AVAssetImageGeneratorResult : NSInteger;
```

## Overview

The constants used in the block completion handler for [`generateCGImagesAsynchronously(forTimes:completionHandler:)`](./generatecgimagesasynchronously%28fortimes,completionhandler%29.md).

## Topics

### Results
- [AVAssetImageGenerator.Result.succeeded](./result/succeeded.md)
  A result that indicates that image generation succeeded.
- [AVAssetImageGenerator.Result.failed](./result/failed.md)
  A result that indicates that image generation failed.
- [AVAssetImageGenerator.Result.cancelled](./result/cancelled.md)
  A result that indicates you canceled image generation.
### Initializers
- [init?(rawValue: Int)](./result/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Data types
- [typealias AVAssetImageGeneratorCompletionHandler](../avassetimagegeneratorcompletionhandler.md)
  A type alias for a closure that provides the result of an image generation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/result)*