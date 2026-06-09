# AVInterfaceSeekCapabilities

**Framework**: AVKit  
**Kind**: struct

Describes navigation capabilities of the media source.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct AVInterfaceSeekCapabilities
```

#### Overview

This option set defines timeline navigation operations. Different content types and sources may have varying levels of navigation support based on technical limitations, licensing restrictions, or content type.

## Topics

### Creating seek capabilities
- [init(rawValue: UInt)](avinterfaceseekcapabilities/init(rawvalue:).md)
### Seek Capabilities
- [static var seek: AVInterfaceSeekCapabilities](avinterfaceseekcapabilities/seek.md)
  The source supports seeking to specific time positions for precise navigation. Enables jumping directly to any arbitrary point within the seekable time ranges.
- [static var scanForward: AVInterfaceSeekCapabilities](avinterfaceseekcapabilities/scanforward.md)
  The source supports forward scanning at accelerated rates for fast-forward operations. Enables rapid progression through content at speeds greater than normal playback.
- [static var scanBackward: AVInterfaceSeekCapabilities](avinterfaceseekcapabilities/scanbackward.md)
  The source supports backward scanning at accelerated rates for rewind operations. Enables rapid reverse progression through content at speeds greater than normal playback.

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

- [protocol AVInterfacePlaybackControllable](avinterfaceplaybackcontrollable-44aba.md)
  Provides playback control and state management for media content.
- [enum AVInterfacePlaybackState](avinterfaceplaybackstate.md)
  Describes possible playback states of the interface source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfaceseekcapabilities)*