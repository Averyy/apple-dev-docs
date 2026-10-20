# init(tags:pixelBuffer:)

**Framework**: Core Media  
**Kind**: init  
**Role**: Initializer

Creates a new tagged buffer from tags and an existing pixel buffer.

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
init(tags: [CMTag], pixelBuffer: CVPixelBuffer)
```

## Parameters

- `tags`: The tags to assign to the buffer.
- `pixelBuffer`: A pixel buffer containing image-based media to associate with the tags.

## See Also

### Creating Tagged Buffers
- [init(tags: [CMTag], buffer: CMTaggedBuffer.Buffer)](./init%28tags,buffer%29.md)
  Creates a new tagged buffer from tags and an existing media buffer.
- [init(tags: [CMTag], sampleBuffer: CMSampleBuffer)](./init%28tags,samplebuffer%29.md)
  Creates a new tagged buffer from tags and an existing sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffer/init(tags:pixelbuffer:))*