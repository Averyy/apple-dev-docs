# AVPlaybackUserInterfaceSeekCapabilities

**Framework**: AVKit  
**Kind**: struct

Describes navigation capabilities of the media source.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct AVPlaybackUserInterfaceSeekCapabilities
```

#### Overview

This option set defines timeline navigation operations. Different content types and sources may have varying levels of navigation support based on technical limitations, licensing restrictions, or content type.

## Topics

### Initializers
- [init(rawValue: UInt)](avplaybackuserinterfaceseekcapabilities/init(rawvalue:).md)
### Type Properties
- [static var scanBackward: AVPlaybackUserInterfaceSeekCapabilities](avplaybackuserinterfaceseekcapabilities/scanbackward.md)
  The source supports backward scanning at accelerated rates for rewind operations. Enables rapid reverse progression through content at speeds greater than normal playback.
- [static var scanForward: AVPlaybackUserInterfaceSeekCapabilities](avplaybackuserinterfaceseekcapabilities/scanforward.md)
  The source supports forward scanning at accelerated rates for fast-forward operations. Enables rapid progression through content at speeds greater than normal playback.
- [static var seek: AVPlaybackUserInterfaceSeekCapabilities](avplaybackuserinterfaceseekcapabilities/seek.md)
  The source supports seeking to specific time positions for precise navigation. Enables jumping directly to any arbitrary point within the seekable time ranges.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [protocol AVPlaybackUserInterfacePlaybackControllable](avplaybackuserinterfaceplaybackcontrollable-9he54.md)
  Provides playback control and state management for media content.
- [enum AVPlaybackUserInterfacePlaybackState](avplaybackuserinterfaceplaybackstate.md)
  Describes possible transport states of the playback source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceseekcapabilities)*