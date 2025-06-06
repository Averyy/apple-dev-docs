# sphericalCoordinates

**Framework**: Core Audio Types  
**Kind**: property

A flag that indicates the channel uses the speaker position’s spherical coordinates.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var sphericalCoordinates: AudioChannelFlags { get }
```

#### Discussion

This flag is mutually exclusive with [`rectangularCoordinates`](audiochannelflags/rectangularcoordinates.md).

## See Also

- [static var meters: AudioChannelFlags](audiochannelflags/meters.md)
  A flag that indicates that unit values are in meters.
- [static var rectangularCoordinates: AudioChannelFlags](audiochannelflags/rectangularcoordinates.md)
  A flag that indicates the channel uses the speaker position’s cartesian coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochannelflags/sphericalcoordinates)*