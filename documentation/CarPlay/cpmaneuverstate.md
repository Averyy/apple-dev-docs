# CPManeuverState

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Values that describe the state of a maneuver.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum CPManeuverState
```

```c
enum CPManeuverState : NSInteger;
```

## Topics

### Getting the maneuver state
- [CPManeuverState.prepare](./cpmaneuverstate/prepare.md)
- [CPManeuverState.initial](./cpmaneuverstate/initial.md)
- [CPManeuverState.execute](./cpmaneuverstate/execute.md)
- [CPManeuverState.continue](./cpmaneuverstate/continue.md)
### Initializers
- [init?(rawValue: Int)](./cpmaneuverstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Maneuvers
- [class CPManeuver](./cpmaneuver.md)
  An object that describes a single navigation instruction.
- [enum CPManeuverType](./cpmaneuvertype.md)
  Values that describe types of navigation maneuvers.
- [class CPTravelEstimates](./cptravelestimates.md)
  An object that describes the time and distance remaining for a maneuver in a navigation session.
- [class CPTripPreviewTextConfiguration](./cptrippreviewtextconfiguration.md)
  A configuration object for changing the button titles on a trip preview.
- [func NSStringFromCPManeuverType(CPManeuverType) -> String!](./nsstringfromcpmaneuvertype%28_%29.md)
- [struct CPLocationCoordinate3D](./cplocationcoordinate3d.md)
  CPLocationCoordinate3D represents a three-dimensional coordinate with latitude, longitude, and altitude components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuverstate)*