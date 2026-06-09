# AVInterfaceMetadata.MediaMode

**Framework**: AVKit  
**Kind**: enum

Describes the type of media content and its display characteristics.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum MediaMode
```

#### Overview

Use `MediaMode` to indicate whether content is audio-only or includes video, and to provide the natural presentation size for video content.

## Topics

### Enumeration Cases
- [AVInterfaceMetadata.MediaMode.audioOnly](avinterfacemetadata-swift.struct/mediamode-swift.enum/audioonly.md)
  The content contains only audio with no video component.
- [AVInterfaceMetadata.MediaMode.video(presentationSize:)](avinterfacemetadata-swift.struct/mediamode-swift.enum/video(presentationsize:).md)
  The content contains video with the specified natural pixel dimensions.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemetadata-swift.struct/mediamode-swift.enum)*