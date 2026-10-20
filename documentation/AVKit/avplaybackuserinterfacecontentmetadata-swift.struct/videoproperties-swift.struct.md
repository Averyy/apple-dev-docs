# AVPlaybackUserInterfaceContentMetadata.VideoProperties

**Framework**: AVKit  
**Kind**: struct  
**Role**: Structure

Properties specific to video content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct VideoProperties
```

#### Overview

The presence of a `VideoProperties` instance indicates the content contains video. Use [`AVPlaybackUserInterfaceContentMetadata.VideoProperties`](./videoproperties-swift.struct.md) to provide the natural presentation size for video content.

## Topics

### Initializers
- [init(presentationSize: CGSize)](./videoproperties-swift.struct/init%28presentationsize%29.md)
  Creates a new video properties instance.
### Instance Properties
- [var presentationSize: CGSize](./videoproperties-swift.struct/presentationsize.md)
  The natural pixel dimensions of the video content, used for aspect ratio calculations and layout.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct/videoproperties-swift.struct)*