# CNSpatialAudioRenderingStyle

**Framework**: Cinematic  
**Kind**: enum

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
enum CNSpatialAudioRenderingStyle
```

#### Overview

Standard rendering styles for Audio Mix type effects

## Topics

### Enumeration Cases
- [CNSpatialAudioRenderingStyle.cinematic](cnspatialaudiorenderingstyle/cinematic.md)
  Isolates the ambience and place it in a spatial stem. Isolates all voices and place them in a mono stem.
- [CNSpatialAudioRenderingStyle.cinematicBackgroundStem](cnspatialaudiorenderingstyle/cinematicbackgroundstem.md)
  Isolates the ambience when foreground is cinematic Audio Mix and place it in a spatial stem. There is no voice stem.
- [CNSpatialAudioRenderingStyle.cinematicForegroundStem](cnspatialaudiorenderingstyle/cinematicforegroundstem.md)
  Isolates all voices and places them in a mono stem. There is no ambience stem.
- [CNSpatialAudioRenderingStyle.inFrame](cnspatialaudiorenderingstyle/inframe.md)
  Isolates the ambience and place it in a spatial stem. Isolates only voices from the camera field of view and place them in a mono stem.
- [CNSpatialAudioRenderingStyle.inFrameBackgroundStem](cnspatialaudiorenderingstyle/inframebackgroundstem.md)
  Isolates the ambience and foreground that is out of frame and place it in a spatial stem. There is no voice stem.
- [CNSpatialAudioRenderingStyle.inFrameForegroundStem](cnspatialaudiorenderingstyle/inframeforegroundstem.md)
  Isolates only voices from the camera field of view and place them in a mono stem. There is no ambience stem.
- [CNSpatialAudioRenderingStyle.standard](cnspatialaudiorenderingstyle/standard.md)
  This produces a spatial stem of the original recording that is unprocessed. This is the default rendering style.
- [CNSpatialAudioRenderingStyle.studio](cnspatialaudiorenderingstyle/studio.md)
  Isolates the ambience and place it in a spatial stem. Isolates all voices, add a studio/proximity effect in the voice track and place them in a mono stem.
- [CNSpatialAudioRenderingStyle.studioBackgroundStem](cnspatialaudiorenderingstyle/studiobackgroundstem.md)
  Isolates the ambience when foreground is studio Audio Mix and place it in a spatial stem. There is no voice stem.
- [CNSpatialAudioRenderingStyle.studioForegroundStem](cnspatialaudiorenderingstyle/studioforegroundstem.md)
  Isolates all voices, add a studio/proximity effect in the voice track and place them in a mono stem. There is no ambience stem.
### Initializers
- [init?(rawValue: Int)](cnspatialaudiorenderingstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnspatialaudiorenderingstyle)*