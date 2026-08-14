# CPLaneGuidance

**Framework**: CarPlay  
**Kind**: class

A class that provides information that describes the number of lanes on a roadway and navigation instruction variants.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
class CPLaneGuidance
```

## Topics

### Properties
- [var instructionVariants: [String]](cplaneguidance/instructionvariants.md)
  An array of strings that represent the instruction for this lane guidance, arranged from most- to least-preferred.
- [var lanes: [CPLane]](cplaneguidance/lanes.md)
  An array of lane objects, each describing a single lane.
### Initializers
- [init?(coder: NSCoder)](cplaneguidance/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class CPRouteInformation](cprouteinformation.md)
  A class that describes the characteristic elements of a route.
- [class CPLane](cplane.md)
  A class that describes characteristics of a lane on a roadway.
- [enum CPLaneStatus](cplanestatus.md)
  Values that describe the status or preferability of a lane.
- [enum CPJunctionType](cpjunctiontype.md)
  Values that represent types of roadway junctions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplaneguidance)*