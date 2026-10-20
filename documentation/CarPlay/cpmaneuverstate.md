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

### Enumeration Cases
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuverstate)*