# AVPlaybackUserInterfaceContentMetadata.VideoProperties

**Framework**: AVKit  
**Kind**: struct

Properties specific to video content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct VideoProperties
```

#### Overview

The presence of a `VideoProperties` instance indicates the content contains video. Use [`AVPlaybackUserInterfaceContentMetadata.VideoProperties`](avplaybackuserinterfacecontentmetadata-swift.struct/videoproperties-swift.struct.md) to provide the natural presentation size for video content.

## Topics

### Initializers
- [init(presentationSize: CGSize)](avplaybackuserinterfacecontentmetadata-swift.struct/videoproperties-swift.struct/init(presentationsize:).md)
  Creates a new video properties instance.
### Instance Properties
- [var presentationSize: CGSize](avplaybackuserinterfacecontentmetadata-swift.struct/videoproperties-swift.struct/presentationsize.md)
  The natural pixel dimensions of the video content, used for aspect ratio calculations and layout.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct/videoproperties-swift.struct)*