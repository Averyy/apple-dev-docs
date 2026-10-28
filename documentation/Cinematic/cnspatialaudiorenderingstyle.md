# CNSpatialAudioRenderingStyle

**Framework**: Cinematic  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CNSpatialAudioRenderingStyle : NSInteger;
```

## Overview

Standard rendering styles for Audio Mix type effects

## Topics

### Enumeration Cases
- [CNSpatialAudioRenderingStyle.cinematic](./cnspatialaudiorenderingstyle/cinematic.md)
  Isolates background and foreground sounds and places them in separate stems.
- [CNSpatialAudioRenderingStyle.cinematicBackgroundStem](./cnspatialaudiorenderingstyle/cinematicbackgroundstem.md)
  Isolates background sounds in a stem.
- [CNSpatialAudioRenderingStyle.cinematicForegroundStem](./cnspatialaudiorenderingstyle/cinematicforegroundstem.md)
  Isolates foreground sounds in a stem.
- [CNSpatialAudioRenderingStyle.inFrame](./cnspatialaudiorenderingstyle/inframe.md)
  Isolates background from foreground sounds in the camera field of view and places them in separate stems.
- [CNSpatialAudioRenderingStyle.inFrameBackgroundStem](./cnspatialaudiorenderingstyle/inframebackgroundstem.md)
  Isolates background plus foreground sounds outside the camera field of view in a stem.
- [CNSpatialAudioRenderingStyle.inFrameForegroundStem](./cnspatialaudiorenderingstyle/inframeforegroundstem.md)
  Isolates foreground sounds within the camera field of view in a stem.
- [CNSpatialAudioRenderingStyle.standard](./cnspatialaudiorenderingstyle/standard.md)
  Produces an unprocessed spatial stem of the original recording. This is the default rendering style.
- [CNSpatialAudioRenderingStyle.studio](./cnspatialaudiorenderingstyle/studio.md)
  Isolates background and foreground in separate stems. Adds a proximity effect to foreground sounds.
- [CNSpatialAudioRenderingStyle.studioBackgroundStem](./cnspatialaudiorenderingstyle/studiobackgroundstem.md)
  Isolates background sounds in a stem.
- [CNSpatialAudioRenderingStyle.studioForegroundStem](./cnspatialaudiorenderingstyle/studioforegroundstem.md)
  Isolates foreground sounds in a stem, and adds a proximity effect.
### Initializers
- [init?(rawValue: Int)](./cnspatialaudiorenderingstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnspatialaudiorenderingstyle)*