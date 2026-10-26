# AVPlaybackUserInterfaceSeekCapabilities

**Framework**: AVKit  
**Kind**: struct  
**Role**: Structure

Describes navigation capabilities of the media source.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct AVPlaybackUserInterfaceSeekCapabilities
```

```c
enum AVPlaybackUserInterfaceSeekCapabilities : NSUInteger;
```

#### Overview

This option set defines timeline navigation operations. Different content types and sources may have varying levels of navigation support based on technical limitations, licensing restrictions, or content type.

## Topics

### Initializers
- [init(rawValue: UInt)](./avplaybackuserinterfaceseekcapabilities/init%28rawvalue%29.md)
### Type Properties
- [static var scanBackward: AVPlaybackUserInterfaceSeekCapabilities](./avplaybackuserinterfaceseekcapabilities/scanbackward.md)
  The source supports backward scanning at accelerated rates for rewind operations. Enables rapid reverse progression through content at speeds greater than normal playback.
- [static var scanForward: AVPlaybackUserInterfaceSeekCapabilities](./avplaybackuserinterfaceseekcapabilities/scanforward.md)
  The source supports forward scanning at accelerated rates for fast-forward operations. Enables rapid progression through content at speeds greater than normal playback.
- [static var seek: AVPlaybackUserInterfaceSeekCapabilities](./avplaybackuserinterfaceseekcapabilities/seek.md)
  The source supports seeking to specific time positions for precise navigation. Enables jumping directly to any arbitrary point within the seekable time ranges.
### Enumeration Cases
- [AVPlaybackUserInterfaceSeekCapabilitiesNone](./avplaybackuserinterfaceseekcapabilities/avplaybackuserinterfaceseekcapabilitiesnone.md)
  The source does not support any scanning or seeking operations.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Playback control
- [protocol AVPlaybackUserInterfacePlaybackControllable](./avplaybackuserinterfaceplaybackcontrollable-9he54.md)
  Provides playback control and state management for media content.
- [enum AVPlaybackUserInterfacePlaybackState](./avplaybackuserinterfaceplaybackstate.md)
  Describes possible transport states of the playback source.
- [AVPlaybackUserInterfacePlaybackControllable](./avplaybackuserinterfaceplaybackcontrollable-81n66.md)
  Provides playback control and state management for media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceseekcapabilities)*