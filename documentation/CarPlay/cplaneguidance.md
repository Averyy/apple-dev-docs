# CPLaneGuidance

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A class that provides information that describes the number of lanes on a roadway and navigation instruction variants.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
class CPLaneGuidance
```

```objc
@interface CPLaneGuidance : NSObject
```

## Topics

### Properties
- [var instructionVariants: [String]](./cplaneguidance/instructionvariants.md)
  An array of strings that represent the instruction for this lane guidance, arranged from most- to least-preferred.
- [var lanes: [CPLane]](./cplaneguidance/lanes.md)
  An array of lane objects, each describing a single lane.
### Initializers
- [init?(coder: NSCoder)](./cplaneguidance/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Routes, lanes and junctions
- [class CPRouteInformation](./cprouteinformation.md)
  A class that describes the characteristic elements of a route.
- [class CPLane](./cplane.md)
  A class that describes characteristics of a lane on a roadway.
- [enum CPLaneStatus](./cplanestatus.md)
  Values that describe the status or preferability of a lane.
- [enum CPJunctionType](./cpjunctiontype.md)
  Values that represent types of roadway junctions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplaneguidance)*