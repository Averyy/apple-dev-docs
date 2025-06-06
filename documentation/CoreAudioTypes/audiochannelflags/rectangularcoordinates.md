# rectangularCoordinates

**Framework**: Core Audio Types  
**Kind**: property

A flag that indicates the channel uses the speaker position’s cartesian coordinates.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var rectangularCoordinates: AudioChannelFlags { get }
```

#### Discussion

This flag is mutually exclusive with [`sphericalCoordinates`](audiochannelflags/sphericalcoordinates.md).

## See Also

- [static var meters: AudioChannelFlags](audiochannelflags/meters.md)
  A flag that indicates that unit values are in meters.
- [static var sphericalCoordinates: AudioChannelFlags](audiochannelflags/sphericalcoordinates.md)
  A flag that indicates the channel uses the speaker position’s spherical coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochannelflags/rectangularcoordinates)*