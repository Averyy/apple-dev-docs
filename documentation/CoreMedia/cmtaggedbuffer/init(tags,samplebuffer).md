# init(tags:sampleBuffer:)

**Framework**: Core Media  
**Kind**: init  
**Role**: Initializer

Creates a new tagged buffer from tags and an existing sample buffer.

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
init(tags: [CMTag], sampleBuffer: CMSampleBuffer)
```

## Parameters

- `tags`: The tags to assign to the buffer.
- `sampleBuffer`: A sample buffer to associate with the tags.

## See Also

### Creating Tagged Buffers
- [init(tags: [CMTag], buffer: CMTaggedBuffer.Buffer)](./init%28tags,buffer%29.md)
  Creates a new tagged buffer from tags and an existing media buffer.
- [init(tags: [CMTag], pixelBuffer: CVPixelBuffer)](./init%28tags,pixelbuffer%29.md)
  Creates a new tagged buffer from tags and an existing pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffer/init(tags:samplebuffer:))*