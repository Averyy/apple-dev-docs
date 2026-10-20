# init(tags:buffer:)

**Framework**: Core Media  
**Kind**: init  
**Role**: Initializer

Creates a new tagged buffer from tags and an existing media buffer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(tags: [CMTag], buffer: CMTaggedBuffer.Buffer)
```

## Parameters

- `tags`: The tags to assign to the buffer.
- `buffer`: The buffer, wrapped as a [`CMTaggedBuffer.Buffer`](./buffer-swift.enum.md), to associate with the tags.

## See Also

### Creating Tagged Buffers
- [init(tags: [CMTag], sampleBuffer: CMSampleBuffer)](./init%28tags,samplebuffer%29.md)
  Creates a new tagged buffer from tags and an existing sample buffer.
- [init(tags: [CMTag], pixelBuffer: CVPixelBuffer)](./init%28tags,pixelbuffer%29.md)
  Creates a new tagged buffer from tags and an existing pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffer/init(tags:buffer:))*