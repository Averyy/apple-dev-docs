# AVAssetImageGenerator.Images

**Framework**: AVFoundation  
**Kind**: struct

An asynchronous sequence of images created by an image generator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Images
```

## Mentions

- [Creating images from a video asset](creating-images-from-a-video-asset.md)

## Topics

### Creating an Iterator
- [func makeAsyncIterator() -> AVAssetImageGenerator.Images](avassetimagegenerator/images/makeasynciterator.md)
  Creates an asynchronous iterator that produces elements of this type.
### Iterating Elements
- [func next() async -> AVAssetImageGenerator.Images.Element?](avassetimagegenerator/images/next.md)
  Returns the next element in the sequence.
- [AVAssetImageGenerator.Images.Element](avassetimagegenerator/images/element.md)
  An element that provides the result of an image generation request.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)
- [AsyncSequence](../Swift/AsyncSequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images)*