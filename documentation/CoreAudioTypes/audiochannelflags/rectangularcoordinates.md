# rectangularCoordinates

**Framework**: Core Audio Types  
**Kind**: property  
**Role**: Type Property

A flag that indicates the channel uses the speaker position’s cartesian coordinates.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var rectangularCoordinates: AudioChannelFlags { get }
```

```c
kAudioChannelFlags_RectangularCoordinates
```

#### Discussion

This flag is mutually exclusive with [`sphericalCoordinates`](./sphericalcoordinates.md).

## See Also

### Flags
- [static var meters: AudioChannelFlags](./meters.md)
  A flag that indicates that unit values are in meters.
- [static var sphericalCoordinates: AudioChannelFlags](./sphericalcoordinates.md)
  A flag that indicates the channel uses the speaker position’s spherical coordinates.
- [kAudioChannelFlags_AllOff](./kaudiochannelflags_alloff.md)
  All flags are clear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochannelflags/rectangularcoordinates)*