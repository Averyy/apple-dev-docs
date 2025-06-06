# init(tags:sampleBuffer:)

**Framework**: Core Media  
**Kind**: init

Creates a new tagged buffer from tags and an existing sample buffer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(tags: [CMTag], sampleBuffer: CMSampleBuffer)
```

## Parameters

- `tags`: The tags to assign to the buffer.
- `sampleBuffer`: A sample buffer to associate with the tags.

## See Also

- [init(tags: [CMTag], buffer: CMTaggedBuffer.Buffer)](cmtaggedbuffer/init(tags:buffer:).md)
  Creates a new tagged buffer from tags and an existing media buffer.
- [init(tags: [CMTag], pixelBuffer: CVPixelBuffer)](cmtaggedbuffer/init(tags:pixelbuffer:).md)
  Creates a new tagged buffer from tags and an existing pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffer/init(tags:samplebuffer:))*