# init(tags:buffer:)

**Framework**: Core Media  
**Kind**: init

Creates a new tagged buffer from tags and an existing media buffer.

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
init(tags: [CMTag], buffer: CMTaggedBuffer.Buffer)
```

## Parameters

- `tags`: The tags to assign to the buffer.
- `buffer`: The buffer, wrapped as a  , to associate with the tags.

## See Also

- [init(tags: [CMTag], sampleBuffer: CMSampleBuffer)](cmtaggedbuffer/init(tags:samplebuffer:).md)
  Creates a new tagged buffer from tags and an existing sample buffer.
- [init(tags: [CMTag], pixelBuffer: CVPixelBuffer)](cmtaggedbuffer/init(tags:pixelbuffer:).md)
  Creates a new tagged buffer from tags and an existing pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffer/init(tags:buffer:))*