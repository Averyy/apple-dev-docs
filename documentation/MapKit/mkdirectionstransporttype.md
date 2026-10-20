# MKDirectionsTransportType

**Framework**: MapKit  
**Kind**: struct  
**Role**: Structure

Constants that specify the type of conveyance to use.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
struct MKDirectionsTransportType
```

```c
enum MKDirectionsTransportType : NSUInteger;
```

## Topics

### Transport types
- [static var any: MKDirectionsTransportType](./mkdirectionstransporttype/any.md)
  Directions suitable for any transportation option.
- [static var automobile: MKDirectionsTransportType](./mkdirectionstransporttype/automobile.md)
  Directions suitable for use while driving.
- [static var cycling: MKDirectionsTransportType](./mkdirectionstransporttype/cycling.md)
  Directions suitable for use while cycling.
- [static var transit: MKDirectionsTransportType](./mkdirectionstransporttype/transit.md)
  Directions suitable for public transportation.
- [static var walking: MKDirectionsTransportType](./mkdirectionstransporttype/walking.md)
  Directions suitable for a pedestrian.
### Creating direction transport types
- [init(rawValue: UInt)](./mkdirectionstransporttype/init%28rawvalue%29.md)
  Creates a direction transport type using a raw unsigned integer value.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirectionstransporttype)*