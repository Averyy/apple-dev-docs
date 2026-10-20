# CMPedometerEventType

**Framework**: Core Motion  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the change that occurred to the user’s pedestrian activity.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum CMPedometerEventType
```

```c
enum CMPedometerEventType : NSInteger;
```

## Topics

### Enumeration Cases
- [CMPedometerEventType.pause](./cmpedometereventtype/pause.md)
  The user’s pedestrian activity stopped.
- [CMPedometerEventType.resume](./cmpedometereventtype/resume.md)
  The user’s pedestrian activity resumed.
### Initializers
- [init?(rawValue: Int)](./cmpedometereventtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Pedometer Data
- [var date: Date](./cmpedometerevent/date.md)
  The date on which the pedometer event was recorded.
- [var type: CMPedometerEventType](./cmpedometerevent/type.md)
  The type of change that occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometereventtype)*